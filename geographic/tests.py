"""Tests for geographic app."""
from django.db import transaction
from django.db.utils import IntegrityError
from django.test import TestCase

from geographic.models import AdministrativeArea


class TestGeographic(TestCase):
    """Test class for geographic app."""

    def test_administrative_areas(self):
        """Test mandatory field of AdministrativeArea model."""
        try:
            with transaction.atomic():
                AdministrativeArea.objects.create(
                    name=None,
                    number=None,
                    uf=None,
                )

            self.fail()
        except IntegrityError:
            pass

        area2 = AdministrativeArea.objects.create(
            name='Test',
            number='II',
            uf='DF',
        )

        self.assertNotEqual(area2.id, None)
