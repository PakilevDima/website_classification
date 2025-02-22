from django import forms
from .models import Image

class ResumeForm(forms.ModelForm):
   class Meta:
      model = Image
      fields = ['image', 'model']