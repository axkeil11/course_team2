from rest_framework import routers
from .views import *
from django.urls import path, include


router = routers.SimpleRouter()
router.register(r'user', UserProfileViewSet, basename='user')
router.register(r'question', QuestionViewSet, basename='question')
router.register(r'option', OptionViewSet, basename='option')
router.register(r'favourite', FavouriteViewSet, basename='favourite')
router.register(r'favourite_course/', FavouriteCourseViewSet, basename='favourite_course')


urlpatterns = (
    path('', include(router.urls)),
    path('course/', CourseListApiView.as_view(), name='course_list'),
    path('course/<int:pk>/', CourseDetailApiView.as_view(), name='course_detail'),
    path('course/create/', CourseCreateApiView.as_view(), name='course_create'),
    path('lesson/', LessonListApiView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonDetailApiView.as_view(), name='lesson_detail'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('exam/', ExamApiView.as_view(), name='exam_list'),
    path('category/', CategoryApiView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailApiView.as_view(), name='category_detail'),
    path('review/', ReviewApiView.as_view(), name='review'),
    path('review/create/', ReviewCreateAPIView.as_view(), name='review_create'),
    path('assignment/', AssignmentApiView.as_view(), name='assignment'),
    path('assignment/create/', AssignmentCreateAPIView.as_view(), name='assignment_create'),
    path('certificate/', CertificateApiView.as_view(), name='certificate'),
    path('certificate/create/', CertificateCreateApiview.as_view(), name='certificate_create'),
)
