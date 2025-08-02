from django.contrib import admin
from portfolio_app.models import Project, SiteStatus

admin.site.register(SiteStatus)
admin.site.register(Project)

