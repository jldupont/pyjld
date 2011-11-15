#! /usr/bin/env python
"""
pyjld.logger: cross-platform logging utilities

@author: Jean-Lou Dupont
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id: logger.py 53 2009-04-13 15:57:33Z jeanlou.dupont $"

__all__ = ['logger', 'xcLogger', 'MsgLogger']


import sys
import logging
import logging.handlers

from string import Template


class Proxy(object):
    """
    Proxy helper
    
    This class is meant to be private to this module.
    """
    #easy way to save space in memory
    __slots__ = ['source', 'target']
    
    def __init__(self, source, target):
        self.source = source
        self.target = target
        
    def __call__(self, *pargs, **kwargs):
        return self.target(self.source, *pargs, **kwargs)




class MsgLogger(object):
    """
    Logger with message look-up and & string.Template functionality
    
    :param name: the logger name
    :param messages: the message look-up dictionary
    :param log: an optional logger (instead of the default one)
    :param template_factory: a template factory for handling the messages
    :param filters: a list of callable filters
    :param kwargs: keyword parameters to pass to the __init__ method of the logger
    
    The ``logger`` must have the following methods:
    
    * info
    * debug
    * warning
    * error
    * critical

    The :param template_factory: must have a method ``safe_substitute`` to render
    the messages. It defaults to the ``Template`` class from the standard 
    ``string`` module thus supporting parameters through the escape sequence
    starting with the *$* character eg.  *$var*
    
    A filter entry is a callable which returns a boolean True if the message
    should be suppressed or False otherwise. Each filter is called in turn with the
    following parameters:
    
        method_source, object, \*\*kwargs
        
    where ``method_source`` is one of [info, debug, warning, critical, error] and
    ``object`` corresponds to the first positional parameter found on the
    ``method_source`` call.
    
    **Simple usage** ::
    
        >>> import pyjld.logger
        >>> messages = ["msg1":"Message1 [$var]"] 
        >>> ml = pyjld.logger.MsgLogger("app_name", messages)
        >>> ml.info('msg1', var="variable1")
        ... app_name     INFO    : Message1 [variable1]

    **Auto-Flush**
    
    Once a message is logged, all handlers are visited and flushed. Each
    handler is inspected for the ``flush`` method thus only supported
    handlers are flushed.

    """
    # the expected interface of self.logger
    # =====================================
    _logger_methods = ['info', 'debug', 'warning', 'critical', 'error']
    
    def __init__(self, name, messages, log=None, template_factory = None, filters = None, **kwargs):
        self.messages = messages

        if log:
            self._logger = log
        else:
            self._logger = logger(name, **kwargs)
            
        if template_factory:
            self.template_factory = template_factory
        else:
            self.template_factory = Template
            
        if filters:
            self.filters = filters
        else:
            self.filters = []

            
    def __getattr__(self, attr):
        """
        Catch method for redirecting access to the logger
        """
        if attr in self._logger_methods:
            return Proxy(attr, self.__handler)
        
        raise AttributeError('attribute [%s] not found in logger' % attr)

    def __handler(self, source, object, **kwargs):
        """
        Valid method calls converge here
        """
        # FILTERING STAGE
        # ===============
        must_filter_out = self._performFiltering(source, object, **kwargs)
            
        if must_filter_out:
            return

        id, params = self.getMessageId(object)
                
        # RENDERING STAGE
        # ===============
        if id is not None:
            rendered = self.__handlerForExceptionClass(exc=object)
        else:
            #no, its just a message_id
            message_or_id = object
            rendered = self._render(message_or_id, **kwargs)
        
        # DISPATCH stage
        # ==============
        method = getattr(self._logger, source)
        method(rendered)
        
        self.flush()
        
        
    def flush(self):
        """
        Performs a ``flush`` on each handler that supports it
        """
        for hdlr in self._logger.handlers:
            flush = getattr(hdlr, 'flush', None)
            if flush is not None:
                flush()

        

    @classmethod
    def getMessageId(cls, object):
        """
        Tries to retrieve a ``message_id`` from the object.
        If successful, the said identifier can be used for
        template based substitution as well as for the
        filtering functionality.
        """
        try:
            id      = object.msg_id 
            params  = object.params
        except:
            try:
                id  = object.message_id
                params = object.params
            except:
                id, params = None, None
                
        return id, params 
        
    def addFilter(self, filter_callable):
        """
        Appends a filter to the current list
        """
        self.filters.append(filter_callable)

    def removeFilters(self):
        """
        Removes all filters
        """
        self.filters = []
        
    def addFilters(self, filters):
        """
        Configures the filter list
        """
        self.filters = filters

    def _performFiltering(self, source, object, **kwargs):
        """
        Returns if at most one filter returns True, else False
        """
        for filter in self.filters:
            if not callable(filter):
                RuntimeError("filters must be callable")
                
            if filter(source, object, **kwargs):
                return True # must filter out
        
        #don't filter out
        return False
        

    def _isExceptionInstance(self, object):
        """
        Verifies if the object is compatible with
        the message_id + params templating interface
        """
        try:
            id      = object.msg_id
            params  = object.params
            return True
        except:
            return False


    def __handlerForExceptionClass(self, exc):
        message_id = exc.msg_id
        params = exc.params
        return self._render(message_id, **params)
        
        
    def _render(self, message_id, **kwargs):
        message = self.__resolveMessageFromId(message_id)
        tpl = self.template_factory(message)
        rendered = tpl.safe_substitute( kwargs )
        return rendered
        

    def __resolveMessageFromId(self, message_id):
        """
        Resolve the human readable message from the ``message_id``
        
        If no corresponding message can be found, the ``message_id`` is used as string.
        
        :param message_id: the message identifier from the ``messages`` dictionary
        """
        default = str( message_id )
        if self.messages:
            return self.messages.get(message_id, default)
        
        return default


def logger( name, include_console = False, include_syslog = False, formatter = None, console_stream = None ):
    """ 
    Returns a simple cross-platform logger
    
    If a logger with ``name`` already exists, its handlers are cleared.
    This behavior is especially useful in daemon environments where the daemonize
    process closes open files and the logging facility must be reinitialized.
    
    **Usage** ::    
    
        >>> log = logger.logger('my_logger')
        >>> log.info('message')
    """
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(name)-12s %(levelname)-8s: %(message)s ", )        
        
    if formatter is None:
        formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s: %(message)s ")

    _logger = logging.getLogger(name)
    
    # clear all handlers
    #  This is especially useful in daemon environment
    _logger.handlers = []
    
    if include_syslog:
        syslog = xcLogger( name )
        syslog.setFormatter(formatter)       
        _logger.addHandler(syslog)
        
    if include_console:
        console_stream = console_stream or sys.stdout 
        console = logging.StreamHandler(console_stream)
        console.setFormatter(formatter)
        _logger.addHandler(console)

    return _logger


def xcLogger( appname ):
    """ 
    Cross-platform *syslog* handler
    
    :param appname: the application name to log messages against
    :type appname: string
    
    :rtype: a ``NTEventLogHandler`` for win32 platform OR a ``SysLogHandler`` for Unix/Linux platforms
    
    For Unix/Linux platforms, the filesystem path used is as follows ::
    
        /var/log/$appname.log
    
    The standard ``SysLogHandler`` from the logging package is more difficult
    to configure as it defaults to using the port ``localhost:514``. 
    """
    if (sys.platform[:3] == 'win'):
        return logging.handlers.NTEventLogHandler( appname )
    
    return logging.handlers.TimedRotatingFileHandler('/var/log/%s.log' % appname)

    #More difficult to configure as it defaults to localhost:514 
    #return logging.handlers.SysLogHandler()         
