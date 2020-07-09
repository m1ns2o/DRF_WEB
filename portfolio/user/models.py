from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class user(models.Model):
#     username = models.CharField(max_length=64, unique=True)
#     # useremail = models.EmailField(max_length=128)
#     password = models.CharField(max_length=64)
#     # registered_dttm = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.username


class Category(models.Model):
    # owner = models.ForeignKey(user, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, db_column="user",on_delete=models.CASCADE)
    category_text = models.CharField(max_length=64)

    def __str__(self):
        return self.category_text

class Contents(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    contents_thumbnail = models.TextField()
    contents_text = models.TextField()
    contents_img = models.TextField()
    

    def __str__(self):
        return self.title
    

    

    