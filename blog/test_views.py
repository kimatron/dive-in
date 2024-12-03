from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Category, Comment

class BlogViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.category = Category.objects.create(
            name='Test Category',
            description='Test Description'
        )
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='Test Content',
            status=1,
            category=self.category
        )

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=['test-post']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_comment_post(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(
            reverse('post_detail', args=['test-post']),
            {'body': 'Test Comment'}
        )
        self.assertEqual(response.status_code, 302)  # Redirect after comment
        self.assertTrue(Comment.objects.filter(body='Test Comment').exists())