# genai_webapp/forms.py

from django import forms

class CodeUploadForm(forms.Form):
    code_file = forms.FileField()

class QuizUploadForm(forms.Form):
    quiz_text = forms.CharField(widget=forms.Textarea)
