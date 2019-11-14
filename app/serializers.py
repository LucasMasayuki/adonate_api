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
    address = AddressSerializer(many=False)
    class Meta:
        model = models.Adonator
        fields = ['address', 'cpf', 'cnpj', 'birth_date', 'username']

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tag
        fields = ['name', 'color', 'tag_type']

class TagCampaignSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=False)

    class Meta:
        model = models.TagCampaign
        fields = ['tag']

class CampaignPhotoSerializer(serializers.ModelSerializer):
    photo_campaign = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = models.CampaignPhoto
        fields = ['photo_campaign']

class CampaignSerializer(serializers.ModelSerializer):
    adonator = AdonatorSerializer(many=False)
    tag_campaign = TagCampaignSerializer(many=True, read_only=True)
    camapaign_photo = CampaignPhotoSerializer(many=True, read_only=True, allow_null=True)

    class Meta:
        model = models.Campaign
        fields = ['adonator', 'tag_campaign', 'name', 'description', 'start', 'end', 'camapaign_photo']

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