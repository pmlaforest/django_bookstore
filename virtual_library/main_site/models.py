from django.db import models

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