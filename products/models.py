import products
from django.db import models
from accounts.models import User
from django.shortcuts import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save

CATEGORY_CHOICES = (
	('technology', 'technology'),
	('furniture', 'furniture'),
	('sports', 'sports'),
	('clothes', 'clothes'),
	('kitchen', 'kitchen'),
	('food', 'food'),
)



class Product(models.Model):
	name = models.CharField(max_length=100)
	price = models.FloatField()
	discount_price = models.FloatField(blank=True, null=True)
	image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None)
	category  = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
	description = models.TextField(blank=True, null=True)
	slug = models.SlugField(blank=True, null=True)

	def  __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("post-detail", kwargs={"slug": self.slug})


def unique_slug_generator(instance):
    constant_slug = slugify(instance.header)
    slug = constant_slug
    num = 0
    Klass = instance.__class__
    while Klass.objects.filter(slug=slug).exists():
        num += 1
        slug = "{slug}-{num}".format(slug=constant_slug, num=num)
    return slug

def pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug or instance.header != Product.objects.filter(slug=instance.slug):
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_reciever, sender=Product)


class OrderProduct(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	ordered = models.BooleanField(default=False)


	def __str__(self):
		return self.product.name


class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	products = models.ManyToManyField(OrderProduct)
	start_date = models.DateTimeField(auto_now_add=True)
	ordered_date = models.DateTimeField()
	ordered = models.BooleanField(default=False)


	def __str__(self):
		return self.user.email

	def get_products(self):
		return "\n".join([p.product.name for p in self.products.all()])

class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart")
	products = models.ManyToManyField(Product)

	def __str__(self):
		return self.user.username

