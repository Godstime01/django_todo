from django.forms import ModelForm
from .models import *

class Edit(ModelForm):
  class Meta:
    model = Todo
    fields = '__all__'