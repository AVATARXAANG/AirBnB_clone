#!/usr/bin/python3
"""command interpreter entry module"""

import cmd
import json
import re
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """command interpreter class"""
    prompt = "(hbnb)"

    def do_quit(self, line):
         """allows smooth exit from the program using: quit"""
         return True

    def do_EOF(self, line):
         """Handling End of File character"""
         print()
         return True

    def do_emptyline(self):
        """handling empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

