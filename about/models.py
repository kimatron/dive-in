from django.db import models


class About(models.Model):
    company_name = models.CharField(max_length=100)
    founding_date = models.DateField()

    # Hero Section
    hero_title = models.CharField(max_length=200, default="Explore the Depths with Us")
    hero_subtitle = models.TextField(help_text="A brief tagline or introduction")
    hero_image = CloudinaryField('image', null=True, blank=True)

    # Main Content
    mission = models.TextField()
    vision = models.TextField(help_text="Our vision for the diving community")

    # Statistics
    total_divers = models.PositiveIntegerField(default=0, help_text="Number of divers in our community")
    dive_locations = models.PositiveIntegerField(default=0, help_text="Number of dive locations covered")
    articles_written = models.PositiveIntegerField(default=0, help_text="Number of diving articles published")

    # Features
    offerings = models.TextField()
    content = models.TextField()

    # Team Section
    team_description = models.TextField(help_text="Description of our team", blank=True)

    # Contact
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=200, blank=True)

    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "About"

    def __str__(self):
        return self.company_name


class CollaborateRequest(models.Model):
    """
    Model for storing collaboration requests submitted by users.

    Attributes:
        name (str): The name of the user submitting the request.
        email (str): The email address of the user.
        message (str): The message or request content.
        read (bool): A flag indicating whether the request has been read.
        created_on (datetime): The date and time when the request was submitted.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
