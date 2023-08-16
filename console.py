#!/usr/bin/python3
"""
A console for the airbnb clone
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBC - Air BnB Console
    """

    prompt = '(hbnb) '

    @staticmethod
    def parse(arg, id=" "):
        """Returns a list conatning the parsed arguments from the string
        """

        arg_list = arg.split(id)
        narg_list = []

        for x in arg_list:
            if x != '':
                narg_list.append(x)
        return narg_list

    def do_quit(self, arg):
        """Exits the program"""

        return True

    def help_quit(self):
        """Prints help for the quit command"""

        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        """Exits the program"""

        print("")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
