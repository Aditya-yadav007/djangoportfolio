from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=120)
    category = models.CharField(max_length=60, blank=True)
    description = models.TextField()
    image_url = models.URLField(blank=True)
    project_url = models.URLField(blank=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "title"]

    def __str__(self):
        return self.title
