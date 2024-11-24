from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings


class CustomAccountAdapter(DefaultAccountAdapter):
    def get_from_email(self):
        """
        This ensures Django-allauth uses your verified sender email
        """
        return settings.DEFAULT_FROM_EMAIL

    def send_mail(self, template_prefix, email, context):
        """
        Override the default email sending to ensure consistent sender
        """
        context['current_site'] = 'Dive In Blog'
        msg = self.render_mail(template_prefix, email, context)
        msg.send()
