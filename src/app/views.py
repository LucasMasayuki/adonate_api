import requests
import base64
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.conf import settings

from .serializers import AdonatorSerializer, ItemSerializer, CampaignSerializer, DonationSerializer, ReportSerializer, AddressSerializer, TagSerializer
from .models import Adonator, Item, Campaign, Donation, Report, Address, Tag, TagCampaign, Photo, CampaignPhoto


class AdonatorList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Adonator.objects.all()
    serializer_class = AdonatorSerializer


class AdonatorDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Adonator.objects.all()
    serializer_class = AdonatorSerializer


class ItemList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class CampaignList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer


class CampaignDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer


class DonationList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer


class DonationDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer


class ReportList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class AddressList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class TagList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetail(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class GetAuth(APIView):
    def get(self, request):
        serializer = AdonatorSerializer(request.user)
        return Response({"adonator": serializer.data})


class GetCampaignsOfAdonator(APIView):
    def get(self, request):
        campaign = Campaign.objects.filter(adonator_id=request.user.id)
        serializer = CampaignSerializer(campaign, many=True)
        return Response(serializer.data)


class SaveCampaignsOfAdonator(APIView):
    def saveCampaign(self, campaignData):
        campaign = Campaign.objects.filter(pk=campaignData["id"]).first()
        campaign.name = campaignData["name"]
        campaign.start = campaignData["start"]
        campaign.end = campaignData["end"]
        campaign.description = campaignData["description"]
        campaign.save()

    def saveAddress(self, addressData, campaignId):
        address = Address.objects.filter(pk=campaignId).first()

        response = self.getLatLngFromGoogle(addressData)

        address.zipcode = addressData["zipcode"]
        address.number = addressData["number"]
        address.city = addressData["city"]
        address.state = addressData["state"]
        address.street = addressData["street"]
        address.lat = response[0]
        address.lng = response[1]
        address.save()

    def getLatLngFromGoogle(self, address):
        api_response = requests.get(
            'https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, settings.GOOGLE_MAPS_API_KEY))
        api_response_dict = api_response.json()
        lat = api_response_dict['results'][0]['geometry']['location']['lat']
        lng = api_response_dict['results'][0]['geometry']['location']['lng']
        return [lat, lng]

    def saveTags(self, tagsNames, campaignId):
        tagsList = Tag.objects.filter(name__in=tagsNames).all()
        tagCampaign = TagCampaign.objects.filter(campaign_id=campaignId).all()

        i = 0
        for tag_campaign in tagCampaign:
            tag_campaign.tag_id = tagsList[i].id
            tag_campaign.save()
            i += 1

    def savePhoto(self, photoData, campaignId):
        photoCampaign = CampaignPhoto.objects.filter(
            campaign_id=campaignId).first()

        if photoCampaign:
            photo = Photo.objects.filter(pk=photoCampaign.photo_id).first()
        else:
            photo = Photo.objects.create(photo="")
            CampaignPhoto.objects.create(
                campaign_id=campaignId, photo_id=photo.id)

        decodedImg = base64.decodestring(photoData["encoded_img"])
        photo.photo.save(photoData["img_name"], decodedImg)

    def post(self, request):
        print(request)
        print(request.data['campaign'])
        campaignData = request.POST.get["campaign"]
        addressData = request.POST.get["address"]
        tagsData = request.POST.get["tags"]
        photoData = request.POST.get["photo"]

        tagsName = [
            tagsData["purpouse"],
            tagsData["item_type"],
        ]

        self.saveCampaign(campaignData)
        self.saveAddress(addressData, campaignData["id"])
        self.saveTags(tagsName, campaignData["id"])

        if photoData:
            self.savePhoto(photoData, campaignData["id"])

        return Response(status=status.HTTP_200_OK)

    def put(self, request):
        campaignData = request.data["campaign"]
        addressData = request.data["address"]
        tagsData = request.data["tags"]
        photoData = request.data["photo"]

        response = self.getLatLngFromGoogle(addressData)

        address = Address.objects.create(
            zipcode=addressData["zipcode"],
            street=addressData["street"],
            number=addressData["number"],
            state=addressData["state"],
            lat=response[0],
            lng=response[1],
            city=addressData["city"]
        )

        campaign = Campaign.objects.create(
            address_id=address.id,
            adonator_id=request.user.id,
            name=campaignData["name"],
            description=campaignData["description"],
            start=campaignData["start"],
            end=campaignData["end"]
        )

        tagsName = [
            tagsData["purpouse"],
            tagsData["item_type"],
        ]

        tagsList = Tag.objects.filter(name__in=tagsName).all()

        i = 0
        for tag in tagsList:
            TagCampaign.objects.create(
                tag_id=tagsList[i].id,
                campaign_id=campaign.id
            )
            i += 1

        if photoData:
            decodedImg = base64.decodestring(photoData["encoded_img"])
            photo = Photo.objects.create()
            photo.photo.save(photoData["img_name"], decodedImg)
            CampaignPhoto.objects.create(
                photo_id=photo.id, campaign_id=campaign.id)

        return Response(status=status.HTTP_200_OK)


class filterCampaign(APIView):
    def get(self, request):
        campaignName = request.GET.get('campaign_name', None)
        porpouse = request.GET.get('purpouse', None)
        itemType = request.GET.get('item_type', None)

        tagsNames = []
        campaignsWithTagId = None

        if porpouse:
            tagsNames.append(porpouse)

        if itemType:
            tagsNames.append(itemType)

        if tagsNames.__len__ != 0:
            tagsId = Tag.objects.filter(name__in=tagsNames)
            campaignsWithTagId = TagCampaign.objects.filter(
                tag_id__in=tagsId).values_list('campaign_id', flat=True)

        if campaignsWithTagId:
            if campaignName:
                queryset = Campaign.objects.filter(
                    id__in=campaignsWithTagId, name__contains=campaignName)
            else:
                queryset = Campaign.objects.filter(id__in=campaignsWithTagId)
        elif campaignName:
            queryset = Campaign.objects.filter(name__contains=campaignName)
        else:
            queryset = Campaign.objects.all()

        serializer = CampaignSerializer(queryset, many=True)
        return Response({"campaigns": serializer.data})
