from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from orm.models import Account,Account_Risk
from orm.form import Account_RiskForm
# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'

# class AccountlistView(ListView):
#     model = Account
#     def get_queryset(self):
#         account = Account.objects.filter(account_id=3).count()
#         return account


def list(request):
    # if request.method == 'POST':
    #     form = Account_RiskForm(request.POST)
    #     if form.is_valid():
    #         aid = form.cleaned_data.get('account_id')
            account = Account.objects.filter(account_id=2).count()
            stg = Account.objects.filter(account_id=2,stage='Won').count()
            poten = Account.objects.filter(account_id=2,potential='HP').count()
            pipe = Account.objects.filter(account_id=2,pipeline='HP').count()
            risk = Account_Risk.objects.filter(account_id=2)
            date_dict = {'insert_me':account,'stg':stg,'poten':poten,'pipe':pipe,'risk':risk}
            return render(request,'orm/account_list.html',context=date_dict)

# def nameList(request):
#     name = Account.objects.filter(stage='Won').count()
#     name_dict = {'name':name}
#     return render(request,'orm/account_list.html',context=name_dict)
