from django.test import TestCase
from django.urls import reverse

from about.models import CollaborateRequest
from .models import About, Post, User
from .forms import CollaborateForm


class AboutPageViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser', password='testpass')
        self.about_url = reverse('about')

    def test_about_page_status_code(self):
        response = self.client.get(self.about_url)
        self.assertEqual(response.status_code, 200)

    def test_about_page_template(self):
        response = self.client.get(self.about_url)
        self.assertTemplateUsed(response, 'about/about.html')

    def test_about_page_context(self):
        response = self.client.get(self.about_url)
        self.assertIn('about', response.context)
        self.assertIsInstance(response.context['about'], About)


class CollaborateFormViewTest(TestCase):
    def setUp(self):
        # Assuming the collaborate form is on the about page
        self.url = reverse('about')

    def test_form_submission(self):
        data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'message': 'I would like to collaborate.'
        }
        response = self.client.post(self.url, data)
        # Check for a redirect after form submission
        self.assertEqual(response.status_code, 302)
        self.assertTrue(CollaborateRequest.objects.exists())
