from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=10,verbose_name='题目')
    content = models.TextField(verbose_name='内容')
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
