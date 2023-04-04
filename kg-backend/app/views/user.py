from app.utils.jsonResponse import json_response
from django.views.decorators.csrf import csrf_exempt
from app.models import User, Permission, UserPermission
import hashlib
from app.utils.jwtAuth import create_token


# 用户注册
@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if not (username and password and email):
            return json_response(201, '请输入完整数据')
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return json_response(202, '账号或用户名已存在')
        encry = hashlib.md5()
        encry.update(password.encode())
        md5_pwd = encry.hexdigest()  # 密码加密
        user = User(username=username, password=md5_pwd, email=email, role=0)
        user.save()
        # 导入权限表数据
        user_id = User.objects.filter(username=username).first()
        permission_list = Permission.objects.values_list("permission_id")
        for permission in permission_list:
            user_permission = UserPermission(user=user_id, permission_id=permission[0])
            user_permission.save()
        return json_response(200, '创建成功')
    else:
        return json_response(203, '无效的请求方法')


# 用户登录
@csrf_exempt
def login(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        email = request.POST.get('email')
        if not (password and email):
            return json_response(201, '请输入完整数据')
        if User.objects.filter(email=email):  # 账号存在
            encry = hashlib.md5()
            encry.update(password.encode())
            md5_pwd = encry.hexdigest()  # 密码加密
            username=User.objects.filter(password=md5_pwd).first().username
            if username:
                token = create_token({"email": email})
                return json_response(200, '登录成功', {"username": username, "token": token})
            else:
                return json_response(204, '密码错误')
        else:
            return json_response(205, '账号不存在')
    else:
        return json_response(203, '无效的请求方法')
