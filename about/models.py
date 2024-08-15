from django.db import models


class About(models.Model):
    """
    Model representing the 'About' section of the website, containing details
    about the company.

    Attributes:
        company_name (str): The name of the company.
        founding_date (date): The date when the company was founded.
        mission (str): The mission statement of the company.
        offerings (str): The products or services the company offers.
        updated_on (datetime): The date and time when the record was last updated.
        content (str): Additional content or information about the company.
    """
    company_name = models.CharField(max_length=100)
    founding_date = models.DateField()
    mission = models.TextField()
    offerings = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

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
