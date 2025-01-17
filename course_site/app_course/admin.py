from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


# class OptionInline(admin.TabularInline):
#         model = Option
#         extra = 1
#
#
# class QuestionInline(admin.TabularInline):
#         model = Question
#         extra = 1
#
#
# @admin.register(Category, Course, Lesson, Assignment)
# class CategoryAdmin(TranslationAdmin):
#
#     class Media:
#         js = (
#             'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
#             'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
#             'modeltranslation/js/tabbed_translation_fields.js',
#         )
#         css = {
#             'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
#         }
#
#
# @admin.register(Exam)
# class ExamAdmin(TranslationAdmin):
#     inlines = [QuestionInline]
#     class Media:
#         js = (
#             'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
#             'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
#             'modeltranslation/js/tabbed_translation_fields.js',
#         )
#         css = {
#             'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
#         }
#
#
# @admin.register(Question)
# class QuestionAdmin(TranslationAdmin):
#     inlines = [OptionInline]
#     class Media:
#         js = (
#             'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
#             'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
#             'modeltranslation/js/tabbed_translation_fields.js',
#         )
#         css = {
#             'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
#         }
#


# admin.site.register(UserProfile)
# admin.site.register(Certificate)
# admin.site.register(Lesson)
# admin.site.register(Assignment)
# admin.site.register(Question)
# admin.site.register(Option)
# admin.site.register(Exam)
# admin.site.register(Questions)
# admin.site.register(Review)
# admin.site.register(Category)