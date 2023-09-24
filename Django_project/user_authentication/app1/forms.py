from django import forms

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ['file']
