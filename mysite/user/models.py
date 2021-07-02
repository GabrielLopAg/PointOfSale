from django.contrib.auth.models import AbstractUser
from django.db import models

import mysite.settings as setting

class User(AbstractUser):
    image = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)

    def get_image(self):
        if self.image:
            return '{}{}'.format(setting.MEDIA_URL, self.image)
        return '{}{}'.format(setting.STATIC_URL, 'img/empty.png')
