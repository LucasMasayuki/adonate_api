from rest_framework import serializers
from .models import User, Item, Campaign, Donation, Report, Address

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        
class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'

        
class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'

        
class CampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campaign
        fields = '__all__'

        
class DonationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Donation
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = '__all__'