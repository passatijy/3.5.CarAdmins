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
    list_display = ('машина', 'title',)
    list_filter = ('title',)
    search_fields = ('title',)
    form = ReviewAdminForm
    def машина(self, obj):
        return obj.car


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
#admin.site.register(Post, PostAdmin)
