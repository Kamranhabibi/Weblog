from django.contrib import admin
from .models import Article, Category, Comment, Input , Like

# Register your models here.

admin.site.register(Category)


class FilterByTitle(admin.SimpleListFilter):
    title = 'کلید های پر تکرار'
    parameter_name = 'title'
    def lookups(self, request, model_admin):
        return (
            ("django",'جنگو'),
            ("python",'پایتون'),
        )
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title__icontains=self.value())


class CommentInline(admin.TabularInline):
    model = Comment
#class CommentInline(admin.StackedInline):
 #   model = Comment

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('author','title','status',)
    list_editable = ('title','status',)
    list_filter = ('status',FilterByTitle)
    search_fields = ('body',)
    inlines = (CommentInline,)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['body','user','parent','create']



@admin.register(Input)
class InputAdmin(admin.ModelAdmin):
    list_display = ['name','subject','date']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('article','user','create',)
