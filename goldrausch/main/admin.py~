from main.models import Agent, Task
from django.contrib import admin
from reversion.admin import VersionAdmin


class TaskInline(admin.TabularInline):
	model = Task
	extra = 0

class AgentAdmin(admin.ModelAdmin):
	model = Agent
	inlines = [TaskInline]


admin.site.register(Agent, AgentAdmin)
admin.site.register(Task)
