from django.conf.urls import url
from orm import views

urlpatterns = [
        # url(r'^$',views.AccountlistView.as_view(),name='account_list'),
        url(r'^$',views.list,name='account_list'),
        # url(r'^$',views.nameList,name='account_list'),
        url(r'^about/$',views.AboutView.as_view(),name='about'),
    ]
