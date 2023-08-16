#!/usr/bin/python3
"""
CMD interpreter for AirBnB clone
"""

import cmd

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    HBNBC - a console class for the the airbnb clone
    program
    """

    prompt = '(hbnb) '
    __class_lst = {
        BaseModel.__name__: BaseModel,
        User.__name__: User,
        State.__name__: State,
        City.__name__: City,
        Place.__name__: Place,
        Amenity.__name__: Amenity,
        Review.__name__: Review
    }
    __class_funcs = ["all", "count", "show", "destroy", "update"]

    @staticmethod
    def parse(arg, id=" "):
        """
        Returns a list conatning the parsed arguments from the string
        """

        arg_list = arg.split(id)
        narg_list = []

        for x in arg_list:
            if x != '':
                narg_list.append(x)
        return narg_list

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """Prints help for the quit command"""
        print(self.do_quit.__doc__)
        print("")

    def do_EOF(self, arg):
        """Exits the program"""

        print("")
        return True

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints
        the id.
            Ex: $ create BaseModel
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
        prints Help info for the create function
        """
        print(self.do_create.__doc__)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based
        on the class name and id.
            Ex: $ show BaseModel 1234-1234-1234
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
            Prints Help for for the creat function
        """
        print(self.do_show.__doc__)

    def do_destroy(self, arg):
        """
            Deletes an instance based on the class name and id
            (save the change into the JSON file).
                Ex: $ destroy BaseModel 1234-1234-1234
        """
        args = HBNBCommand.parse(arg)
        storage.reload()
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
            # print(storage.__class__.__name__.__objects)
            del db["{}.{}".format(args[0], args[1])]
            storage.save()

    def help_destroy(self):
        """
            Prints Help for the destroy function
        """
        print(self.do_destroy.__doc__)

    def do_all(self, arg):
        """
            Prints all string representation of all instances based or
            not on the class name.
                Ex: $ all BaseModel or $ all
        """
        arg_list = HBNBCommand.parse(arg)
        if len(arg_list) > 0 and arg_list[0] not in HBNBCommand.__class_lst:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(arg_list) > 0 and arg_list[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(arg_list) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def help_all(self):
        """
            prints help for the all function
        """
        print(self.do_all.__doc__)

    def do_update(self, arg):
        """
            Updates an instance based on the class name and id by adding or
            updating attribute (save the change into the JSON file).
                Ex: $ update BaseModel 1234-1234-1234 email
                      "aibnb@holbertonschool.com"
        """
        arg_list = HBNBCommand.parse(arg)
        objdict = storage.all()

        if len(arg_list) == 0:
            print("** class name missing **")
            return False
        if arg_list[0] not in HBNBCommand.__class_lst:
            print("** class doesn't exist **")
            return False
        if len(arg_list) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_list[0], arg_list[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_list) == 3:
            try:
                type(eval(arg_list[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(arg_list) == 4:
            obj = objdict["{}.{}".format(arg_list[0], arg_list[1])]
            if arg_list[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arg_list[2]])
                obj.__dict__[arg_list[2]] = valtype(arg_list[3])
            else:
                obj.__dict__[arg_list[2]] = arg_list[3]
        elif type(eval(arg_list[2])) == dict:
            obj = objdict["{}.{}".format(arg_list[0], arg_list[1])]
            for k, v in eval(arg_list[2]).items():
                if (k in obj.__class__.__dict__.keys() and type(
                        obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def help_update(self):
        """
        prints Help for the update function
        """
        print(self.do_update.__doc__)

    def emptyline(self):
        """
        Does nothing if Empty line + enter is inserted.
        Used for overriding the emptyline function
        """
        pass

    def do_count(self, arg):
        """
        Prints the number of elements inside the FileStorage that
        are of instances of cls
        """
        arg_list = HBNBCommand.parse(arg)
        if len(arg_list) > 0 and arg_list[0] not in HBNBCommand.__class_lst:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(arg_list) > 0 and arg_list[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(arg_list) == 0:
                    objl.append(obj.__str__())
            print(len(objl))

    def show(self, cls):
        """
        Gives all the elements inside the FileStorage that
        are of instances of cls
        """
        pass

    def destroy(self, cls):
        """
        Gives all the elements inside the FileStorage that
        are of instances of cls
        """
        pass

    def update(self, cls):
        """
        Gives all the elements inside the FileStorage that
        are of instances of cls
        """
        pass

    def default(self, line):
        """
        Handles the case where the the command has no equivlaent
        do_ method
        """

        line_p = HBNBCommand.parse(line, '.')
        if line_p[0] in HBNBCommand.__class_lst.keys() and len(line_p) > 1:
            if line_p[1][:-2] in HBNBCommand.__class_funcs:
                func = line_p[1][:-2]
                cls = HBNBCommand.__class_lst[line_p[0]]
                eval("self.do_" + func)(cls.__name__)
            else:
                print("** class doesn't exist **")
        else:
            super().default(line)
        return False


if __name__ == "__main__":
    console = HBNBCommand()
    console.cmdloop()
