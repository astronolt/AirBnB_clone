#!/usr/bin/python3

"""
Tests for the base_model class
"""

import json
from unittest import TestCase

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(TestCase):

    def tearDown(self) -> None:
        """Tears down the test"""
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def setUp(self) -> None:
        """Sets up the test"""
        FileStorage._FileStorage__objects = {}
        FileStorage._FileStorage__file_path = "file.json"

    def test_all(self):
        """Tests the all method"""
        fs = FileStorage()
        self.assertEqual(fs.all(), {})

    def test_new(self):
        """Tests the new method"""
        fs = FileStorage()
        bm = BaseModel()
        fs.new(bm)
        self.assertDictEqual(
            fs.all(), {"BaseModel.{}".format(bm.id): bm.to_dict()})

    def test_save(self):
        """Tests the save method"""
        fs = FileStorage()
        bm = BaseModel()
        fs.new(bm)
        fs.save()
        with open(fs._FileStorage__file_path, "r") as f:
            content = f.read()
            loaded = json.loads(content)
            self.assertDictEqual(
                loaded, {"BaseModel.{}".format(bm.id): bm.to_dict()})

    def test_empty_save(self):
        """Tests the save method with no objects"""
        fs = FileStorage()
        fs.save()
        with open(fs._FileStorage__file_path, "r") as f:
            content = f.read()
            loaded = json.loads(content)
            self.assertDictEqual(loaded, {})

    def test_reload(self):
        """Tests the reload method"""
        fs = FileStorage()
        bm = BaseModel()
        fs.new(bm)
        fs.save()
        fs.reload()
        self.assertEqual(
            fs.all(), {"BaseModel.{}".format(bm.id): bm.to_dict()})
