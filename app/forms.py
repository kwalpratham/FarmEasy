from django import forms
from django.forms import ModelForm
from .models import landModel

class addPostForm(ModelForm):
    class Meta:
        model = landModel
        fields = ('ownerName', 'irrigationSource', 'climateCond', 'cropHistory',
                    'address', 'landSize', 'soilType', 'pub_date', 'thumbnail')
        labels = {
            
        }