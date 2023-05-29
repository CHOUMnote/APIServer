from .serializers import ScoreSerializer
from utils.api import MyAPI
from .models import ScoreBoard

class Test(MyAPI):
    def get(self, request):
        result = self.success("따흐흑")
        return result
    
class CreateScore(MyAPI):
    '''
    데이터 저장
    '''
    def get(self,request):
        s = request.GET.get('score', 0)
        c = request.GET.get('clip', 'guest')
        
        model = ScoreBoard.objects.create(score = s, clip = c)
        
        return self.success("ok")
    
class GetScore(MyAPI):
    def get(self, request):
        obj = ScoreBoard.objects.all()
        se = ScoreSerializer(obj, many=True)
        return self.success(se.data)