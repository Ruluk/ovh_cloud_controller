import sys
from getopt import getopt

from . import instance, backup

_commands = {
    "help": lambda opts, arg:
    print(_help()),
}

_subcommands = {
    "instance": instance.commands,
    "backup": backup.commands,
}


def run():
    all_args = sys.argv

    if len(all_args) < 2:
        print(_help())
        sys.exit(0)

    if all_args[1] in _commands:
        command = _commands[all_args[1]]
        command_arg_index = 2
    elif all_args[1] in _subcommands and all_args[2] in _subcommands[all_args[1]]:
        command = _subcommands[all_args[1]][all_args[2]]
        command_arg_index = 3
    else:
        print(_help())
        sys.exit(0)

    opts, args = getopt(all_args[command_arg_index:], "", ["instance-model=", "region="])

    if len(args) == 0:
        command(opts, "")
    else:
        command(opts, args[0])


def _help() -> str:
    return """
Usage: main.py <command>
 
Available commands:
help

backup create-from-instance <instance-name>

instance create-from-latest-backup [--region=BHS5] [--instance-model=s1-2] <backup-prefix>
instance delete <instance-name>
instance wait-ready <instance-name>
"""
