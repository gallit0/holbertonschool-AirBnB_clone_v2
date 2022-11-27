#!/usr/bin/python3
"""
Unit test for the file storage class
"""
import unittest
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from io import StringIO
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """Test console class"""
    def test_console(self):
        with patch('sys.stdout', new=StringIO()) as strio:
            HBNBCommand().onecmd("create State")
            self.assertTrue(len(strio.getvalue()) > 0)
