from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True, db_column='user_id')
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.IntegerField(choices=[(0, '普通用户'), (1, '管理员')])
    permission = models.ManyToManyField('Permission', through='UserPermission')

    class Meta:
        db_table = 'user'


class Permission(models.Model):
    permission_id = models.AutoField(primary_key=True, db_column='permission_id')
    permission_name = models.CharField(max_length=50, db_column='permission_name')

    class Meta:
        db_table = 'permission'


class UserPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE, db_column='permission_id')
    is_allowed = models.BooleanField(db_column="is_allowed", default=True)

    class Meta:
        db_table = 'user_permission'
        unique_together = ('user_id', 'permission_id')


class Document(models.Model):
    document_id = models.AutoField(primary_key=True, db_column='document_id')
    field = models.CharField(max_length=50)
    create_time = models.CharField(max_length=50)
    update_time = models.CharField(max_length=50)
    status = models.IntegerField(choices=[(0, '未审核'), (1, '已审核'), (2, '审核不通过')])
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id', related_name='user')
    title = models.CharField(max_length=50)
    content = models.TextField()
    reason = models.CharField(default='', max_length=100)
    auditor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='auditor')

    class Meta:
        db_table = 'document'


class QADocument(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField()
    answer = models.TextField()
    document_id = models.ForeignKey(Document, on_delete=models.CASCADE, db_column='document_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')

    class Meta:
        db_table = 'q_a_document'
