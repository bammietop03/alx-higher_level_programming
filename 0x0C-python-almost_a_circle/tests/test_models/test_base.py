#!/usr/bin/python3
"""
Test cases for the Base class in models.base module.
"""

import unittest
import pep8
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    A class to test methods and behaviors of the Base class.
    """
    def test_pep8_base(self):
        """
        Test that checks PEP8
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/base.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_instance(self):
        """
        Test Base Class instance
        """
        base_instance = Base()
        self.assertEqual(type(base_instance), Base)
        self.assertTrue(isinstance(base_instance, Base))

    def test_id(self):
        """
        Test for positive Base Class id
        """
        base_instance = Base(110)
        self.assertEqual(base_instance.id, 110)
        base_instance = Base(30)
        self.assertEqual(base_instance.id, 30)

        """
        Test for negative Base Class id
        """
        base_instance = Base(-20)
        self.assertEqual(base_instance.id, -20)
        base_instance = Base(-10)
        self.assertEqual(base_instance.id, -10)

        """
        Test for None Base Class id
        """
	# Reset the counter to 0
        Base._Base__nb_objects = 0

        base_instance = Base()
        self.assertEqual(base_instance.id, 1)
        base_instance = Base(None)
        self.assertEqual(base_instance.id, 2)

        """Test id with string argument"""
        base_instance = Base("Ping Pong")
        self.assertEqual(base_instance.id, "Ping Pong")
        base_instance = Base("Hola soy Goku")
        self.assertEqual(base_instance.id, "Hola soy Goku")

    def test_to_json_string(self):
        """
        Test to_json_string method
        """
        rect_instance = Rectangle(10, 17, 2, 8, 70)
        rect_data = rect_instance.to_dictionary()
        json_data = Base.to_json_string([rect_data])
        self.assertEqual(type(json_data), str)

        """
        Test for a empty data on to_json_string method
        """
        empty_data = []
        json_data = Base.to_json_string(empty_data)
        self.assertEqual(json_data, "[]")

        empty_data = None
        json_data = Base.to_json_string(empty_data)
        self.assertEqual(json_data, "[]")

        """
        Test a correct to_json_string functionality
        """
        rect_data = {'id': 31, 'x': 14, 'y': 10, 'width': 5, 'height': 5}
        json_data = Base.to_json_string([rect_data])

        self.assertTrue(isinstance(rect_data, dict))
        self.assertTrue(isinstance(json_data, str))
        self.assertCountEqual(
            json_data,
            '{["id": 31, "x": 14, "y": 10, "width": 5, "height": 5]}'
        )

        """
        Test a wrong functionality of to_json_string method
        """
        json_data = Base.to_json_string(None)
        self.assertEqual(json_data, "[]")

        warn = ("to_json_string() missing 1 required positional argument: " +
                "'list_dictionaries'")

        with self.assertRaises(TypeError) as msg:
            Base.to_json_string()

        self.assertEqual(warn, str(msg.exception))

        warn = "to_json_string() takes 1 positional argument but 2 were given"

        with self.assertRaises(TypeError) as msg:
            Base.to_json_string([{43, 87}], [{22, 17}])

        self.assertEqual(warn, str(msg.exception))

    def test_save_to_file(self):
        """
        Test save_to_file method
        """
        with self.assertRaises(AttributeError) as msg:
            Base.save_to_file([Base(1), Base(2)])

        # Test saving with None as input
        self.assertIsNone(Rectangle.save_to_file(None))

        # Test saving an empty list of Rectangle instances
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            saved_content = file.read()
            self.assertEqual(saved_content, "[]")

	# Test saving a list containing Rectangle instances
        rect1 = Rectangle(1, 2)
        rect2 = Rectangle(3, 4)
        Rectangle.save_to_file([rect1, rect2])

        # Check the contents of the file
        with open('Rectangle.json', 'r') as f:
            file_contents = f.read()
        expected_json = (
             '[{"x": 0, "y": 0, "id": 4, "height": 2, "width": 1}, '
              '{"x": 0, "y": 0, "id": 5, "height": 4, "width": 3}]')
        self.assertEqual(file_contents, expected_json)
   
	# Test saving to file for Square
        square1 = Square(4, 1, 2, 10)
        square2 = Square(6, 2, 3, 20)
        Square.save_to_file([square1, square2])
        # Check the contents of the file
        with open('Square.json', 'r') as f:
            file_contents = f.read()
        expected_json = '[{"id": 10, "x": 1, "size": 4, "y": 2}, {"id": 20, "x": 2, "size": 6, "y": 3}]'
        self.assertEqual(file_contents, expected_json)

	# Test saving an empty list to file
        Square.save_to_file([])
        # Check the contents of the file
        with open('Square.json', 'r') as f:
            file_contents = f.read()
        self.assertEqual(file_contents, '[]')

    def test_create(self):
        """
        Test cases for the create method
        """
        with self.assertRaises(TypeError) as msg:
            warn = Rectangle.create('Monty Python')

        self.assertEqual(
            "create() takes 1 positional argument but 2 were given",
            str(msg.exception)
        )

        # Test creation of Rectangle with 'id' attribute
        rect = Rectangle.create(**{'id': 89})
        self.assertEqual(rect.id, 89)

        # Test creation of Rectangle with 'id' and 'width' attributes
        rect = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)

        # Test creation of Rectangle with 'id,' 'width,' and 'height' attributes
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

        # Test creation of Rectangle with 'id,' 'width,' 'height,' and 'x' attributes
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)

        # Test creation of Rectangle with 'id,' 'width,' 'height,' 'x,' and 'y' attributes
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

	# Test creation of Square with 'id' attribute
        square = Square.create(**{'id': 89})
        self.assertEqual(square.id, 89)

	# Test creation of Square with 'id' and 'size' attributes
        square = Square.create(**{'id': 89, 'size': 4})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 4)

	# Test creation of Square with 'id,' 'size,' and 'x' attributes
        square = Square.create(**{'id': 89, 'size': 4, 'x': 1})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 1)

	# Test creation of Square with 'id,' 'size,' 'x,' and 'y' attributes
        square = Square.create(**{'id': 89, 'size': 4, 'x': 1, 'y': 2})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)

    def test_load_from_file(self):
        """
        Test load_from_file method
        """
        if os.path.exists("Base.json"):
            os.remove("Base.json")

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        if os.path.exists("Square.json"):
            os.remove("Square.json")

        rect_output = Rectangle.load_from_file()
        self.assertEqual(rect_output, [])

        square_output = Square.load_from_file()
        self.assertEqual(square_output, [])

        warn = "load_from_file() takes 1 positional argument but 2 were given"

        with self.assertRaises(TypeError) as msg:
            Rectangle.load_from_file('Monty Python')

        self.assertEqual(warn, str(msg.exception))
