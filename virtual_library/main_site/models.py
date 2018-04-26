from django.db import models
from django.core.cache import cache

class Author(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField('date of birth', null=True, blank=True)
    date_of_death = models.DateTimeField('date of death', null=True, blank=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    NAMES = (
        ('SF', 'Science fiction'),
        ('S', 'Satire'),
        ('AA', 'Action and Adventure'),
        ('R', 'Romance'),
        ('M', 'Mystery'),
        ('H', 'Horror'),
        ('SH', 'Self help'),
        ('H', 'Health'),
        ('G', 'Guide'),
        ('HI', 'History'),
        ('SC', 'Science'),
        ('CO', 'Cookbooks'),
    )
    name = models.CharField(max_length=2, choices=NAMES)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', null=True,  blank=True)
    synopsis = models.TextField(max_length=2500,blank=True)
    path_to_img = models.CharField(max_length=260)


    # need to add the price of the book here !
    buy_price = models.FloatField(blank=True, null=True)
    rent_price = models.FloatField(blank=True, null=True)

    authors = models.ManyToManyField(Author, through="Book_Author")
    genres  = models.ManyToManyField(Genre, through="Book_Genre")

    def __str__(self):
        return self.title

class Book_Author(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Book_Genre(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre =  models.ForeignKey(Genre, on_delete=models.CASCADE)
#Proxy ***********************************************************************
'''
import abc


class BookI(metaclass=abc.ABCMeta):
    """
    Define the common interface for RealSubject and Proxy so that a
    Proxy can be used anywhere a RealSubject is expected.
    """

    @abc.abstractmethod
    def getTitle(self):
        pass

class Proxy(BookI):


    def __init__(self, book):
        self.book = book

    def getTitle(self):
        # ...
        self.book.request()
        # ...


class Book(BookI):

    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', null=True,  blank=True)
    synopsis = models.TextField(max_length=2500,blank=True)
    path_to_img = models.CharField(max_length=260)


    # need to add the price of the book here !
    buy_price = models.FloatField(blank=True, null=True)
    rent_price = models.FloatField(blank=True, null=True)

    authors = models.ManyToManyField(Author, through="Book_Author")
    genres  = models.ManyToManyField(Genre, through="Book_Genre")


    def getTitle(self):
        return self.title

    def setBuyPrice(self, price):
        self.buy_price=price
        return

def main():
    book = Book()
    proxy = Proxy(book)
    proxy.getSynopsis()


if __name__ == "__main__":
    main()
'''
#Singleton *******************************************************************
class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        pass

    def set_cache(self):
        cache.set(self.__class__.__name__, self)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

        self.set_cache()

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)


class SiteSettings(SingletonModel):
    support = models.EmailField(default='support@example.com')
    sales_department = models.EmailField(blank=True)
    library_account_sid = models.CharField(max_length=255, default='ACbcad883c9c3e9d9913a715557dddff99')
    library_auth_token = models.CharField(max_length=255, default='abd4d45dd57dd79b86dd51df2e2a6cd5')
    library_phone_number = models.CharField(max_length=255, default='+15006660005')
