# Author Kjærsti L. Bergli, email: klb022@uit.no
# A lot of this functionality is derived from https://codingwithmitch.com/

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from cryptography.fernet import Fernet #Used for password encryption

# Functions used to override the account cration process 
# Creating user and superuser with all necessary fields in database. Superuser has all admin rights.
class MyUserManager(BaseUserManager):
	def create_user(self, email, password, username, role, phone):
		if not email:
			raise ValueError('Alle brukere må ha en epostadresse')

        # Important to use 'normalize_email' here to make shure the email adress is only lower case letters
		user = self.model(
			username = username,
            email = self.normalize_email(email),
            password = password,
            role = role,
            phone = phone,
		)
        
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, email,  password, role, phone):
		user = self.create_user(
            username = username,
			email = self.normalize_email(email),
			password = password,
            role = role,
            phone = phone,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


# Custom user model inheriting from Django's user class
class User(AbstractBaseUser):
    class Roles(models.IntegerChoices):
      CUSTOMER = 1, "Kunde"
      HAIRDRESSER = 2, "Frisør"
      ADMIN = 3, "Administrator"
    email = models.EmailField(verbose_name="E-post", max_length=100, unique=True)
    username = models.CharField(verbose_name="Brukernavn", max_length=30, unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(verbose_name="Navn", max_length=100, null=True)
    role = models.PositiveSmallIntegerField(verbose_name="Rolle", choices= Roles.choices, default= Roles.CUSTOMER)
    # This field is only meant for hairdressers to have a description showing on the webpage. 
    about = models.TextField(verbose_name="Om meg", blank=True)
    # This field could also have a minimum length of 8 numbers. Future work dicovered while testing.
    phone = models.CharField(verbose_name="Telefon", max_length=13, null=True)
    # The 4 boolean values starting with 'is_' have to be modified to extend the user model 'AbstractBaseuser'
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    #Sets the login to be email rather than username. But also requiered fields for password, role, phone
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password', 'role', 'phone']

    # Ties the account to the custom user manager
    objects = MyUserManager()
    
    # Default return value from the object if no paricular field is accessed
    def __str__(self):
        return self.email
    
    # Password encryption
    def encryptPassword(self, password):
        key = Fernet.generate_key()
        fernet = Fernet(key)
        encrypted_pass = fernet.encrypt(password.encode())
        return encrypted_pass

    # The following functions has to be defined to use AbstractBaseUser
    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # All users have permission to view this app
    def has_module_perms(self, app_label):
        return True