from django.db import models
from django.utils.translation import gettext_lazy as _


class ContestsModel(models.Model):
    image = models.ImageField(upload_to='contest', verbose_name=_('image'))
    title = models.CharField(max_length=100, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'))
