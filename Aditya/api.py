from rest_framework import permissions, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from .models import Project
from .serializers import ProjectSerializer


class IsStaffOrReadOnly(permissions.BasePermission):
    """Allow anyone to read projects; only staff can change them."""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsStaffOrReadOnly,)
    authentication_classes = (SessionAuthentication, BasicAuthentication)
