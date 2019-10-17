from django.db import models

# Create your models here.

class Users(models.Model):

    class Meta:
        db_table = 'users'

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    cpf = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=200)
    birth_date = models.DateField()

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
        
class Donations(models.Model):

    class Meta:
        db_table = 'donations'

    id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    items_id = models.IntegerField()

    def __str__(self):
        return self.users_id

class DonationsCampaigns(models.Model):

    class Meta:
        db_table = 'donations_campaigns'

    id = models.AutoField(primary_key=True)
    campaingns_id = models.IntegerField()
    donations_id = models.IntegerField()

    def __str__(self):
        return self.campaingns_id

class Addresses(models.Model):

    class Meta:
        db_table = 'addresses'

    id = models.AutoField(primary_key=True)
    zipcode = models.IntegerField()
    street = models.CharField(max_length=200)
    number = models.IntegerField()
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.zipcode

class Items(models.Model):

    class Meta:
        db_table = 'items'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)
    photo = models.CharField(max_length=200)
    coments = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Reports(models.Model):

    class Meta:
        db_table = 'reports'

    id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    campaigns_id = models.IntegerField()
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Campaigns(models.Model):

    class Meta:
        db_table = 'campaigns'

    id = models.AutoField(primary_key=True)
    users_id = models.IntegerField()
    item_type_tag_id = models.IntegerField()
    purpose_tag_id = models.IntegerField()
    name = models.CharField(max_length=200)
    img_path = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return self.name

class Tags(models.Model):

    class Meta:
        db_table = 'tags'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)

    def __str__(self):
        return self.name