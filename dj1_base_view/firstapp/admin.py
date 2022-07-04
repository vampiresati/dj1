from django.contrib import admin

from .models import Student, Parent, Child, Author, Tag, Book, Borrow


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'roll_number')


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city')
    search_fields = ('name',)


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent_id')
    list_filter = ('parent_id',)
    search_fields = ('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'slug')
    search_fields = ('slug',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cover', 'publication_date', 'isbn')
    list_filter = ('publication_date',)
    raw_id_fields = ('tags', 'authors')


@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'borrow_date', 'returned_date', 'book')
    list_filter = ('user', 'borrow_date', 'returned_date', 'book')
