from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):

    class Meta:
        db_table = 'user'
        verbose_name = u'User'
        verbose_name_plural = u'Users'

    id = models.AutoField(primary_key=True)
    users_galeries_id = models.IntegerField(models.ForeignKey('UserGalerie', on_delete=models.PROTECT), null=True, default=None)
    addresses_id = models.IntegerField(models.ForeignKey('Address', on_delete=models.PROTECT), null=True, default=None)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    cpf = models.CharField(max_length=200, null=True, default=None)
    cnpj = models.CharField(max_length=200, null=True, default=None)
    birth_date = models.DateField()
    created = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(User, self).save(*args, **kwargs)
        
class Donation(models.Model):

    class Meta:
        db_table = 'donation'
        verbose_name = u'Donation'
        verbose_name_plural = u'Donations'

    id = models.AutoField(primary_key=True)
    users_id = models.IntegerField(models.ForeignKey('User', on_delete=models.PROTECT), null=True, default=None)
    items_id = models.IntegerField(models.ForeignKey('Item', on_delete=models.PROTECT), null=True, default=None)
    created = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.id

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
    campaingns_id = models.IntegerField(models.ForeignKey('Campaign', on_delete=models.PROTECT), null=True, default=None)
    donations_id = models.IntegerField(models.ForeignKey('Donation', on_delete=models.PROTECT), null=True, default=None)
    created = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.id

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
    created = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.id

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
    items_galeries_id = models.IntegerField(models.ForeignKey('ItemGalery', on_delete=models.PROTECT), null=True, default=None)
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
    users_id = models.IntegerField(models.ForeignKey('User', on_delete=models.PROTECT), null=True, default=None)
    campaigns_id = models.IntegerField(models.ForeignKey('Campaign', on_delete=models.PROTECT), null=True, default=None)
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
    users_id = models.IntegerField(models.ForeignKey('User', on_delete=models.PROTECT), null=True, default=None)
    item_type_tag_id = models.IntegerField(models.ForeignKey('Tag', on_delete=models.PROTECT), null=True, default=None)
    purpose_tag_id = models.IntegerField(models.ForeignKey('Tag', on_delete=models.PROTECT), null=True, default=None)
    campaigns_galeries_id = models.IntegerField(models.ForeignKey('CampaignGalery', on_delete=models.PROTECT), null=True, default=None)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date_start = models.DateField()
    date_end = models.DateField()
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

class UserGalery(models.Model):

    class Meta:
        db_table = 'user_galery'
        verbose_name = u'UserGalery'
        verbose_name_plural = u'UsersGaleries'

    id = models.AutoField(primary_key=True)
    users_id = models.IntegerField(models.ForeignKey('User', on_delete=models.PROTECT), null=True, default=None)
    photos_id = models.IntegerField( models.ForeignKey('Photo', on_delete=models.PROTECT), null=True, default=None)
    created = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(UserGalery, self).save(*args, **kwargs)

class CampaignGalery(models.Model):

    class Meta:
        db_table = 'campaign_galery'
        verbose_name = u'CampaignGalery'
        verbose_name_plural = u'CampaignsGaleries'

    id = models.AutoField(primary_key=True)
    campaigns_id = models.IntegerField(models.ForeignKey('Campaign', on_delete=models.PROTECT), null=True, default=None)
    photos_id = models.IntegerField( models.ForeignKey('Photo', on_delete=models.PROTECT), null=True, default=None)
    created = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(CampaignGalery, self).save(*args, **kwargs)

class ItemGalery(models.Model):

    class Meta:
        db_table = 'item_galery'
        verbose_name = u'ItemGalery'
        verbose_name_plural = u'ItemsGaleries'

    id = models.AutoField(primary_key=True)
    items_id = models.IntegerField(models.ForeignKey('Item', on_delete=models.PROTECT), null=True, default=None)
    photos_id = models.IntegerField( models.ForeignKey('Photo', on_delete=models.PROTECT), null=True, default=None)
    created = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(ItemGalery, self).save(*args, **kwargs)

class Photo(models.Model):

    class Meta:
        db_table = 'photo'
        verbose_name = u'Photo'
        verbose_name_plural = u'Photos'

    id = models.AutoField(primary_key=True)
    photo = models.CharField(max_length=200)
    created = models.DateTimeField(editable=False, default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.photo

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Photo, self).save(*args, **kwargs)