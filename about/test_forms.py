from django.test import TestCase
from .forms import CollaborateForm


class CollaborateFormTest(TestCase):
    def test_valid_form(self):
        form = CollaborateForm(data={
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'message': 'I would like to collaborate.'
        })
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = CollaborateForm(data={
            'name': '',
            'email': 'not-an-email',
            'message': ''
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)  # Check number of errors
