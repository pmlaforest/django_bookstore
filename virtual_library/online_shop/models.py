from django.db import models

# Create your models here.
class Subject:

    def __init__(self):
        self._observers = []
        self.attach(History())

    def  attach(self, observer):
        if not observer in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError as err:
            pass

    def notify(self, **kwargs):
        for observer in self._observers:
            observer.update(self, **kwargs)

class Sale(models.Model,Subject):

    def save(self):
        super().save()
        self.notify()

class History(models.Model):

    def update(self, subject, **kwargs):
        self.action = "sale"
        self.username = subject.user.username
        self.total = subject.product #subject.product.total
        self.time_stamp = "this is a time stamp"
        self.save(force_insert=True)
