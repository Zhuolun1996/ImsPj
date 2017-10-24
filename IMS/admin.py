from django.contrib import admin
from IMS.models import staff, Gstudent, Ustudent, indexContent, blog, papers, event, patent, resource, ask, about

# Register your models here.
admin.site.register(staff)
admin.site.register(Gstudent)
admin.site.register(Ustudent)
admin.site.register(indexContent)
admin.site.register(blog)
admin.site.register(papers)
admin.site.register(event)
admin.site.register(patent)
admin.site.register(resource)
admin.site.register(ask)
admin.site.register(about)
