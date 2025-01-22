from rest_framework import generics, viewsets, status
from .models import UserProfile, Category, Course, Lesson, Assignment, Question, Option, Exam, Certificate, Review, \
    Favourite, FavouriteCourse
from .serializers import (
    UserProfileDetailSerializer, CategorySerializer,
    AssignmentSerializer, QuestionSerializer, OptionSerializer, ExamSerializer,
    CertificateSerializer, ReviewSerializer, CourseListSerializer, CourseDetailSerializer, LessonListSerializer,
    LessonDetailSerializer, CategoryDetailSerializer, CourseSerializer, CreateCertificateSerializer, LessonSerializer,
    CreateAssignmentSerializer, CreateReviewSerializer, FavouriteSerializer, FavouriteCourseSerializer, UserSerializer,
    LoginSerializer,
)
from .permissions import CheckUser, CheckStudent
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CourseFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken



class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception= True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        try :
            serializer.is_valid(raise_exeption = True)
        except Exception:
            return Response({'detail': 'неверные учетные данные:'}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileDetailSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class CategoryApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailApiView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class CourseListApiView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CourseFilter
    search_fields = ['category', 'course_name']
    ordering_fields = ['price']


class CourseDetailApiView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer


class CourseCreateApiView(generics.CreateAPIView):
    serializer_class = CourseSerializer
    permission_classes = [CheckUser]


class LessonListApiView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer


class LessonDetailApiView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [CheckUser]


class AssignmentApiView(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class AssignmentCreateAPIView(generics.CreateAPIView):
    serializer_class = CreateAssignmentSerializer
    permission_classes = [CheckUser]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class ExamApiView(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class CertificateApiView(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class CertificateCreateApiview(generics.CreateAPIView):
    serializer_class = CreateCertificateSerializer


class ReviewApiView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewCreateAPIView(generics.CreateAPIView):
    serializer_class = CreateReviewSerializer
    permission_classes = [CheckStudent]


class FavouriteViewSet(viewsets.ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer


class FavouriteCourseViewSet(viewsets.ModelViewSet):
    queryset = FavouriteCourse.objects.all()
    serializer_class = FavouriteCourseSerializer
