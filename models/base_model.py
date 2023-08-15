#!/usr/bin/python3

"""
Base model module
"""

from copy import deepcopy
import uuid
from datetime import datetime

from . import storage


class BaseModel:
    """
    Base model class for all other models
    """

    def __init__(self, *args, **kwargs) -> None:
        """Initializing the base model instance
        """
        if kwargs:
            created_at = kwargs.pop("created_at", None)
            updated_at = kwargs.pop("updated_at", None)
            self.created_at = datetime.strptime(
                created_at, "%Y-%m-%dT%H:%M:%S.%f") \
                if created_at else datetime.now()
            self.updated_at = datetime.strptime(
                updated_at, "%Y-%m-%dT%H:%M:%S.%f") \
                if updated_at else datetime.now()
            self.id = kwargs.pop("id", str(uuid.uuid4()))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Formal representation of a model object
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates this model
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a JSON representation of this model
        """
        obj = deepcopy(self.__dict__)
        obj["__class__"] = self.__class__.__name__
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()
        return obj
