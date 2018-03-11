from django import forms
from orm.models import Account_Risk
class Account_RiskForm(forms.ModelForm):
    class Meta:
        model = Account_Risk
        fields = ('account_id',)
