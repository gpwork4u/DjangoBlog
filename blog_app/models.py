from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=100)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title