from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField



class Tag(models.Model):
    tag=models.CharField(max_length=30)
    object=models.Manager()
    def __str__(self):
        return self.tag

class Author(models.Model):
    name=models.CharField(max_length=20)
    object=models.Manager()
    def __str__(self):
        return self.name
    
class Article(models.Model):
    article_title = models.CharField(max_length=100)
    article_content = RichTextUploadingField(default='')
    article_author = models.ForeignKey(Author,on_delete=models.CASCADE)
    article_tag = models.ForeignKey(Tag,on_delete=models.CASCADE)
    createtime = models.DateTimeField('保存日期',auto_now = True)
    object=models.Manager()
    def __str__(self):
        return self.article_title
    