import unittest
from dictify import *


class TestModel(unittest.TestCase):
    def setUp(self):
        class TestModel(Model):
            name = Field().type(str)

        self.model = TestModel({'name': 'initial name'})

    def test_ModelDict(self):
        with self.assertRaises(ValueError):
            self.model['name'] = 0
        self.assertEqual(self.model['name'], 'initial name')
        self.model['name'] = 'new name'
        self.assertEqual(self.model['name'], 'new name')


class TestField(unittest.TestCase):
    def setUp(self):
        def add_10(value):
            return value + 10

        class TestModel(Model):
            required = Field().required()
            default = Field().default(1)
            type = Field().type(str)
            match = Field().match('[0-9]+')
            apply = Field().default(10).apply(add_10)
            length = Field().length(min=2, max=10)
            range = Field().range(min=0, max=20)
            any = Field().any([1, 2, 3])
            subset = Field().subset([1, 2, 3])

        self.model = TestModel({'required': True})

    def test_required(self):
        required = self.model['required']
        with self.assertRaises(ValueError):
            self.model['required'] = None
            self.assertEqual(self.model['required'], required)

    def test_default(self):
        self.assertEqual(self.model['default'], 1)

    def test_type(self):
        t = self.model['type']
        with self.assertRaises(ValueError):
            self.model['type'] = 1
            self.assertEqual(self.model['type'], t)

    def test_match(self):
        self.model['match'] = '0123456789'
        match = self.model['match']
        with self.assertRaises(ValueError):
            self.model['match'] = 'a'
            self.assertEqual(self.model['match'], match)

    def test_apply(self):
        self.assertEqual(self.model['apply'], 20)

    def test_length(self):
        self.model['length'] = 'hello'
        with self.assertRaises(ValueError):
            self.model['length'] = 'test-with-lenght-more-than-10'

    def test_any(self):
        self.model['any'] = 1
        with self.assertRaises(ValueError):
            self.model['any'] = 5

    def test_subset(self):
            self.model['subset'] = [1, 2, 3]
