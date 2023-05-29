from django.db import models

class ScoreBoard(models.Model):
    score = models.IntegerField(default=0)
    clip = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-score']