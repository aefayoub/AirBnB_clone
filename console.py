#!/usr/bin/python3
"""The imports"""
import cmd

"""The Module HBNBCommand"""


class HBNBCommand(cmd.Cmd):
    """The class HBNBCommand"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
