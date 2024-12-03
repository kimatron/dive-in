from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment, Category, UserProfile
from .forms import CommentForm, UserProfileForm
from django.core.files.uploadedfile import SimpleUploadedFile

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create test user
        test_user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Create test category
        test_category = Category.objects.create(
            name='Test Category',
            description='Test Category Description'
        )
        
        # Create test post
        Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=test_user,
            content='Test Content',
            status=1,
            excerpt='Test Excerpt',
            category=test_category
        )

    def test_post_creation(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.slug, 'test-post')
        self.assertEqual(post.status, 1)
        self.assertTrue(post.category is not None)
        
    def test_post_str_method(self):
        post = Post.objects.get(id=1)
        expected_str = f"{post.title} | scribed by {post.author}"
        self.assertEqual(str(post), expected_str)


class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create test user
        test_user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Create test post
        test_post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=test_user,
            content='Test Content',
            status=1
        )
        
        # Create test comment
        Comment.objects.create(
            post=test_post,
            author=test_user,
            body='Test Comment',
            approved=False
        )

    def test_comment_creation(self):
        comment = Comment.objects.get(id=1)
        self.assertEqual(comment.body, 'Test Comment')
        self.assertFalse(comment.approved)
        
    def test_comment_approval(self):
        comment = Comment.objects.get(id=1)
        comment.approved = True
        comment.save()
        self.assertTrue(comment.approved)


class PostViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.category = Category.objects.create(
            name='Test Category',
            description='Test Category Description'
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


class UserProfileTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        # Delete any existing profile (since signals might create one)
        UserProfile.objects.filter(user=self.user).delete()
        # Create new profile
        self.profile = UserProfile.objects.create(
            user=self.user,
            bio='Test Bio',
            location='Test Location',
            certification_level=None,  # Assuming this can be null
            experience_level='beginner',
            preferred_diving_type='recreational'
        )

    def test_profile_creation(self):
        profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(profile.user.username, 'testuser')
        self.assertEqual(profile.bio, 'Test Bio')
        
    def test_profile_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/profile.html')

class CommentFormTest(TestCase):
    def test_comment_form_valid(self):
        form_data = {'body': 'Test Comment Body'}
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
            'certification_level': '',  # or a valid certification level ID if required
            'favorite_dive_site': '',
            'favorite_marine_life': ''
        }
        form = UserProfileForm(data=form_data)
        if not form.is_valid():
            print(form.errors)  # This will help debug any validation errors
        self.assertTrue(form.is_valid())


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(
            name='Test Category',
            description='Test Description'
        )

    def test_category_creation(self):
        category = Category.objects.get(id=1)
        self.assertEqual(category.name, 'Test Category')
        self.assertEqual(category.description, 'Test Description')
        
    def test_category_str_method(self):
        category = Category.objects.get(id=1)
        self.assertEqual(str(category), 'Test Category')