from django.db import models
import uuid

class baseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateField(auto_created=True)
    update_at = models.DateField(auto_created=True)

    class Meta:
        abstract = True


class product(baseModel):
    product_name = models.CharField(max_length=100)
    product_slug = models.SlugField(unique=True)
    product_desc = models.TextField()
    product_price = models.IntegerField(default=0)
    product_demo_price = models.IntegerField(default=0)
    product_quantity = models.CharField(null=True)


class productMetaInformation(baseModel):
    product = models.OneToOneField(product,on_delete=models.CASCADE)
 
    
class productImages(baseModel):
    product_images = models.ImageField(upload_to='products')
    

# Create your models here.
