from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Scope, Article, Tag


# class RelationshipInlineFormset(BaseInlineFormSet):
#     def clean(self):
#         for form in self.forms:
#             if not form.cleaned_data:
#                 raise ValidationError
#
#         return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    # formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    list_filter = ['id']
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
