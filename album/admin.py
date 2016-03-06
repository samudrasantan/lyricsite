from django import forms
from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea

# Register your models here.
from album.models import Gitikar, Shilpi, Prokashok, Bandname, Albumname, Gaan, Catagory

class GaanForm(forms.ModelForm):
    lyric = forms.CharField(label = u'গান', widget=forms.Textarea(attrs={'rows': 20, 'cols': 100}))
    class Meta:
        model = Gaan
        fields = ['title','lyric', 'gitikar', 'shilpi', 'bandname','albumname', 'catagory']
class CatagoryForm(forms.ModelForm):
    short_description=forms.CharField(label=u'সংক্ষিপ্ত বিবরণ', widget=forms.Textarea(attrs={'rows': 20, 'cols': 100}), required=False)
    class Meta:
        model = Catagory
        fields = ['title','short_description']
        verbose_name = u'বিভাগ'
        verbose_name_plural = u'বিভাগ'
class GaanAdmin(admin.ModelAdmin):
    list_display =('title','lyric',)
    search_fields = ('title','lyric',)
    list_filter = ('gitikar','shilpi','bandname','albumname',)
    filter_horizontal = ('gitikar','shilpi','bandname','albumname',)
    raw_id_fields = ('gitikar',)
    form =GaanForm
class CatagoryAdmin(admin.ModelAdmin):
    form =CatagoryForm
    

admin.site.register(Gitikar)
admin.site.register(Shilpi)
admin.site.register(Bandname)
admin.site.register(Prokashok)
admin.site.register(Albumname)
admin.site.register(Catagory, CatagoryAdmin)
admin.site.register(Gaan, GaanAdmin)