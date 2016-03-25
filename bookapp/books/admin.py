from django.contrib import admin

# Register your models here.
from .models import Author, Book, Publisher


class AuthorAdmin(admin.ModelAdmin):
    fieldsets = [
         (None, {'fields': ['name']}),
         (None, {'fields': ['salutation']}),
     ]
    list_display = ('name',)


class BookInline(admin.TabularInline):
    model = Book.authors.through


class BookAdmin(admin.ModelAdmin):
    fieldsets = [
         (None, {'fields': ['title']}),
         (None, {'fields': ['publisher']}),
         (None, {'fields': ['publication_date']}),
     ]

    inlines = [
        BookInline,
    ]
    list_display = ('title', 'publisher', 'publication_date',)


admin.site.register(Author, AuthorAdmin	)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher)

