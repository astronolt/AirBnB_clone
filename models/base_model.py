#!/usr/bin/python3

"""
Base model module
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    Base model class for all other models
    """

    def __init__(self) -> None:
        """Initializing the base model instance
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Formal representation of a model object
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates this model
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a JSON representation of this model
        """
        obj = self.__dict__
        obj["__class__"] = self.__class__.__name__
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()
        return obj
