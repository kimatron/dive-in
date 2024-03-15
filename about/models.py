from django.db import models


class About(models.Model):
    company_name = models.CharField(max_length=100)
    founding_date = models.DateField()
    mission = models.TextField()
    offerings = models.TextField()

    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.company_name
