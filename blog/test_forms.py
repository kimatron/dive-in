from django.test import TestCase
from .forms import CommentForm, UserProfileForm
from django.contrib.auth.models import User

class CommentFormTest(TestCase):
    def test_comment_form_valid(self):
        form_data = {'body': 'Test comment'}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_comment_form_invalid(self):
        form_data = {'body': ''}
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())

class UserProfileFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
    def test_profile_form_valid(self):
        form_data = {
            'bio': 'Test Bio',
            'location': 'Test Location',
            'experience_level': 'beginner',
            'preferred_diving_type': 'recreational',
            'total_dives': 0,
            'favorite_dive_site': 'Test Site',
            'favorite_marine_life': 'Test Marine Life'
        }
        form = UserProfileForm(data=form_data)
        if not form.is_valid():
            print("Form errors:", form.errors)
        self.assertTrue(form.is_valid())

    def test_profile_form_invalid(self):
        form_data = {'bio': 'x' * 501}  # Bio exceeding max length
        form = UserProfileForm(data=form_data)
        self.assertFalse(form.is_valid())