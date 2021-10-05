from django.contrib import admin

from .models import Adonator
from .models import Campaign
from .models import Item
from .models import Donation
from .models import DonationCampaign
from .models import Address
from .models import Photo
from .models import Report
from .models import Tag
from .models import ItemPhoto
from .models import CampaignPhoto
from .models import AdonatorPhoto
from .models import TagCampaign
from django.contrib.auth.admin import UserAdmin

from .forms import AdonatorCreationForm, AdonatorChangeForm

class AdonatorAdmin(UserAdmin):
    add_form = AdonatorCreationForm
    form = AdonatorChangeForm
    model = Adonator
    list_display = ['email', 'username', 'name']

admin.site.register(Adonator)
admin.site.register(Campaign)
admin.site.register(Item)
admin.site.register(DonationCampaign)
admin.site.register(Donation)
admin.site.register(Address)
admin.site.register(Report)
admin.site.register(Tag)
admin.site.register(Photo)
admin.site.register(CampaignPhoto)
admin.site.register(AdonatorPhoto)
admin.site.register(ItemPhoto)
admin.site.register(TagCampaign)