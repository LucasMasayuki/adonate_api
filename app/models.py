from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from .enums import TagType

# Create your models here.

class Adonator(AbstractUser):
    class Meta:
        db_table = 'adonator'
        verbose_name = u'Adonator'
        verbose_name_plural = u'Adonators'

    address = models.ForeignKey('Address', on_delete=models.PROTECT, null=True)
    cpf = models.CharField(max_length=200, null=True, default=None)
    cnpj = models.CharField(max_length=200, null=True, default=None)
    birth_date = models.DateField(null=True, default=None)

    def __str__(self):
        return self.email
        
class Donation(models.Model):

    class Meta:
        db_table = 'donation'
        verbose_name = u'Donation'
        verbose_name_plural = u'Donations'

    id = models.AutoField(primary_key=True)
    adonator = models.ForeignKey('Adonator', on_delete=models.PROTECT)
    item = models.ForeignKey('Item', on_delete=models.PROTECT)
    created = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Donation, self).save(*args, **kwargs)

class DonationCampaign(models.Model):

    class Meta:
        db_table = 'donation_campaign'
        verbose_name = u'DonationCampaign'
        verbose_name_plural = u'DonationsCampaigns'

    id = models.AutoField(primary_key=True)
    campaingn = models.ForeignKey('Campaign', on_delete=models.PROTECT)
    donation = models.ForeignKey('Donation', on_delete=models.PROTECT)
    created = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(DonationCampaign, self).save(*args, **kwargs)

class Address(models.Model):

    class Meta:
        db_table = 'address'
        verbose_name = u'Address'
        verbose_name_plural = u'Addresses'

    id = models.AutoField(primary_key=True)
    zipcode = models.IntegerField(blank=True, null=True, default=None)
    street = models.CharField(max_length=200)
    number = models.IntegerField(blank=True, null=True, default=None)
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    lat = models.CharField(max_length=200)
    lng = models.CharField(max_length=200)
    created = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Address, self).save(*args, **kwargs)

class Item(models.Model):

    class Meta:
        db_table = 'item'
        verbose_name = u'Item'
        verbose_name_plural = u'Items'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default='')
    amount = models.IntegerField(default=0, null=False)
    coments = models.CharField(max_length=200)
    created = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Item, self).save(*args, **kwargs)

class Report(models.Model):

    class Meta:
        db_table = 'report'
        verbose_name = u'Report'
        verbose_name_plural = u'Reports'

    id = models.AutoField(primary_key=True)
    adonator = models.ForeignKey('Adonator', on_delete=models.PROTECT)
    campaign = models.ForeignKey('Campaign', on_delete=models.PROTECT)
    text = models.CharField(max_length=200)
    created = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Report, self).save(*args, **kwargs)

class Campaign(models.Model):

    class Meta:
        db_table = 'campaign'
        verbose_name = u'Campaign'
        verbose_name_plural = u'Campaigns'

    id = models.AutoField(primary_key=True)
    adonator = models.ForeignKey('Adonator', on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    start = models.DateField()
    end = models.DateField()
    created = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Campaign, self).save(*args, **kwargs)

class Tag(models.Model):

    class Meta:
        db_table = 'tag'
        verbose_name = u'Tag'
        verbose_name_plural = u'Tags'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    tag_type = models.CharField(max_length=255, choices=TagType.choices())
    created = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Tag, self).save(*args, **kwargs)

class TagCampaign(models.Model):

    class Meta:
        db_table = 'tag_campaign'
        verbose_name = u'TagCampaign'
        verbose_name_plural = u'TagCampaigns'

    id = models.AutoField(primary_key=True)
    campaign = models.ForeignKey(Campaign, related_name='tag_campaign', on_delete=models.PROTECT)
    tag = models.ForeignKey(Tag, related_name='tag', on_delete=models.PROTECT)
    created = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(TagCampaign, self).save(*args, **kwargs)

class CampaignPhoto(models.Model):

    class Meta:
        db_table = 'campaign_photo'
        verbose_name = u'CampaignPhoto'
        verbose_name_plural = u'CampaignPhotos'

    id = models.AutoField(primary_key=True)
    campaign = models.ForeignKey('Campaign', related_name='camapaign_photo', on_delete=models.PROTECT)
    photo = models.ForeignKey('Photo', related_name='photo_campaign', on_delete=models.PROTECT)
    created = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(CampaignPhoto, self).save(*args, **kwargs)

class AdonatorPhoto(models.Model):

    class Meta:
        db_table = 'adonator_photo'
        verbose_name = u'AdonatorPhoto'
        verbose_name_plural = u'AdonatorPhotos'

    id = models.AutoField(primary_key=True)
    adonator = models.ForeignKey('Adonator', related_name='adonator_photo', on_delete=models.PROTECT)
    photo = models.ForeignKey('Photo', related_name='photo_adonator', on_delete=models.PROTECT)
    created = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(AdonatorPhoto , self).save(*args, **kwargs)


class ItemPhoto(models.Model):

    class Meta:
        db_table = 'item_photo'
        verbose_name = u'ItemPhoto'
        verbose_name_plural = u'ItemPhotos'

    id = models.AutoField(primary_key=True)
    item = models.ForeignKey('Item', related_name='item_photo', on_delete=models.PROTECT)
    photo = models.ForeignKey('Photo', related_name='photo_item', on_delete=models.PROTECT)
    created = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(ItemPhoto, self).save(*args, **kwargs)

class Photo(models.Model):

    class Meta:
        db_table = 'photo'
        verbose_name = u'Photo'
        verbose_name_plural = u'Photos'

    id = models.AutoField(primary_key=True)
    photo = models.FileField(upload_to='photo')
    created = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Photo, self).save(*args, **kwargs)