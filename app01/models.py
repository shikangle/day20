from django.db import models

# Create your models here.
class Business(models.Model):
    caption = models.CharField(max_length=32)
    code = models.CharField(max_length=32)


class Host(models.Model):
    nid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32,db_index=True)# db_index  加上索引
    ip = models.GenericIPAddressField(db_index=True)
    port = models.IntegerField(max_length=32,null=True)
    b = models.ForeignKey("Business",to_field='id',on_delete=True)
