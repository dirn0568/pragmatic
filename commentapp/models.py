from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article

# ForeignKey는 1:N관계로 서로를 연결시키기위해 사용함 N인쪽에서 ForeignKey를 선언

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, related_name='comment')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment')

    content = models.TextField(null=False)
    # created_at이라서 자동으로 생성되는지 models.DateTimeField(auto_now=True)이라서 자동생성되는지 잘모르겠음
    created_at = models.DateTimeField(auto_now=True)