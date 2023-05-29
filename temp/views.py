from .models import User, Message
from .serializers import UserSerializer, MessageSerializer
from utils.api import MyAPI

class Test(MyAPI):
    def get(self, request):
        result = self.success("따흐흑")
        return result
    
class CreateMSG(MyAPI):
    '''
    채팅 메세지 생성
    '''
    def get(self, request):
        user = request.GET.get('user')
        msg = request.GET.get('msg')
        
        if msg:
            result = Message.objects.create(message=msg)
        else:
            self.error("No msg")
            
        if user:
            result.user = user
        
        result.save()
        
        return self.success("ok")

class GetMessages(MyAPI):
    '''
    채팅 가져오기
    '''
    def get(self,request):
        # serializer = MessageSerializer(Message.recentMsg(), many=True)
        serializer = MessageSerializer(Message.objects.get(id=1))
        result = dict(serializer.data)
        result["aaa"] = 'ABC'
        print(result)
        
        return self.success(result)
    
class SyncMessage(MyAPI):
    '''
    최신 채팅 시퀸스 가져오기
    '''
    def get(self,request):
        last=request.GET.get("id")
        msg=Message.objects.filter(id__gt=last)
        serializer = MessageSerializer(msg, many=True)
        print(len(msg))
        return self.success(serializer.data)