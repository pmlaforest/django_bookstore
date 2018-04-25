# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Book, Author, Book_Author, SiteSettings

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Book_Author)
admin.site.register(SiteSettings)
