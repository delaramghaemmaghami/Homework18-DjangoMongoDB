from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=150)

    def __str__(self):
        return self.title
