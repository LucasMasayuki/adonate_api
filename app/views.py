from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import AdonatorSerializer, ItemSerializer, CampaignSerializer, DonationSerializer, ReportSerializer, AddressSerializer
from .models import Adonator, Item, Campaign, Donation, Report, Address
from django.http import Http404    

class AdonatorList(generics.ListAPIView):
    permission_classes = (IsAuthenticated)
    queryset = Adonator.objects.all()
    serializer_class = AdonatorSerializer

class AdonatorDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated)
    queryset = Adonator.objects.all()
    serializer_class = AdonatorSerializer

class ItemList(generics.ListAPIView):
    permission_classes = (IsAuthenticated)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CampaignList(generics.ListAPIView):
    permission_classes = (IsAuthenticated)
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class CampaignDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated)
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class DonationList(generics.ListAPIView):
    permission_classes = (IsAuthenticated)
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

class DonationDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated)
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

class ReportList(generics.ListAPIView):
    permission_classes = (IsAuthenticated)
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ReportDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated)
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class AddressList(generics.ListAPIView):
    permission_classes = (IsAuthenticated)
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class AddressDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated)
    queryset = Address.objects.all()
    serializer_class = AddressSerializer