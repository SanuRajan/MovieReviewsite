from django import forms


from .models import Comm


class CommUpdateForm(forms.ModelForm):
    

    class Meta:
        model = Comm
        fields = ['ratings', 'comments',]
