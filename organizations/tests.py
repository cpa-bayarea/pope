"""Tests for organizations app."""
import unittest
from django.forms import ValidationError

from organizations.validators import validate_CNPJ


class TestCNPJValidator(unittest.TestCase):
    """Testing CNPJ validator."""

    def test_valid_cnpj(self):
        """Tests for valid CNPJs."""
        test_load = [
            '78144240000157',
            '01005787000147',
            '38213075000123',
            '43540770000130',
            '37582260000122',
        ]
        for cnpj in test_load:
            self.assertEqual(validate_CNPJ(cnpj), cnpj)

    def test_invalid_length(self):
        """Test if it fails for CNPJ wrong length."""
        with self.assertRaises(ValidationError):
            validate_CNPJ('123')

        with self.assertRaises(ValidationError):
            validate_CNPJ('123123123123123123123')

    def test_invalid_cnpj(self):
        """Test if it fails for invalid CNPJ."""
        test_load = [
            '78144240000199',
            '01005787000199',
            '38213075000199',
            '43540770000199',
            '37582260000199',
        ]
        for cnpj in test_load:
            with self.assertRaises(ValidationError):
                validate_CNPJ(cnpj)
