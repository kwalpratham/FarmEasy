from django.db import models

# Create your models here.
class landModel(models. Model):   
    post_id = models.AutoField(primary_key= True)
    ownerName = models.CharField(max_length=50)
    irrigationSource = models.CharField(max_length=500, default="")
    climateCond = models.CharField(max_length=500, default="")
    cropHistory = models.CharField(max_length=5000, default="")
    address = models.CharField(max_length=5000, default="")
    landSize = models.CharField(max_length=500, default="")
    soilType = models.CharField(max_length=5000, default="")
    pub_date = models.DateField() # may need correction
    thumbnail = models.ImageField(upload_to='images/', default="")

    # def __str__(self):
    #     return self.post_id   

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name