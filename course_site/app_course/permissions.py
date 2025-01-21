from rest_framework import permissions


class CheckUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'преподаватель':
            return True
        return False


class CheckStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_role == 'студент'