from django.contrib import admin
from blog.models import Post, Comment

'''class PostAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Post._meta.fields]

	class Meta:
		model = Post
'''
admin.site.register(Post)
admin.site.register(Comment)
