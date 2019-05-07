from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Post model and User model will have a one to many relationship as user will be the Author of one or
# multiple post and post only should have one author and to do this, we need 'Foreign key'
# Create your models here -> Post is a table 
class Post(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100)
    content = models.TextField(default='Demo Posts')
    # date_posted = models.DateTimeField(auto_now_add=true) -> add exact posted time and cannot be modified
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User , on_delete = models.CASCADE)
    # on-delete is telling django if User is deleted, posts will also be deleted
    # Here author/user is the primary key of User table

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail' , kwargs={'pk' : self.pk})
