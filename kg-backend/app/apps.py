from django.apps import AppConfig
from django.db.models.signals import post_migrate
import hashlib


# 初始化数据库
def init_account(sender, **kwargs):
    from app.models import User, Permission, Settings, DocumentField
    from app.models import Graph
    if not User.objects.filter(username='admin').exists():
        password = "123456"
        encry = hashlib.md5()
        encry.update(password.encode())
        md5_pwd = encry.hexdigest()  # 密码加密
        # 创建超级管理员
        User.objects.create(username='admin', password=md5_pwd, email="admin@qq.com", role=1)
        # 创建权限
        Permission.objects.create(permission_name="uploadFile")
        Permission.objects.create(permission_name="searchFileList")
        Permission.objects.create(permission_name="getAnswer")
        Permission.objects.create(permission_name="getGraph")
        # 创建设置
        Settings.objects.create(name="auto_examine", isOpened="1")
        Settings.objects.create(name="turn_off_permission_control", isOpened="1")
        # 创建文献类别
        DocumentField.objects.create(field_name="literature")
        DocumentField.objects.create(field_name="biology")
        DocumentField.objects.create(field_name="medicine")
        # 创建管理员图谱
        Graph.objects.create(username='admin', graph={})


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        post_migrate.connect(init_account, sender=self)
