from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view(), name='users-list'),
    url(r'^items/$', views.ItemList.as_view(), name='items-list'),
    url(r'^campaigns/$', views.CampaignList.as_view(), name='campaigns-list'),
    url(r'^reports/$', views.ReportList.as_view(), name='reports-list'),
    url(r'^adresses/$', views.AddressList.as_view(), name='addresses-list'),
    url(r'^donations/$', views.DonationList.as_view(), name='donations-list'),
]