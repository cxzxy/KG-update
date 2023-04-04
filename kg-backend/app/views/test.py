from app.utils.jsonResponse import json_response
from app.models import User
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def test(request):
    if request.method == 'GET':
        users = User.objects.all()
        data = {"users": list(users.values())}
        return json_response(200, '请求成功', data)