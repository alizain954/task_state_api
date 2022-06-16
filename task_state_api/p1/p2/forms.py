
from django import forms
from .models import *


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title',)

    def __init__(self, *args, **kwargs):
        super(AddTaskForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control border-input'
