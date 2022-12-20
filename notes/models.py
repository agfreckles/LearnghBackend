from django.db import models

# Create your models here.


class NoteInstance(models.Model):
    title = models.CharField(
        unique=True, max_length=300, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
