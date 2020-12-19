from django.db import models
from django.contrib.auth.models import (AbstractUser, BaseUserManager, AbstractBaseUser)



class UserManager(BaseUserManager):
	def create_user(self, email, username=None, password=None):
		if not email:
			return ValueError('Users must have a email address')
		if not username:
			return ValueError('Users must have a username')
		if not password:
			return ValueError('Users must have a password')
		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)
		user.set_password(password)
		user.save(using=self.db)
		return user

	def create_superuser(self, email, username=None, password=None):
		user = self.create_user(email, username, password)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self.db)
		return user



class User(AbstractUser):
	email = models.CharField(max_length=255, unique=True)
	username = models.CharField(max_length=20)
	date_joined = models.DateTimeField(auto_now_add=True)
	last_login = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)

	objects = UserManager()
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username',]

	def __str__(self):
		return self.email

	def __unicode__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True
