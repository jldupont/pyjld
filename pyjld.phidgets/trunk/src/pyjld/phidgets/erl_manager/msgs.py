#!/usr/bin/env python
"""
pyjld.phidgets.erl_manager.msgs
"""
__author__  = "Jean-Lou Dupont"
__email     = "python (at) jldupont.com"
__fileid    = "$Id: msgs.py 71 2009-04-20 13:53:31Z jeanlou.dupont $"

__all__ = ['messages',]

messages ={

'error_invalid_command':'ERROR: invalid command [$cmd]',

#Daemon related
'error_pidfile_locked':                 'PID File locked. Is the daemon already running?',
'error_pidfile_not_locked':             'PID File not locked. Is the daemon really running?',
'error_daemon_aborted':                 'Daemon aborted',
'error_daemon_open':                    'Failed to open daemon',
'error_daemon_terminate_process':       'Failed to terminate daemon process. Is the daemon',
'error_daemon_openfilepath':            'Cannot open filepath [$path]',
'error_application_method_not_found':   'Application method[$method] missing',

# PHIDGETS related
'error_creating_phidgets_manager':      'Cannot create Phidget Manager',
'error_setting_handlers':               'Cannot set onAttach/onDetach handlers',
'error_opening_phidget_manager':        'Cannot open Phidget Manager',

'info_phidget_attached':                'Found phidget, type[$type] name[$name] serial[$serial] version[$version]',
'info_phidget_attached_without_info':   'Found phidget but cannot retrieve info',
'info_phidget_detached':                'Phidget detached type[$type] name[$name] serial[$serial] version[$version]',
'info_phidget_detached_without_info':   'Phidget detached but cannot retrieve info',

'error_phidget_device':                 'Cannot get attribute ``device`` from event [$event]',
'error_phidget_error_event':            'Phidget Manager fires an "error event"',

'error_untrapped':                      'Untrapped error [$exc]',

# Erlang related
'':'',
'':'',


# HELP related:
'help_erl_name':                        'Erlang server name',
'help_erl_port':                        'Erlang server port',
'help_erl_cookie':                      'Erlang secret cookie',
}
