from django import forms
from .models import Friend


        
class HelloForm(forms.Form):
    id = forms.IntegerField(label='ID')

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'mail' , 'age', 'birthday']
        
    gender = forms.TypedChoiceField(
        widget=forms.RadioSelect,
        required=True,
    )
    
    birthday = forms.DateField(
        label = 'BIRTHDAY',
        widget=forms.SelectDateWidget(years=[x for x in range(1990, 2019)]),
    )
    