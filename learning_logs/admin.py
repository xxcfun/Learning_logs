from django.contrib import admin
# from learning_logs.models import Topic, Entry
from learning_logs.models import Topic, Entry

# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ('Topic', 'entry')

admin.site.register(Topic)
admin.site.register(Entry)
# Register your models here.
