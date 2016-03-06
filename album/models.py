#pfrom __future__ import unicode_literals
from django.db import models


# Create your models here.
class Gitikar(models.Model):
    title = models.CharField(max_length=100, verbose_name = u'নাম')
    biography = models.CharField(max_length=1000, blank=True, null=True, verbose_name = u'বিবরন')
    
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'গীতিকার'
        verbose_name_plural = u'গীতিকারগণ'

class Prokashok(models.Model):
    title = models.CharField(max_length=150, verbose_name = u'নাম')
    short_description = models.CharField(max_length=1000, blank=True, null=True, verbose_name = u'বিবরন')
    class Meta:
        verbose_name = u'প্রকাশক'
        verbose_name_plural = u'প্রকাশকবৃন্দ'

    def __unicode__(self):
            return self.title

class Shilpi(models.Model):
    title = models.CharField(max_length=100, verbose_name = u'নাম')
    biography = models.CharField(max_length=1000, blank=True, null=True, verbose_name = u'বিবরন')
   
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'শিল্পী'
        verbose_name_plural = u'শিল্পীবৃন্দ'

class Bandname(models.Model):
    title = models.CharField(max_length=100, verbose_name = u'নাম')
    short_history = models.CharField(max_length=1000, blank=True, null=True, verbose_name = u'বিবরন')
    shilpi = models.ManyToManyField(Shilpi)
    class Meta:
        verbose_name = u'ব্যান্ড'
        verbose_name_plural = u'ব্যান্ডদল'

    def __unicode__(self):
        return self.title

class Albumname(models.Model):
    title = models.CharField(max_length=100, verbose_name = u'নাম')
    album_text = models.CharField(max_length=1000, blank=True, null=True, verbose_name = u'বিবরন')
    album_no = models.IntegerField(blank=True, null=True, verbose_name = u'এলবাম নাম্বার')
    lineup = models.ManyToManyField(Shilpi)
    prokashok = models.ManyToManyField(Prokashok)
    class Meta:
        verbose_name = u'এলবাম'
        verbose_name_plural = u'এলবামগুলো'

    def __unicode__(self):
        return self.title
    
    def first_letter(self):
        return self.title and self.tilte[0] or ''

class Catagory(models.Model):
    title = models.CharField(max_length=500, verbose_name = u'বিভাগ')
    short_description = models.CharField(max_length=1000, blank=True, null=True, verbose_name = u'বিবরন')
    class Meta:
        verbose_name = u'শ্রেণীবিভাগ'
        verbose_name_plural = u'বিভাগ সমূহ'
    
    def __unicode__(self):
        return self.title

class Gaan(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'শিরোনাম')
    lyric = models.CharField(max_length=5000, blank=True, null=True, verbose_name=u'গান')
    gitikar = models.ManyToManyField(Gitikar, blank=True, null=True, verbose_name=u'গীতিকার')
    shilpi = models.ManyToManyField(Shilpi, blank=True, null=True, verbose_name=u'শিল্পী')
    bandname = models.ManyToManyField(Bandname, blank=True, null=True, verbose_name=u'ব্যান্ড')
    albumname = models.ManyToManyField(Albumname, blank=True, null=True,verbose_name=u'এলবাম')
    catagory = models.ManyToManyField(Catagory, blank=True, null=True,verbose_name=u'শ্রেণিবিভাগ')
    class Meta:
        verbose_name = u'গান'
        verbose_name_plural = u'গানগুলো'

    def __unicode__(self):
        return self.title


