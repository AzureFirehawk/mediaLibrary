from django.db import models

# Create your models here.
class MediaItem(models.Model):
  STATUS_CHOICES = [
    ('wishlist', 'Wishlist'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
  ]

  TYPE_CHOICES = [
    ('game', 'Game'),
    ('book', 'Book'),
    ('movie', 'Movie'),
    ('show', 'TV Show'),
    ('other', 'Other'),
  ]

  title = models.CharField(max_length=200)
  creator = models.CharField(max_length=200)
  type = models.CharField(
    max_length=20, 
    choices=TYPE_CHOICES, 
    default='game')  
  status = models.CharField(
    max_length=20, 
    choices=STATUS_CHOICES,
    default='wishlist')
  notes = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def next_status(self):
    if self.status == 'wishlist':
      return 'in_progress'
    elif self.status == 'in_progress':
      return 'completed'
    return None

  def __str__(self):
    return self.title