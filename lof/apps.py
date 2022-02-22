from django.contrib.admin.apps import AdminConfig


class LocumFinderConfig(AdminConfig):
    default_site = 'lof.admin.LocumFinderAdminSite'
