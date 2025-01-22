from rest_framework import serializers
from .models import UserProfile, Category, Course, Lesson, Assignment, Question, Option, Exam, Certificate, Review, FavouriteCourse, Favourite
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['password', 'last_name', 'username']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Неверные учетные данные")
        return user



class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name', 'username', 'profile_picture',
                  'age', 'phone_number', 'bio', 'user_role']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'username']


class CategorySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title']


class LessonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title', 'video_url', 'content']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'title', 'description', 'due_date']


class CreateAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'text', 'is_correct']


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'difficulty_level', 'passing_score', 'duration', 'options']


class ExamSerializer(serializers.ModelSerializer):
    exam_questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Exam
        fields = ['id', 'title', 'exam_questions']


class CourseListSerializer(serializers.ModelSerializer):
    category = CategorySimpleSerializer()

    class Meta:
        model = Course
        fields = ['id', 'course_name', 'course_image', 'category', 'price']


class ReviewSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    course = CourseListSerializer()

    class Meta:
        model = Review
        fields = ['id', 'user', 'course', 'rating', 'comment']


class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    category = CategorySimpleSerializer()
    lessons = LessonListSerializer(many=True, read_only=True)
    tasks = AssignmentSerializer()
    created_by = UserProfileSerializer()

    class Meta:
        model = Course
        fields = ['course_name', 'course_image', 'category', 'price', 'level',
                  'description', 'lessons', 'created_by', 'created_at', 'updated_at', 'tasks']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class CategoryDetailSerializer(serializers.ModelSerializer):
    course_category = CourseListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['category_name', 'course_category']


class CertificateSerializer(serializers.ModelSerializer):
    student = UserProfileSerializer()
    course = CourseListSerializer()

    class Meta:
        model = Certificate
        fields = ['id', 'student', 'course', 'issued_at', 'certificate_url']


class CreateCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class FavouriteCourseSerializer(serializers.ModelSerializer):
    course = CourseListSerializer()

    class Meta:
        model = FavouriteCourse
        fields = ['cart', 'course']


class FavouriteSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()

    class Meta:
        model = Favourite
        fields = ['user']