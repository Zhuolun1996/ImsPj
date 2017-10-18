from django.contrib import admin
from IMS.models import staff,Gstudent,Ustudent,indexContent,blog,papers

# Register your models here.
admin.site.register(staff)
admin.site.register(Gstudent)
admin.site.register(Ustudent)
admin.site.register(indexContent)
admin.site.register(blog)
admin.site.register(papers)