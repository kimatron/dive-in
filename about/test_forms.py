from django.test import TestCase
from .forms import CollaborateForm


class CollaborateFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'collaboration_type': 'article',
            # Using a valid choice from COLLABORATION_TYPES
            'diving_experience': 'PADI Advanced Open Water with 50+ dives',
            'message': 'I would like to contribute a\
            detailed article about diving in the Great Barrier Reef.'
        }
        form = CollaborateForm(data=form_data)
        if not form.is_valid():
            print("Form validation errors:", form.errors)  # For debugging
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {}  # Empty form
        form = CollaborateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5)  # All fields are required

    def test_invalid_collaboration_type(self):
        form_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'collaboration_type': 'invalid_type',  # Invalid choice
            'diving_experience': 'Test Experience',
            'message': 'Test Message'
        }
        form = CollaborateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('collaboration_type', form.errors)

    def test_invalid_email(self):
        form_data = {
            'name': 'Test User',
            'email': 'invalid-email',  # Invalid email format
            'collaboration_type': 'article',
            'diving_experience': 'Test Experience',
            'message': 'Test Message'
        }
        form = CollaborateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
