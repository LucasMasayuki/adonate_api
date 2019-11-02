from rest_framework import serializers
from . import models

class AdonatorSerializer(serializers.ModelSerializer):
    adonator_galery = serializers.PrimaryKeyRelatedField(many=False, read_only=True, allow_null=True)
    address = serializers.PrimaryKeyRelatedField(many=False, read_only=True, allow_null=True)

    class Meta:
        model = models.Adonator
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    item_galery = serializers.PrimaryKeyRelatedField(many=False, read_only=True, allow_null=True)

    class Meta:
        model = models.Item
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Address
        fields = '__all__'

class CampaignSerializer(serializers.ModelSerializer):
    campaign_galery = serializers.PrimaryKeyRelatedField(many=False, read_only=True, allow_null=True)

    class Meta:
        model = models.Campaign
        fields = '__all__'

class DonationSerializer(serializers.ModelSerializer):
    adonator = serializers.PrimaryKeyRelatedField(many=False, read_only=True, allow_null=True)
    item = serializers.PrimaryKeyRelatedField(many=True, read_only=True, allow_null=True)

    class Meta:
        model = models.Donation
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    adonator = serializers.PrimaryKeyRelatedField(many=False, read_only=True, allow_null=True)

    class Meta:
        model = models.Report
        fields = '__all__'