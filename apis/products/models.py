from django.db import models
from django.urls import reverse

# Create your models here.
from django.utils.text import slugify


class Product(models.Model):

    name = models.CharField(max_length=255)
    image = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self)->str:
        """
        Returns the name of the product.
        """
        return self.name
    @property
    def variants(self):
        return self.product_variants.all().count()
    
    def get_product_actions_url(self):
        return reverse("product_update", kwargs={
            "pk": self.pk
        })
    


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_variants")
    sku = models.CharField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=500, unique=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()


    def __str__(self)->str:
        """
        Returns the name of the product.
        """
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.sku)
        super().save(*args, **kwargs)
    