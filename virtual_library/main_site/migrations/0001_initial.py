# Generated by Django 2.0.4 on 2018-04-17 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateTimeField(blank=True, null=True, verbose_name='date of birth')),
                ('date_of_death', models.DateTimeField(blank=True, null=True, verbose_name='date of death')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='date published')),
                ('synopsis', models.TextField(blank=True, max_length=2500)),
                ('path_to_img', models.CharField(max_length=260)),
            ],
        ),
        migrations.CreateModel(
            name='Book_Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_site.Author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_site.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Book_Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_site.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='book_genre',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_site.Genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(through='main_site.Book_Author', to='main_site.Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(through='main_site.Book_Genre', to='main_site.Genre'),
        ),
    ]
