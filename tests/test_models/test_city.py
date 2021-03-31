#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.base_model import BaseModel
import unittest
import os

type_storage = os.getenv('HBNB_TYPE_STORAGE')


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    @unittest.skipIf(type_storage == 'db', "No apply for db")
    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    @unittest.skipIf(type_storage == 'db', "No apply for db")
    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


class TestCity(unittest.TestCase):
    """ a class for testing City"""

    @classmethod
    def setUpClass(cls):
        """ Example Data """
        cls.city = City()
        cls.city.name = "San Francisco"
        cls.city.state_id = "san-francisco"

    def teardown(cls):
        """ tear down Class """
        del cls.city

    def tearDown(self):
        """ teard dsdmd """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_City_docs(self):
        """ check for docstring """
        self.assertIsNotNone(City.__doc__)

    def test_City_attribute_types(self):
        """ test City attribute types """
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_City_is_subclass(self):
        """ test if City is subclass of BaseModel """
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "City won't save\
                     because it needs to be tied to a state :\\")
    def test_City_save(self):
        """ test save() command """
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_City_sa_instance_state(self):
        """ test is _sa_instance_state has been removed """
        self.assertNotIn('_sa_instance_state', self.city.to_dict())
