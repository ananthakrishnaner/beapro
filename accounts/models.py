from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser,BaseUserManager
from django.contrib.auth.models import Group,Permission
# Create your models here.

# create a new user


class MyAccoutManager(BaseUserManager):

    def create_user(self,email,username,password=None,tutor=False,student=False):
        if not email:
            raise ValueError("Users must have  an email")
        if not username:
            raise ValueError("Users must have  an username")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.is_student = student
        user.is_tutor = tutor
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



def get_profile_image_filepath(self,filename):
    return f'profile_image/{self.pk}/{"profile_image.png"}'

def get_default_profile_image():
    return "default_img/pro_pic.gif" 

class Account(AbstractBaseUser):

    email           = models.EmailField(verbose_name='email',max_length=60,unique=True)
    username        = models.CharField(max_length=39,unique=True)
    first_name =   models.CharField(max_length=39,blank=True)
    last_name =    models.CharField(max_length=39,blank=True)
    date_joined    = models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_login     = models.DateTimeField(verbose_name="last login",auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    profile_image   = models.ImageField(upload_to=get_profile_image_filepath,null=True,blank=True,default=get_default_profile_image)
    is_student      = models.BooleanField(default=False)
    is_tutor     = models.BooleanField(default=False)

    objects=MyAccoutManager()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username']


    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="user_set",
        related_query_name="user",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name="user_set",
        related_query_name="user",
    )

    def __str__(self):
        return self.username

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_image/{self.pk}/'):]

    def  has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True

    def get_group_permissions(obj=None):
        return True

    def get_all_permissions(obj=None):
        return True
    


    