from django import forms

class ContactForm(forms.Form):

    from_email = forms.EmailField(required=True)
   # number = forms.CharField(required=True)    
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)
    