from django.db import models

# Create your models here.
class FacedetectUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    email = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    password = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faceDetect_user'

