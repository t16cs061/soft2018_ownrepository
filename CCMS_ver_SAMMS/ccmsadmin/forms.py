from django import forms
from CCMS.models import EmployeeMaster, CarMaster

class EmployeeForm(forms.Form):
    id = forms.IntegerField(label='ID')