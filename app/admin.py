from django.contrib import admin

from .models import Adonator
from .models import Campaign
from .models import Item
from .models import ItemGalery
from .models import AdonatorGalery
from .models import Donation
from .models import DonationCampaign
from .models import Address
from .models import Photo
from .models import Report
from .models import CampaignGalery
from .models import Tag
from django.contrib.auth.admin import UserAdmin

from .forms import AdonatorCreationForm, AdonatorChangeForm

class AdonatorAdmin(UserAdmin):
    add_form = AdonatorCreationForm
    form = AdonatorChangeForm
    model = Adonator
    list_display = ['email', 'username', 'name']

admin.site.register(Adonator)
admin.site.register(Campaign)
admin.site.register(ItemGalery)
admin.site.register(Item)
admin.site.register(AdonatorGalery)
admin.site.register(DonationCampaign)
admin.site.register(Donation)
admin.site.register(Address)
admin.site.register(Report)
admin.site.register(Photo)
admin.site.register(CampaignGalery)
admin.site.register(Tag)