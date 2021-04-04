from django import forms
from companies.models import Experience


class ExperienceUpdateForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    # first_name = forms.CharField(
    #     label='',
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'First Name',
    #             'id': 'input-first-name'
    #             }
    #         )
    #     )

    class Meta:
        model = Experience
        exclude = ('user',)
