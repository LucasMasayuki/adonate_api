from rest_framework import generics
from .models import User, Item, Campaign, Donation, Report, Address
from .serializers import UserSerializer, ItemSerializer, CampaignSerializer, DonationSerializer, ReportSerializer, AddressSerializer

# Create your views here.
class UserList(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class ItemList(generics.ListCreateAPIView):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CampaignList(generics.ListCreateAPIView):

    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class DonationList(generics.ListCreateAPIView):

    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

class ReportList(generics.ListCreateAPIView):

    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class AddressList(generics.ListCreateAPIView):

    queryset = Address.objects.all()
    serializer_class = AddressSerializer