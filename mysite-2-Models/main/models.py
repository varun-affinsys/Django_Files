from django.db import models

# models map to database tables
# Create your models here.
class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length = 200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField("date published")

    def __str__(self):
        return self.tutorial_title
