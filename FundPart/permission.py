from rest_framework import permissions

class IsOwnerPermission(permissions.BasePermission):
    message = 'Not allowed.'

    def has_permission(self, request, view):
    	print view.queryset
    	if request.user == view :
    		return True