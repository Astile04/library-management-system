from django.contrib import admin
from . import models
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display= ['name','created_at']
    search_fields = ['name']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author','isbn','available_copies']
    search_fields = ['title','isbn']
    list_filter = ['author']

class MemberAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','joined_date']
    search_fields = ['name','email']

class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ['book','member','borrow_date','return_date','is_returned']
    list_filter = ['is_returned']
    search_fields = ['book__title','member__name']


admin.site.register(models.Author,AuthorAdmin)
admin.site.register(models.Book,BookAdmin)
admin.site.register(models.Member,MemberAdmin)
admin.site.register(models.BorrowRecord,BorrowRecordAdmin)