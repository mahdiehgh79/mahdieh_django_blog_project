from django.db import models
from django.shortcuts import reverse
class Post(models.Model) :

    STATUES_CHOISES = (
        ('PUB','PUBLISHED'),
        ('DRF','DRAFT'),
    )
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    statues = models.CharField(choices=STATUES_CHOISES,max_length=3)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('posts_detail',args=[self.id])


