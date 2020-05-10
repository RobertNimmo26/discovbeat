# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from django.utils.translation import gettext_lazy as _
# from django.template.defaultfilters import slugify
# from django.utils import timezone
# from .managers import CustomUserManager

# # User Model
# class User(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(_("username"), max_length=50)
#     email = models.EmailField(_('email address'), unique=True)
#     name = models.CharField(_("name"), max_length=50)
#     party = models.ForeignKey(Party, on_delete=models.CASCADE)

#     #Required django User fields
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     #####

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email