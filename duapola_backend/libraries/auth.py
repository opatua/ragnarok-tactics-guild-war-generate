from django.apps import apps
from rest_framework import permissions

from duapola_backend.enums import Capability


class CapabilitiesPermission(permissions.BasePermission):
    ALLOW_ANY_CAPABILITIES = {
        Capability.CATEGORY_LIST.value,
        Capability.CATEGORY_RETRIEVE.value,
        Capability.CITY_LIST.value,
        Capability.CITY_RETRIEVE.value,
        Capability.COLOR_LIST.value,
        Capability.COLOR_RETRIEVE.value,
        Capability.COUNTRY_LIST.value,
        Capability.COUNTRY_RETRIEVE.value,
        Capability.CURRENCY_LIST.value,
        Capability.CURRENCY_RETRIEVE.value,
        Capability.PRODUCT_FAMILY_LIST.value,
        Capability.PRODUCT_FAMILY_RETRIEVE.value,
        Capability.PRODUCT_LIST.value,
        Capability.PRODUCT_RETRIEVE.value,
        Capability.PRODUCT_INVENTORY_LIST.value,
        Capability.PRODUCT_INVENTORY_RETRIEVE.value,
    }

    def has_permission(self, request, view):
        module_slug = None
        if hasattr(view, 'module_slug') and view.module_slug:
            module_slug = view.module_slug

        if not module_slug:
            return False

        action = view.action

        if action == 'partial_update':
            action = 'update'

        if not action:
            return False

        capability = '{}:{}'.format(module_slug, action)

        # Check if capability is in AllowAny set (sign in is optional)
        if capability in [enum for enum in self.ALLOW_ANY_CAPABILITIES]:
            return True

        # From here onwards, we require user
        if request.user and request.user.id:
            return True

        return False
