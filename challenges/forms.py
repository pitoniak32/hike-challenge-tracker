from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django import forms

class AchievementForm(forms.Form):
	date_done = forms.DateTimeField(widget=DateTimePickerInput(format="%m/%d/%Y"), required=False)
