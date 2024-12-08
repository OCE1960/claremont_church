from django.contrib import admin


class MyAdminSite(admin.AdminSite):
    site_header = "Claremont Church"
    site_title = "Claremont Church official website"