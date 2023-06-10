from django.db import models
from django.utils.translation import gettext_lazy as _


class JobsModel(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    image = models.ImageField(upload_to='jobs', verbose_name=_('title'))