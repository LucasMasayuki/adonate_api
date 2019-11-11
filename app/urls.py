from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('adonator/', views.AdonatorList.as_view()),
    path('adonator/<int:pk>', views.AdonatorDetail.as_view()),
    path('items/', views.ItemList.as_view()),
    path('items/<int:pk>', views.ItemDetail.as_view()),
    path('campaigns/', views.CampaignList.as_view()),
    path('campaigns/<int:pk>', views.CampaignDetail.as_view()),
    path('reports/', views.ReportList.as_view()),
    path('reports/<int:pk>', views.ReportDetail.as_view()),
    path('adresses/', views.AddressList.as_view()),
    path('adresses/<int:pk>', views.AddressDetail.as_view()),
    path('donations/', views.DonationList.as_view()),
    path('donations/<int:pk>', views.DonationDetail.as_view()),
]