from django.db import models
from login.models import User
from wakanda_forever.models import Article


class Comment(models.Model):
    content_type = models.ForeignKey(Article,on_delete=models.CASCADE)
    text = models.TextField()
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    comment_time = models.DateTimeField(auto_now_add=True)
    object=models.Manager()
    
    class Meta:
        ordering = ['-comment_time']
    def __str__(self):
        return self.text
    
