from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    COLLABORATION_TYPES = [
        ('article', 'Article Contribution'),
        ('photography', 'Underwater Photography'),
        ('review', 'Diving Location Review'),
        ('guide', 'Diving Guide Feature'),
        ('other', 'Other')
    ]

    collaboration_type = forms.ChoiceField(choices=COLLABORATION_TYPES)
    diving_experience = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}),
                                        help_text="Brief description of your diving experience")

    class Meta:
        model = CollaborateRequest
        fields = ['name', 'email', 'collaboration_type', 'diving_experience', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4,
                                    'placeholder': 'Tell us more about your collaboration idea...'}),
        }
