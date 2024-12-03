from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post
from .models import About, CollaborateRequest
from django.utils import timezone
import datetime


class AboutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.about = About.objects.create(
            company_name='Test Company',
            founding_date=datetime.date(2020, 1, 1),
            mission='Test Mission',
            vision='Test Vision',
            offerings='Test Offerings',
            content='Test Content',
            hero_title='Welcome to Test Company',
            hero_subtitle='Explore the depths with Test Company',
            total_divers=100,
            dive_locations=50,
            articles_written=25,
            contact_email='test@example.com',
            contact_phone='+1234567890',
            location='Test Location'
        )

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about.html')
        
    def test_about_content(self):
        """Test that about page contains the correct content"""
        response = self.client.get(reverse('about'))
        content = response.content.decode()
        
        # Test hero section content
        self.assertIn('Welcome to Test Company', content)
        self.assertIn('Explore the depths with Test Company', content)
        
        # Test mission and vision
        self.assertIn('Test Mission', content)
        self.assertIn('Test Vision', content)
        
        # Test stat elements presence (not the actual numbers as they're loaded via JS)
        self.assertIn('stat-number', content)
        self.assertIn('Community Members', content)
        self.assertIn('Dive Locations', content)
        self.assertIn('Articles Published', content)
        
        # Test contact information
        self.assertIn('test@example.com', content)
        self.assertIn('+1234567890', content)
        
    def test_context_data(self):
        """Test that the about data is correctly passed to the template context"""
        response = self.client.get(reverse('about'))
        self.assertIn('about', response.context)
        about = response.context['about']
        
        # Test context values
        self.assertEqual(about.company_name, 'Test Company')
        self.assertEqual(about.mission, 'Test Mission')
        self.assertEqual(about.vision, 'Test Vision')
        self.assertEqual(about.total_divers, 100)
        self.assertEqual(about.dive_locations, 50)
        self.assertEqual(about.articles_written, 25)