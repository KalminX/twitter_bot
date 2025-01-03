from django.db import models

class Tweet(models.Model):
    user = models.CharField(max_length=255)
    tweet = models.TextField()

    def __str__(self):
        return f'{self.user}: {self.tweet}'
