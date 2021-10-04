from django.contrib.auth.models import AbstractUser, User
from django.db import models


class UserProfile(models.Model):
    CURRENCY_CHOICES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)
    base_currency = models.CharField(
        max_length=20,
        choices=CURRENCY_CHOICES,
        default='1'
    )
    source_label = models.CharField(max_length=20, blank=True)

    def save(self, *args, **kwargs):
        self.id = self.user_id
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username}   |   id = {self.id}'
