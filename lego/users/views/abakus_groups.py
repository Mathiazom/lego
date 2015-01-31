# -*- coding: utf8 -*-
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from lego.permissions.model_permissions import PostDeleteModelPermissions
from lego.users.models import AbakusGroup
from lego.users.permissions import AbakusGroupObjectPermission
from lego.users.serializers import AbakusGroupSerializer


class AbakusGroupViewSet(viewsets.ModelViewSet):
    queryset = AbakusGroup.objects.all()
    serializer_class = AbakusGroupSerializer
    permission_classes = (IsAuthenticated, PostDeleteModelPermissions, AbakusGroupObjectPermission)
