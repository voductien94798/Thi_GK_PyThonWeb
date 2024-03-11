from django.contrib import admin
from .models import NhatKy
# admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','date']
    list_filter = ['date']
    search_fields = ['title']

admin.site.register(NhatKy,PostAdmin)
# Register your models here.
