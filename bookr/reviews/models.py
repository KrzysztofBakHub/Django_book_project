from django.db import models
from django.contrib import auth

class Publisher(models.Model):
    """Company publishing books"""

    name = models.CharField(
        max_length=50,
        help_text='Publisher name'
    )

    website = models.URLField(
        help_text='Company website'
    )

    email = models.EmailField(
        help_text='Company email'
    )

    def __str__(self):
        return self.name

class Book(models.Model):
    """Published book"""

    title = models.CharField(
        max_length=70,
        help_text='Book title'
    )

    publication_date = models.DateField(
        verbose_name='Publication date'
    )

    isbn = models.CharField(
        max_length=20,
        verbose_name='Books ISBN number'
    )

    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE
    )

    contributors = models.ManyToManyField(
        'Contributor',
        through='BookContributor'
    )

    def __str__(self):
        return self.title

class Contributor(models.Model):
    """Books Contributor, i.e. author, publisher"""

    first_names = models.CharField(
        max_length=50,
        help_text='Contributor first name or names'
    )

    last_names = models.CharField(
        max_length=50,
        help_text='Contributor last name or names'
    )

    email = models.EmailField(
        help_text='Contributor email'
    )

    def __str__(self):
        return self.first_names

class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co_Author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
    )

    contributor = models.ForeignKey(
        Contributor,
        on_delete=models.CASCADE,
    )

    role = models.CharField(
        verbose_name='Role contributor played during book creation',
        choices=ContributionRole,
        max_length=20,
    )

class Review(models.Model):
    content = models.TextField(
        help_text='Review content'
    )

    rating = models.IntegerField(
        help_text='User rating'
    )

    date_created = models.DateField(
        auto_now_add=True,
        help_text='Data and time of review creation'
    )

    date_edited = models.DateField(
        null=True,
        help_text='Data and time of review editing'
    )

    creator = models.ForeignKey(
        auth.get_user_model(),
        on_delete=models.CASCADE,
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        help_text= 'Book reviewed'
    )