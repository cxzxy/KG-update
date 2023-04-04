from django.views.decorators.csrf import csrf_exempt
from app.utils.jsonResponse import json_response
from app.models import User, UserPermission
import json


@csrf_exempt
def get_permission_list(request):
    if request.method == 'GET':
        user = User.objects.filter(email=request.user_info).first()
        if user.role == 1:
            users = User.objects.all().filter(role=0)
            user_list = []
            for user in users:
                user_dict = {}
                user_dict['user_id'] = user.user_id
                user_dict['username'] = user.username
                user_dict['email'] = user.email
                user_dict['permission'] = []
                for permission in user.userpermission_set.all():
                    permission_dict = {}
                    permission_dict['permission_id'] = permission.permission_id
                    permission_dict['permission_name'] = permission.permission.permission_name
                    permission_dict['is_allowed'] = permission.is_allowed
                    user_dict['permission'].append(permission_dict)
                user_list.append(user_dict)
            return json_response(200, '请求成功', user_list)
        else:
            return json_response(206, '无权限该操作')
    else:
        return json_response(203, '请求方式错误')


@csrf_exempt
def change_permission(request):
    if request.method == 'POST':
        user = User.objects.filter(email=request.user_info).first()
        if user.role == 1:
            data = json.loads(request.body)
            user_id = data['user_id']
            permission_id = data['permission_id']
            is_allowed = data['is_allowed']
            for i in range(len(permission_id)):
                userpermission = UserPermission.objects.filter(user_id=user_id, permission_id=permission_id[i]).first()
                userpermission.is_allowed = is_allowed[i]
            userpermission.save()
            return json_response(200, '修改成功')
        else:
            return json_response(206, '无权限该操作')
    else:
        return json_response(203, '请求方式错误')


@csrf_exempt
def grant_admin(request):
    if request.method == 'POST':
        user = User.objects.filter(email=request.user_info).first()
        if user.role == 1:
            user_id = request.POST.get('user_id')
            new_admin = User.objects.filter(user_id=user_id).first()
            new_admin.role = 1
            new_admin.save()
            userpermission = UserPermission.objects.filter(user_id=user_id)
            userpermission.delete()
            return json_response(200, '操作成功')
        else:
            return json_response(206, '无权限该操作')
    else:
        return json_response(203, '请求方式错误')
