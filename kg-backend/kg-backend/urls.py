from django.urls import path
from app.views import test, user, file, permission


urlpatterns = [
    path(r'test', test.test),
    path(r'user/register', user.register),
    path(r'user/login', user.login),
    path(r'file/uploadFile', file.upload_file),
    path(r'file/searchFileList', file.search_file_list),
    path(r'file/getFileDetail', file.get_file_detail),
    path(r'file/getSuccessFiles', file.get_success_files),
    path(r'file/getFailureFiles', file.get_failure_files),
    path(r'file/getUploadedFiles', file.get_uploaded_files),
    path(r'file/getUnauditedFiles', file.get_unaudited_files),
    path(r'file/examineFile', file.examine_file),
    path(r'file/getFileList', file.get_file_list),
    path(r'file/changeFile', file.change_file),
    path(r'file/deleteFile', file.delete_file),
    path(r'permission/getPermissionList', permission.get_permission_list),
    path(r'permission/changePermission', permission.change_permission),
    path(r'permission/guardAdmin',permission.grant_admin)
]
