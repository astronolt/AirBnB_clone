#!/usr/bin/python3

"""
FileStorage module
"""


import json


class FileStorage:
    """
    FileStorage class
    """

    __file_path = ""
    __objects = {}

    def all(self):
        """Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id

        :param self: Instance of FileStorage
        :type self: FileStorage
        :param obj: Object to set in __objects
        :type obj: BaseModel
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing. If the file doesn't
        exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, "r") as f:
                content = f.read()
                if content:
                    self.__objects = json.loads(content)
        except FileNotFoundError:
            pass
