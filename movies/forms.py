from django import forms

from .models import Reviews


class ReviewForm(forms.ModelForm):
    """Отзывы к фильму"""
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')