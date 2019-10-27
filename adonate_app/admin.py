from django.contrib import admin

from .models import User
from .models import Campaign
from .models import Item
from .models import ItemGalery
from .models import UserGalery
from .models import Donation
from .models import DonationCampaign
from .models import Address
from .models import Photo
from .models import Report
from .models import CampaignGalery
from .models import Tag

admin.site.register(User)
admin.site.register(Campaign)
admin.site.register(ItemGalery)
admin.site.register(Item)
admin.site.register(UserGalery)
admin.site.register(DonationCampaign)
admin.site.register(Donation)
admin.site.register(Address)
admin.site.register(Report)
admin.site.register(Photo)
admin.site.register(CampaignGalery)
admin.site.register(Tag)