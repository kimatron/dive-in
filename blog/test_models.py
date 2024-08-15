from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Post, Comment, About, Category, Tag, Subscriber, FeaturedPost, UserProfile
from django.contrib.auth.models import User

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='testpass')
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='This is a test post.',
            status=1
        )

    def test_post_creation(self):
        self.assertTrue(isinstance(self.post, Post))
        self.assertEqual(str(self.post), 'Test Post | scribed by testuser')

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='testpass')
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='This is a test post.',
            status=1
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            body='This is a test comment.'
        )

    def test_comment_creation(self):
        self.assertTrue(isinstance(self.comment, Comment))
        self.assertEqual(str(self.comment), 'Comment This is a test comment. by testuser')

class AboutModelTest(TestCase):
    def setUp(self):
        self.about = About.objects.create(
            company_name='Test Company',
            founding_date='2000-01-01',
            mission='Our mission is to test.',
            offerings='We offer testing services.',
            content='More about us...'
        )

    def test_about_creation(self):
        self.assertTrue(isinstance(self.about, About))
        self.assertEqual(str(self.about), 'Test Company')
