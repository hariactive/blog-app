from django.db import models
from datetime import date

# Create your models here.
class User(models.Model):
    username = models.CharField('User Name', max_length=100)
    email = models.CharField('User Email',max_length=100)
    password = models.CharField('User Password',max_length=20)
    
    
    
class Blog(models.Model):
    #Yaha pe relationship hoag one to many ka
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images/')
    title = models.CharField('Post Title', max_length=100)
    description = models.TextField('Post Description')
    posted_date = models.DateField(default = date.today)
    good_name = models.CharField('Good name', max_length=100)
    
class Comment(models.Model):
    message = models.TextField('Message')
    date_comment = models.DateField(default=date.today)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')  # This references the User who made the comment
    post_id = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='post_comments')  # This should reference the Blog (or Post) that the comment belongs to

    
        
    