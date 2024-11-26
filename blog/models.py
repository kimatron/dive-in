from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone

STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    """
    Represents a category for organizing blog posts.

    Attributes:
        name (str): The name of the category.
        description (str): A description of the category.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Represents a blog post.

    Attributes:
        title (str): The title of the post, must be unique.
        slug (str): The URL-friendly version of the title, must be unique.
        author (User): The author of the post, linked to the User model.
        featured_image (CloudinaryField): The image associated with the post, defaults to a placeholder.
        content (str): The main content of the post.
        created_on (datetime): The date and time when the post was created, automatically set on creation.
        status (int): The publication status of the post (0 for Draft, 1 for Published).
        excerpt (str): A short summary of the post, can be left blank.
        updated_on (datetime): The date and time when the post was last updated, automatically set on update.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="posts")
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | scribed by {self.author}"

    def get_related_posts(self):
        """
        Returns related posts based on category and tags.
        Prioritizes posts that share both category and tags.
        """
        related_posts = Post.objects.filter(status=1).exclude(id=self.id)

        # Get posts from same category
        category_posts = related_posts.filter(category=self.category) if self.category else related_posts.none()

        # Get posts with similar tags
        tag_posts = related_posts.filter(tags__in=self.tags.all()).distinct() if self.tags.exists() else related_posts.none()

        # Combine and order the results
        combined_posts = (category_posts | tag_posts).distinct().order_by('-created_on')

        return combined_posts[:3]  # Return top 3 related posts


class Comment(models.Model):
    """
    Represents a comment on a blog post.

    Attributes:
        post (Post): The post that the comment is associated with.
        author (User): The author of the comment, linked to the User model.
        body (str): The content of the comment.
        approved (bool): Whether the comment is approved for display.
        created_on (datetime): The date and time when the comment was created, automatically set on creation.
        updated_on (datetime): The date and time when the comment was last updated, automatically set on update.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"


class About(models.Model):
    """
    Represents information about the company.

    Attributes:
        company_name (str): The name of the company.
        founding_date (date): The date when the company was founded.
        mission (str): The mission statement of the company.
        offerings (str): The products or services offered by the company.
        updated_on (datetime): The date and time when the information was last updated, automatically set on update.
        content (str): Additional content or description about the company.
    """
    company_name = models.CharField(max_length=100)
    founding_date = models.DateField()
    mission = models.TextField()
    offerings = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.company_name


class Tag(models.Model):
    """
    Represents a tag for categorizing blog posts.

    Attributes:
        name (str): The name of the tag.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    """
    Represents a subscriber to the blog's newsletter.

    Attributes:
        email (str): The email address of the subscriber.
        name (str): The name of the subscriber.
        subscribed_on (datetime): The date and time when the subscription was made, automatically set on creation.
        active (bool): Whether the subscription is active.
    """
    email = models.EmailField()
    name = models.CharField(max_length=100)
    subscribed_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.email


class FeaturedPost(models.Model):
    """
    Represents a featured blog post.

    Attributes:
        post (Post): The post that is marked as featured.
        is_featured (bool): Whether the post is currently featured.
    """
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False)


class CertificationLevel(models.Model):
    """Represents different diving certification levels"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    EXPERIENCE_LEVELS = [
        ('beginner', 'Beginner (0-20 dives)'),
        ('intermediate', 'Intermediate (21-50 dives)'),
        ('advanced', 'Advanced (51-100 dives)'),
        ('expert', 'Expert (100+ dives)')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    # Diving specific fields
    certification_level = models.ForeignKey(
        CertificationLevel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    total_dives = models.PositiveIntegerField(default=0)
    experience_level = models.CharField(
        max_length=20,
        choices=EXPERIENCE_LEVELS,
        default='beginner'
    )
    favorite_dive_site = models.CharField(max_length=200, blank=True)
    favorite_marine_life = models.CharField(max_length=200, blank=True)
    preferred_diving_type = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=200, blank=True)

    # Social media links
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)

    # Additional fields with defaults
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
