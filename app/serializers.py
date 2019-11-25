from rest_framework import serializers
from rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer
from . import models

class LoginSerializer(RestAuthLoginSerializer):
    username = None

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Item
        fields = ['name', 'amount', 'coments', 'created', 'modified']

class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Photo
        fields = ['photo']

class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Address
        fields = ['zipcode', 'street', 'number', 'state', 'city', 'lat', 'lng']

class AdonatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Adonator
        fields = ['id', 'username', 'email', 'cpf', 'cnpj', 'birth_date']

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tag
        fields = ['id', 'name', 'color', 'tag_type']

class TagCampaignSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=False)

    class Meta:
        model = models.TagCampaign
        fields = ['tag']

class CampaignPhotoSerializer(serializers.ModelSerializer):
    photo = PhotoSerializer(many=False, read_only=True)

    class Meta:
        model = models.CampaignPhoto
        fields = ['photo']

class CampaignSerializer(serializers.ModelSerializer):
    adonator = AdonatorSerializer(many=False)
    address = AddressSerializer(many=False, read_only=True)
    tag_campaign = TagCampaignSerializer(many=True, read_only=True)
    camapaign_photo = CampaignPhotoSerializer(many=True, read_only=True, allow_null=True)

    class Meta:
        model = models.Campaign
        fields = ['adonator', 'tag_campaign', 'camapaign_photo', 'address', 'id', 'name', 'description', 'start', 'end']

class DonationSerializer(serializers.ModelSerializer):
    adonator = AdonatorSerializer(many=False)
    item = ItemSerializer(many=False)

    class Meta:
        model = models.Donation
        fields = ['adonator', 'item']

class ReportSerializer(serializers.ModelSerializer):
    adonator = AdonatorSerializer(many=False, allow_null=True)
    campaign = CampaignSerializer(many=False, allow_null=True)

    class Meta:
        model = models.Report
        fields = ['adonator', 'campaign', 'text']