from django.db import models

# Create your models here.
class MediaItem(models.Model):
  STATUS_CHOICES = [
    ('wishlist', 'Wishlist'),
    ('in-progress', 'In Progress'),
    ('completed', 'Completed'),
  ]

  title = models.CharField(max_length=200)
  creator = models.CharField(max_length=200)
  status = models.CharField(
    max_length=20, 
    choices=STATUS_CHOICES,
    default='wishlist')
  notes = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title