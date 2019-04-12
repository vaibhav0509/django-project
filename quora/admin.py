from django.contrib import admin

from quora.models import Tag, Question, Answer

admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Answer)