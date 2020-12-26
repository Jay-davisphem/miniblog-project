from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    """Model representing blog post"""
    title = models.CharField(max_length=100)
    date = models.DateTimeField('Post date', null=True, blank=True)
    author = models.ForeignKey(
        'Blogger', on_delete=models.SET_NULL, null=True
    )
    description = models.TextField(
        max_length=5000, help_text='Enter your blog post here'
    )
    class Meta:
        ordering = ['date']
    def __str__(self):
        return f'{self.title} by {self.author}'

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

class Commenter(models.Model):
    """Model representing those who comments on a post
    Model representing a blogger.
    """
    username = models.CharField(max_length=100)
    class Meta:
        ordering = ['username']
    def __str__(self):
        return self.username

class Blogger(Commenter):
    """Model representing bloggers on the page"""
    profile = models.TextField('Bio', help_text='Enter blogger biography')

    class Meta:
        permissions = (('can_post_blog', 'Post blog post'), )
    def __str__(self):
        return f'{self.username}'
    def get_absolute_url(self):
        return reverse('blogger', args=[str(self.id)])

class Comment(models.Model):
    """Model representing Commenters comments on a post"""
    comment = models.TextField(null=True, blank=True)
    date = models.DateTimeField('Comment Date', null=True, blank=True)
    post = models.ForeignKey(
        'Post', on_delete=models.SET_NULL, null=True
    )
    commenter = models.ForeignKey(
        Commenter, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        ordering = ['date']
    def __str__(self):
        return f'{self.commenter} commented on {self.post}'
