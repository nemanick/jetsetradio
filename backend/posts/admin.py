from django.contrib import admin

from .models import Genre, Track, Like, Comment


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'color')


class CommentsInline(admin.StackedInline):
    model = Comment
    extra = 0


class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'count_likes')
    list_filter = ('author', 'title', 'genres')
    inlines = (CommentsInline,)

    def count_likes(self, obj):
        return obj.like.count()


admin.site.register(Genre, GenreAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(Like)
admin.site.register(Comment)
