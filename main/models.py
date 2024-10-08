from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class GiggleCatalogue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    giggleLevel = models.IntegerField(null=True, blank=True, default=0)
    time = models.DateField(auto_now_add=True)

