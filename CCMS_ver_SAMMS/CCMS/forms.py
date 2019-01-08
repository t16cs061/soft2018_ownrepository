from django import forms
from .models import Friend


        
class HelloForm(forms.Form):
    id = forms.IntegerField(label='ID')

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['car_name', 'start_day','end_day' ,'want_go']
        
    car_name = forms.TypedChoiceField(
        initial=1,
        coerce=lambda x: bool(int(x)),
        choices=(
            (1, u'サクシード'),
            (0, u'エブリイ'),
            (2, u'ソリオ'),
        ),
        widget=forms.RadioSelect,
    )
    
    start_day = forms.DateField(
        label = 'start_day',
        widget=forms.SelectDateWidget(years=[x for x in range(2018, 2050)]),
        )
    end_day = forms.DateField(
        label = 'end_day',
        widget=forms.SelectDateWidget(years=[x for x in range(2018, 2050)]),
    )
