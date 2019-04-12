from django import forms

from . models import Tag, Question ,Answer

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['text']
        labels = {'text': 'Enter New Tag Name'}

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']
        labels = {'text':'Enter Question'}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text',]
        labels = {'text':'Your Answer'}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
        