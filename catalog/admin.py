from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

# Register your models here.
class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

class BookInline(admin.TabularInline):
    model = Book
    extra = 0
    exclude = ["summary","genre"]

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name","first_name","date_of_birth","date_of_death")
    fields = ["first_name","last_name",("date_of_birth","date_of_death")]
    inlines = [BookInline]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title","author","display_genre")
    inlines = [BookInstanceInline]

@admin.register(BookInstance)
class BookInstance(admin.ModelAdmin):
    list_display = ("book","status","borrower","due_back","id")
    list_filter = ("status","due_back")
    fieldsets = (
        (None, {
            "fields":("book","imprint","id")
        }),
        ("Availability", {
            "fields":("status","due_back", "borrower")
        })
    )
    
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
