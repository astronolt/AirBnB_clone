#!/usr/bin/python3

"""
Tests for the base_model class
"""

from datetime import datetime
import os
from unittest import TestCase

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(TestCase):

    def tearDown(self) -> None:
        """Tears down the test
        """
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_create(self):
        """Test creating an instance of the BaseModel class
        """
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)
        self.assertIs(type(b.created_at), datetime)
        self.assertIs(type(b.updated_at), datetime)
        self.assertIsNotNone(b.id)

    def test_create_with_kwargs(self):
        """Test creating an instance of the BaseModel class with kwargs
        """
        b = BaseModel(id="123", created_at=datetime.now().isoformat(),
                      updated_at=datetime.now().isoformat())
        self.assertIsInstance(b, BaseModel)
        self.assertIsInstance(b.id, str)
        self.assertEqual(b.id, "123")
        self.assertIsInstance(b.created_at, datetime)
        self.assertIsInstance(b.updated_at, datetime)

    def test_str(self):
        """Test the __str__ method
        """
        b = BaseModel()
        self.assertEqual(str(b), "[BaseModel] ({}) {}".format(
            b.id, b.__dict__))

    def test_save(self):
        """Test the save method
        """
        b = BaseModel()
        old = b.updated_at
        FileStorage._FileStorage__file_path = "test.json"
        b.save()
        self.assertNotEqual(old, b.updated_at)

    def test_to_dict(self):
        """Test the to_dict method
        """
        b = BaseModel()
        d = b.to_dict()
        self.assertIs(type(d), dict)
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertEqual(d["created_at"], b.created_at.isoformat())
        self.assertEqual(d["updated_at"], b.updated_at.isoformat())
        self.assertEqual(d["id"], b.id)
