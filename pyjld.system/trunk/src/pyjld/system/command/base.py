""" 
pyjld.system.command.base
"""
__author__  = "Jean-Lou Dupont"
__version__ = "$Id: base.py 38 2009-04-03 15:37:33Z jeanlou.dupont $"

__dependencies__ = []

__all__ = ['BaseCmd', 'BaseCmdException']

import sys


class BaseCmdException(Exception):
    """
    Base class for exceptions of this module
    """
    def __init__(self, msg, params = None):
        Exception.__init__(self, msg)
        self.msg = msg
        self.params = params


class metaBaseCmd(type):
    """
    Meta-class used in the command discovery process
    """
    
    _prefix = 'cmd_'
    
    def __init__(cls, name, bases, ns):
        cls._extractCommands(ns)

    def _extractCommands(cls, ns):
        ""
        cls.commands = filter( lambda X: str(X).startswith(cls._prefix), ns )
        cls.cmds = map( lambda X: str(X)[len(cls._prefix):], cls.commands )



class BaseCmd(object):
    """ 
    Base class for command line utilities

    The functionality of this class includes:
    
    * automatic discovery of declared commands i.e. methods with starting prefix `cmd_`
    * automatic generation of the help command for each discoverd commands
    """
    __metaclass__ = metaBaseCmd

    _platform_win32 = sys.platform[:3] == 'win'
    
    _prefix_cmd    = 'cmd_'
    _prefix_test   = 'test_'
    _prefix_config = 'config_'
    
    def __init__(self):
        """ Scans through all the methods of this instance
            and extracts all the ones prefixed with 'cmd_'
        """
        #self._discoverCommands()
        self._genCommandsHelp()        
        
    def _discoverCommands(self):
        """
        Discovers the commands declared in the class 
        """
        commands = filter( lambda X: str(X).startswith(self._prefix_cmd), self.__dict__)
        self.commands.extend( commands )
        cmds = map( lambda X: str(X)[len(self._prefix):], commands )
        self.cmds.extend( cmds )



    def _genCommandsHelp(self, padding=15):
        """ 
        Generates the list of commands and their corresponding docstring
        
        The result is stored in the local attribute :attr:`command_help`.
        Methods with prefix ``test_`` are ignored.
        
        :param padding: the number of spaces used for padding each line
        """
        self.commands_help = ''
        for cmd in self.commands:
            if (cmd.startswith(self._prefix_test)):
                continue

            name = str(cmd)[len(self._prefix_cmd):]
            method = getattr(self, cmd)
            try:    doc = getattr(method, '__doc__')
            except: doc = ''

            line = "%*s : %s\n" % (padding,name,doc)
            self.commands_help = self.commands_help + line



    def validateCommand(self, command):
        """ 
        Validates the specified command against the list
        of discovered commands i.e. methods starting 
        with ``cmd_``.  Raises :class:`BaseCmdException` 
        if the command is not found.
        """ 
        if (command not in self.cmds):
            raise BaseCmdException( 'error_invalid_command', {'cmd':command} )


    def safe_validateCommand(self, command):
        """ 
        Validates the specified command against the list
        of discovered commands i.e. methods starting 
        with ``cmd_``. 
        :rtype: boolean
        """ 
        return command in self.cmds


    def iterconfig(self):
        """ 
        Iterator for the configuration parameters
        
        Iterates through all the class attributes starting 
        with ``config_``.        
        """
        for name in self.__dict__:
            if name.startswith(self._prefix_config):
                value = getattr(self, name)
                yield (name, value) 

        raise StopIteration


    def itercommands(self):
        """ 
        Iterator for the discovered commands
        """
        for cmd in self.commands:
            yield cmd
            
        raise StopIteration 


    def getConfig(self):
        """
        Returns a dictionary containing all the ``config_`` attributes
        """
        result = {}
        for key, value in self.iterconfig():
            result[key] = value
            
        return result