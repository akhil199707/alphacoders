from django.db import models
from django.utils.text import slugify
#from django.contrib.auth import get_user_model
from accounts.models import Profile
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Create your models here.



class Question(models.Model):

    TYPE = (
    ('Easy peasy lemon squeezy', 'Easy peasy lemon squeezy'),
    ('Not so easy and not so hard too...', 'Not so easy and not so hard too...'),
    ('Hard question good make sure you have good knoledge about programing', 'Hard question good make sure you have good knoledge about programing'),
    ('good your are mastreing the programing', 'good your are mastreing the programing'),
    )

    POINTS =(
    ('5','5'),
    ('10','10'),
    ('15','15'),
    ('20','20')
    )

    qid = models.AutoField(primary_key=True)
    question_title = models.CharField(max_length=100)
    question_text = models.TextField(max_length=50000)
    question_type = models.CharField(max_length=100,choices=TYPE,null=True)
    points = models.CharField(max_length=3, choices=POINTS,null=True)
    slug = models.SlugField(max_length=40)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.question_title)
        super(Question, self).save(*args, **kwargs)

class Python(models.Model):

    ques = models.OneToOneField(Question,on_delete=models.CASCADE,primary_key=True)
    test = models.TextField(max_length=10000000,null=True)

class Solved(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    ques = models.IntegerField(default=0)
