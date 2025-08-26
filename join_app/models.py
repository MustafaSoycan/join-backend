from django.db import models
from datetime import date
import uuid
# Create your models here.


class Contact(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False
                          )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length=254)
    phone = models.CharField()

    def __str__(self):
        return self.first_name + " " + self.last_name


class Task(models.Model):
    id = models.UUIDField(
        primary_key=True,  # macht dieses Feld zum Primärschlüssel
        default=uuid.uuid4,  # generiert automatisch eine neue UUID
        editable=False  # verhindert, dass das Feld im Admin oder via API bearbeitet wird
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField(default=date.today)
    category = models.CharField(default="sales")
    priority = models.CharField(default="medium")
    kanban = models.CharField(default="to-do")
    subtasks = models.CharField(null=True)
    assigned_to = models.ManyToManyField(Contact, related_name='tasks')

    def __str__(self):
        return self.title
