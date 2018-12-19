from django import forms
from .models import Friends


        
class HelloForm(forms.Form):
    id = forms.IntegerField(label='ID')

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friends
        fields = ['car_name',  'use_day','want_go']
        
        # gender = forms.TypedChoiceField(
        # widget=forms.RadioSelect,
        # required=True, )
    
        use_day = forms.DateField(
            label = 'use_day',
            widget=forms.SelectDateWidget(years=[x for x in range(1990, 2019)]),
          
    
    
    )
    