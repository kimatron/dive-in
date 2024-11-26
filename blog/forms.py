from .models import Comment
from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'profile_picture',
            'bio',
            'certification_level',
            'total_dives',
            'experience_level',
            'favorite_dive_site',
            'favorite_marine_life',
            'preferred_diving_type',
            'location',
            'instagram',
            'facebook',
            'twitter'
        ]
        widgets = {
            'bio': forms.Textarea(
                attrs={'rows': 4}
                                ),
            'profile_picture': forms.FileInput(
                attrs={'class': 'form-control-file'}
                                ),
            'certification_date': forms.DateInput(attrs={'type': 'date'}),
            'diving_since': forms.DateInput(attrs={'type': 'date'}),
            'equipment_details': forms.Textarea(attrs={'rows': 4}),
        }


class CommentForm(forms.ModelForm):
    """
    Form for users to submit comments on a blog post.

    Fields:
        body (str): The content of the comment.
    """
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'id': 'id_body', 'name': 'body'})
        }
