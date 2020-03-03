from django import forms
from .models import Question
class FriendlyForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']
