from django import forms
from .models import CollaborateRequest

class CollaborateForm(forms.ModelForm):
    """
    A form for submitting collaboration requests.

    This form is based on the `CollaborateRequest` model and includes fields
    for the user's name, email, and message. The 'read' field is excluded as per
    requirements.

    Attributes:
        Meta (class): Contains metadata for the form, including the model to base it on,
            the fields to include, and any widget customizations.
            - model (CollaborateRequest): The model that the form is based on.
            - fields (list): List of fields to be included in the form.
            - widgets (dict): Custom widget configuration, such as setting the size of the textarea for the message field.
    """
    class Meta:
        model = CollaborateRequest
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
