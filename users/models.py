from django.db import models
from django.contrib.auth.models import User, BaseUserManager

from utils.models import TimestampZone

class CustomUserManager(BaseUserManager):
    def create_user(self, nickname, username, password, **extra_fields):
        if not nickname:
            raise ValueError(_("You must provide an nickname"))

        user = self.model(
            nickname=nickname,
            username=username,
            password=password,
            # phone=extra_fields.pop("phone", None),
            **extra_fields
        )
        user.set_password(password)
        user.save()

class CustomUser(TimestampZone):
    user = models.BigAutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    username = models.CharField(max_length=45)
    nickname = models.CharField(max_length=45, unique=True)
    bio = models.TextField(max_length=256)

    USERNAME_FIELD = "nickname"

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.username