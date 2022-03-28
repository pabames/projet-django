from django.db import models

# Create your models here.

class About(models.Model):
    titre = models.CharField(max_length= 100)
    content = models.TextField()
    image = models.FileField(max_length=255, null=True)
    create_at = models.DateField(auto_now=True)

    class Meta:
        db_table = "about"


class Visa(models.Model):
    titre = models.CharField(max_length=100)
    content = models.TextField()
    autor = models.CharField(max_length=100)
    image = models.FileField(max_length=255, null=True)
    date = models.DateField(auto_now=True)
    prix = models.FloatField()
    duree = models.IntegerField()

    class Meta:
        db_table = "visa"


class Developpement(models.Model):
    titre = models.CharField(max_length=100)
    content = models.TextField()
    image = models.FileField(max_length=255, null=True)
    date = models.DateField(auto_now=True)
    prix = models.FloatField()

    class Meta:
        db_table = "developpement"

class Design(models.Model):
    titre = models.CharField(max_length=100)
    content = models.TextField()
    image = models.FileField(max_length=255, null=True)
    date = models.DateField(auto_now=True)
    prix = models.FloatField()

    class Meta:
        db_table = "design"

class Application(models.Model):
    titre = models.CharField(max_length=100)
    content = models.TextField()
    image = models.FileField(max_length=255, null=True)
    date = models.DateField(auto_now=True)
    prix = models.FloatField()

    class Meta:
        db_table = "application"

class Contact(models.Model):
    nom = models.CharField(max_length=100, null=True)
    subject = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    message = models.TextField()
    date = models.DateField(auto_now=True)

    class Meta:
        db_table = "contact"

class Actualite(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    image = models.FileField(max_length=255, null=True)
    date = models.DateField(auto_now= True)
    author = models.CharField(max_length=100)
