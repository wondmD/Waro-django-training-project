from django.forms import ModelForm
from .models import Postroom
from .models import Gallery

class Postroomform(ModelForm):
    class Meta:
        model = Postroom
        fields = '__all__'
        exclude =['host','participants',]
class Galleryform(ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'