from django.contrib import admin

# Register your models here.


from .models import Books

class BooksAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "page_count", "avg_rating")

admin.site.register(Books, BooksAdmin)
