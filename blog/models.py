from django.db import models


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    text = models.TextField(max_length=300)
    img = models.ImageField(upload_to="blog_images/")

    def get_summary(self):
        return self.text[:70]

    def __str__(self):
        return self.title
