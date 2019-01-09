from django import forms
from .models import Friend, MentenanceMaster


        
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

#車両メンテナンス予定追加用フォーム
class MentenanceForm(forms.ModelForm):
    class Meta:
        model = MentenanceMaster
        fields = ['CarName', 'StartDayTime','EndDayTime' ,'MentenanceOverview']
        
    CarName = forms.TypedChoiceField(
        label = '車両名',
        initial=1,
        coerce=lambda x: bool(int(x)),
        choices=(
            (0, u'サクシード'),
            (1, u'エブリイ'),
            (2, u'ソリオ'),
        ),
        widget=forms.RadioSelect,
    )
    
    StartDayTime = forms.DateField(
        label = 'メンテナンス開始日時',
        widget=forms.SelectDateWidget(years=[x for x in range(2018, 2050)]),
        )
    EndDayTime = forms.DateField(
        label = 'メンテナンス終了日時',
        widget=forms.SelectDateWidget(years=[x for x in range(2018, 2050)]),
    )
    MentenanceOverview = forms.CharField(
        label = 'メンテナンス概要',
        max_length=200,
        widget=forms.TextInput(attrs={
            'placeholder': 'メンテナンス概要を入力',
            }
            )
    )