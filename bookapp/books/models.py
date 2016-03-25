# models.py
from django.core.urlresolvers import reverse
from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)

    class Meta:
        ordering = ["-name"]

    def get_absolute_url(self):
        return reverse('publisher-detail', kwargs={'pk': self.pk})

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author', related_name='books',
            blank=True)
    publisher = models.ForeignKey(Publisher, blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.title
