from django.db import models

class User(models.Model):
    username = models.TextField(unique=True)
    password = models.TextField(null=False)
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    
class Message(models.Model):
    user = models.TextField(null=True, default="ㅇㅇ")
    message = models.TextField(null=False,max_length=500)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def recentMsg():
        """
        최근 메세지 출력
        """
        data = Message.objects.all().order_by("-id")[:30]
        
        return data
    
    def __str__(self):
        msg = self.user+":"+self.message
        return msg