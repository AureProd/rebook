from django.contrib.auth.models import AbstractUser
from django.db.models import DateField


class UserProfile(AbstractUser):
    birth_date = DateField(null=True, blank=True)

    def __str__(self):
        return self.username
