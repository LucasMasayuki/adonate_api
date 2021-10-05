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
    path('tags/', views.TagList.as_view()),
    path('tags/<int:pk>', views.TagDetail.as_view()),
    path('auth', views.GetAuth.as_view()),
    path('get_campaigns_adonator', views.GetCampaignsOfAdonator.as_view()),
    path('save_campaign', views.SaveCampaignsOfAdonator.as_view()),
    path('filter_campaign', views.filterCampaign.as_view()),
]