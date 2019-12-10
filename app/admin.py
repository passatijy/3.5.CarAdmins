from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm

from django import forms

from ckeditor.widgets import CKEditorWidget

class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'review_count' )
    list_filter = ('brand', 'model', )
    search_fields = ('model',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('carview', 'title',)
    list_filter = ('title',)
    search_fields = ('title',)
    ordering = ('-id',)
    form = ReviewAdminForm
    def carview(self, obj):
        return obj.car
    carview.short_description = 'Машина'




admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
#admin.site.register(Post, PostAdmin)
