#!/usr/bin/python3
"""The imports"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
import shlex

"""The Module HBNBCommand"""


class HBNBCommand(cmd.Cmd):
    """The class HBNBCommand"""

    prompt = "(hbnb) "
    l_classes = [
            'BaseModel',
            'User',
            'Place',
            'State',
            'City',
            'Amenity',
            'Review']

    l_c = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def precmd(self, arg):
        """parses command input"""
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            cnd = cls[1].split('(')
            args = cnd[1].split(')')
            if cls[0] in HBNBCommand.l_classes and cnd[0] in HBNBCommand.l_c:
                arg = cnd[0] + ' ' + cls[0] + ' ' + args[0]
        return arg

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        else:
            class_dict = {
                    'BaseModel': BaseModel,
                    'User': User,
                    'Place': Place,
                    'City': City,
                    'Amenity': Amenity,
                    'State': State,
                    'Review': Review}
            get_model = class_dict[arg]()
            print(get_model.id)
            get_model.save()

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split(' ')
i        if not arg:
            print("** class name missing **")
            return

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
            return

        else:
            all_data = storage.all()
            for k, v in all_data.items():
                data_name = v.__class__.__name__
                data_id = v.id
                if data_name == args[0] and data_id == args[1].strip('"'):
                    print(v)
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based"""

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')
        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        else:
            all_data = storage.all()
            instances = []
            for k, v in all_data.items():
                data_name = v.__class__.__name__
                if data_name == args[0]:
                    instances += [v.__str__()]
            print(instances)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id"""

        if not arg:
            print("** class name missing **")
            return

        a = ""
        for argv in arg.split(','):
            a = a + argv

        args = shlex.split(a)

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_data = storage.all()
            for k, v in all_data.items():
                data_name = v.__class__.__name__
                data_id = v.id
                if data_name == args[0] and data_id == args[1].strip('"'):
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(v, args[2], args[3])
                        storage.save()
                    return
        print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_data = storage.all()
            for k, v in all_data.items():
                data_name = v.__class__.__name__
                data_id = v.id
                if data_name == args[0] and data_id == args[1].strip('"'):
                    del v
                    del storage._FileStorage__objects[k]
                    storage.save()
                    return
            print("** no instance found **")
    
    def emptyline(self):
        """do nothing when empty line"""
        pass

    def do_quit(self, arg):
        """quit command to exit the program"""
        print()
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
