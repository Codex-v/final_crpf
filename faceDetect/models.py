from django.db import models
from django import  forms

# Create your models here.


class FacedetectCriminal(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    aadhar_no = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    address = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    picture = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    status = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'faceDetect_criminal'


class FacedetectCriminallastspotted(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    aadhar_no = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    address = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    picture = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    status = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    latitude = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    longitude = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'faceDetect_criminallastspotted'


class FacedetectFile(models.Model):
    id = models.BigAutoField(primary_key=True)
    file = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    remark = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'faceDetect_file'

class imageView(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')


class Imagetable(models.Model):
    imageid = models.AutoField(db_column='ImageID', primary_key=True)  # Field name made lowercase.
    imagedata = models.BinaryField(db_column='ImageData', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ImageTable'
