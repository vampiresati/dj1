from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Student(models.Model):
    # id=models.AutoField()
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    roll_number=models.IntegerField()
    class Meta:
        verbose_name='Student'
class Parent(models.Model):
    name=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Child(models.Model):
    name=models.CharField(max_length=50)
    parent_id=models.ForeignKey(Parent, on_delete=models.CASCADE,related_name='children')
    def __str__(self):
        return self.parent_id.name+","+self.name

####
# sudo apt-get install graphviz graphviz-dev
# pip3 install pygraphviz
# pip3 install django-extensions
#  python3 manage.py graph_models firstapp -g -o model_vi.png


class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name=('First name'))
    last_name = models.CharField(max_length=40, verbose_name=('Last name'))

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name = ('Author')
        verbose_name_plural = ('Authors')


class Tag(models.Model):
    word = models.CharField(max_length=35, verbose_name=('Word'))
    slug = models.CharField(max_length=50, verbose_name=('Slug'))

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = ('Tag')
        verbose_name_plural = ('Tags')

class BookTataManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(title='tata')

class Book(models.Model):
    title = models.CharField(max_length=40, verbose_name=('Title'))
    cover = models.ImageField(upload_to='book-covers', verbose_name=('Cover'), blank=True)
    tags = models.ManyToManyField(Tag, verbose_name=('Tags'), related_name='books')
    authors = models.ManyToManyField(Author, verbose_name=('Authors'), related_name='books')
    publication_date = models.DateField(verbose_name=('Publication date'))
    isbn = models.CharField(max_length=40,verbose_name=('ISBN code'))
    book=models.Manager()
    objects=models.Manager()
    tata=BookTataManager()
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Book')
        verbose_name_plural = ('Books')



class Borrow(models.Model):
    user = models.OneToOneField(get_user_model(), verbose_name=('Usuario'), on_delete=models.PROTECT)
    borrow_date = models.DateField(verbose_name=('Borrow date'))
    returned_date = models.DateField(verbose_name=('Returned date'), blank=True, null=True)
    book = models.ForeignKey(Book, verbose_name=('Book'), on_delete=models.PROTECT)

    class Meta:
        verbose_name = ('Borrow')
        verbose_name_plural = ('Borrows')

    def __str__(self):
        return '{}_{}'.format(self.user, self.borrow_date)
