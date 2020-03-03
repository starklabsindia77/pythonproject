from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models
from django.utils import timezone
from django.utils.timezone import now



# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, mobile, password=None, full_name=None, vehicle_type=None, is_active=True, customer=True, driver=False, is_staff=False, is_admin=False):
        if not mobile:
            raise ValueError("Users must have an mobile address")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(
            mobile = mobile,
            full_name=full_name,
            vehicle_type=vehicle_type
        )
        user_obj.set_password(password) # change user password
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.is_active = is_active
        user_obj.customer = customer
        user_obj.driver = driver
        user_obj.save(using=self._db)
        return user_obj

    def create_driver(self, mobile, password=None, full_name=None, vehicle_type=None):
        user = self.create_user(
                mobile,
                full_name=full_name,
                vehicle_type=vehicle_type,
                password=password,
                customer=False,
                driver=True
        )
        return user

    def create_staffuser(self, mobile,password=None, full_name=None):
        user = self.create_user(
                mobile,
                full_name=full_name,
                password=password,
                is_staff=True,
                customer= False
        )
        return user
    

    def create_superuser(self, mobile, password=None, full_name=None):
        user = self.create_user(
                mobile,
                full_name=full_name,
                password=password,
                is_staff=True,
                is_admin=True,
                customer= False
        )
        return user


class User(AbstractBaseUser):
    objects = UserManager()
    
    mobile      = models.CharField(max_length=255, unique=True, default='none')
    full_name   = models.CharField(max_length=255, blank=True, null=True)
    vehicle_type   = models.CharField(max_length=255, blank=True, null=True)
    is_active   = models.BooleanField(default=True) # can login 
    customer    = models.BooleanField(default=True) # can login
    driver      = models.BooleanField(default=False) # can login 
    staff       = models.BooleanField(default=False) # staff user non superuser
    admin       = models.BooleanField(default=False) # superuser 
    timestamp   = models.DateTimeField(auto_now_add=True)
    # confirm     = models.BooleanField(default=False)
    # confirmed_date     = models.DateTimeField(default=False)

    USERNAME_FIELD = 'mobile' #username
    # USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = [] #['full_name'] #python manage.py createsuperuser

    def __str__(self):
        return self.mobile

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.mobile

    def get_short_name(self):
        return self.mobile

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        if self.is_admin:
            return True
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    # @property
    # def is_active(self):
    #     return self.active

