from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    autor = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True,null=True)
    image = models.ImageField(blank=True, null=True, upload_to='.image/')

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



