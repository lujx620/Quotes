from __future__ import unicode_literals
from django.db import models
from ..log_reg.models import Users
# Create your models here.
class QuotesManager(models.Manager):
    def validate(self, postData, user_id):
        quoter= postData['quoter']
        content= postData['content']

        flag = False
        errs=[]

        if len(quoter)<=3:
            flag= True
            errs.append('Quoted by must be more than 3 characters')
        if len(content)< 10:
            flag = True
            errs.append('Quote must be more than 10 characters long')
        if flag is False:
            quote= self.create(quoter=quoter, content = content, user_id= user_id)

            return (flag, quote)
        else:
            return (flag, errs)

class Quotes(models.Model):
    quoter= models.CharField(max_length= 100)
    content = models.TextField()
    user = models.ForeignKey(Users, related_name='user')
    favorite = models.ManyToManyField(Users, related_name ='fav_by')
    objects = QuotesManager()
