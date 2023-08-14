#!/usr/bin/python3

"""
Tests for the base_model class
"""

from datetime import datetime
from unittest import TestCase


class TestBaseModel(TestCase):
    def test_create(self):
        """Test creating an instance of the BaseModel class
        """
        from models.base_model import BaseModel
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)
        self.assertIs(type(b.created_at), datetime)
        self.assertIs(type(b.updated_at), datetime)
        self.assertIsNotNone(b.id)

    def test_str(self):
        """Test the __str__ method
        """
        from models.base_model import BaseModel
        b = BaseModel()
        self.assertEqual(str(b), "[BaseModel] ({}) {}".format(
            b.id, b.__dict__))

    def test_save(self):
        """Test the save method
        """
        from models.base_model import BaseModel
        b = BaseModel()
        old = b.updated_at
        b.save()
        self.assertNotEqual(old, b.updated_at)
    
    def test_to_dict(self):
        """Test the to_dict method
        """
        from models.base_model import BaseModel
        b = BaseModel()
        d = b.to_dict()
        self.assertIs(type(d), dict)
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertEqual(d["created_at"], b.created_at.isoformat())
        self.assertEqual(d["updated_at"], b.updated_at.isoformat())
        self.assertEqual(d["id"], b.id)
