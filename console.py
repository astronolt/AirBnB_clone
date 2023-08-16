#!/usr/bin/python3
"""
A console for the airbnb clone
"""

import cmd

from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNBC - Air BnB Console
    """

    prompt = '(hbnb) '
    __class_lst = {
        BaseModel.__name__: BaseModel,
    }
    __class_funcs = ["all", "count", "show", "destroy", "update"]

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

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints
        the id.
        """

        args = HBNBCommand.parse(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False

        if len(args) > 1:
            print("** to many arguments **")
            return False

        if (args[0] in HBNBCommand.__class_lst.keys()):
            new_obj = HBNBCommand.__class_lst[args[0]]()
            new_obj.save()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")

    def help_create(self):
        """
        Prints help for the create command
        """
        print("Creats a new instance of the first argument \
stores it in the JSON file and prints its id")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based
        on the class name and id.
        """
        args = HBNBCommand.parse(arg)
        db = storage.all()
        if not len(args):
            print("** class name missing **")
        elif (args[0] not in HBNBCommand.__class_lst.keys()):
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in db:
            print("** no instance found **")
        else:
            print(db["{}.{}".format(args[0], args[1])])

    def help_show(self):
        """
        Prints help for the show command
        """
        print("Prints the string representation of an instance based \
on the class name and id")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        args = HBNBCommand.parse(arg)
        db = storage.all()
        if not len(args):
            print("** class name missing **")
        elif (args[0] not in HBNBCommand.__class_lst.keys()):
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in db:
            print("** no instance found **")
        else:
            del db["{}.{}".format(args[0], args[1])]
            storage.save()

    def help_destroy(self):
        """
        Prints help for the destroy command
        """
        print("Deletes an instance based on the class name and id \
(save the change into the JSON file)")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        args = HBNBCommand.parse(arg)
        db = storage.all()
        if len(args) == 0:
            for k, v in db.items():
                print(v)
        elif (args[0] not in HBNBCommand.__class_lst.keys()):
            print("** class doesn't exist **")
        else:
            for k, v in db.items():
                if args[0] in k:
                    print(v)

    def help_all(self):
        """
        Prints help for the all command
        """
        print("Prints all string representation of all instances \
based or not on the class name")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into
        the JSON file).
        """
        args = HBNBCommand.parse(arg, " ")
        db = storage.all()
        if not len(args):
            print("** class name missing **")
        elif (args[0] not in HBNBCommand.__class_lst.keys()):
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in db:
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            setattr(db["{}.{}".format(args[0], args[1])], args[2], args[3])
            storage.save()

    def help_update(self):
        """
        Prints help for the update command
        """
        print("Updates an instance based on the class name and id \
by adding or updating attribute (save the change into the JSON file)")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
