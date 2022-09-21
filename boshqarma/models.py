from django.db import models

class News(models.Model):
    title = models.CharField(max_length=100, null=True)
    body = models.TextField(null=True)
    image = models.ImageField(upload_to='news/%Y/%m/%d')
    date = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return self.title

class SendModel(models.Model):
    fish = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    mavzu = models.CharField(max_length=100, null=True)
    xabar = models.TextField(null=True)

    def __str__(self):
        return self.fish

class QuyiTashkilotlar(models.Model):
    title = models.CharField(max_length=100, null=True)
    info = models.TextField(null=True)
    image = models.ImageField(upload_to='branches/')

    def __str__(self):
        return self.title
