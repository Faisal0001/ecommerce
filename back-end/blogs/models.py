from django.db import models
from django.utils.text import slugify
from accounts.models import User
from django.db.models.signals import pre_save
from django.shortcuts import reverse

STATUS_CHOICES = (
    ('draft','draft'),
    ('publish','publish'),
)




class Blog(models.Model):
	title =	models.CharField(max_length=200)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	created_on = models.DateTimeField(auto_now_add=True)
	content = models.TextField()
	status = models.CharField(max_length= 20,choices=STATUS_CHOICES, default='draft')
	slug = models.SlugField(default='abc', unique=True)
	updated_on = models.DateTimeField(auto_now= True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("blog-detail", kwargs={"slug": self.slug})

def unique_slug_generator(instance):
    constant_slug = slugify(instance.title)
    slug = constant_slug
    num = 0
    Klass = instance.__class__
    while Klass.objects.filter(slug=slug).exists():
        num += 1
        slug = "{slug}-{num}".format(slug=constant_slug, num=num)
    return slug


def pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug or instance.title != Blog.objects.filter(slug=instance.slug):
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_reciever, sender=Blog)

