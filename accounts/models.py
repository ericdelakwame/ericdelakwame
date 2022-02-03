from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.gis.db.models import PointField
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)
    activated = models.BooleanField(default=False)
    tel_no = PhoneNumberField(blank=True, null=True)
    location = PointField(null=True)
    photo = models.ImageField(
        upload_to='users/%Y/%m/%d', null=True, blank=True)
    connected_users = models.ManyToManyField('self', related_name='network')
    country = models.CharField(max_length=100, default='')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('accounts:user_detail', kwargs={'user_pk': self.pk})

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Admin(User):
    pass

    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admin'

    def __str__(self):
        return '{}: Admin'.format(self.get_full_name())
