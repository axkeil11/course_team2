from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator,MaxValueValidator


class UserProfile(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(14),
                                                       MinValueValidator(70)], null=True, blank=True)
    phone_number = PhoneNumberField()
    bio = models.TextField(null=True, blank=True)
    ROLE_CHOICES =(
        ('студент','студент'),
        ('преподаватель','преподаватель'),
    )
    user_role = models.CharField(max_length=140, choices=ROLE_CHOICES, default='студент')


    def __str__(self):
        return f'{self.first_name}-{self.last_name}-{self.user_role}'


class Category(models.Model):
    category_name= models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.category_name


class Course(models.Model):
    course_name = models.CharField(max_length=140)
    course_image = models.ImageField(upload_to='course_img/', null=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name='course_category')
    LEVEL_CHOICES = (
        ('начальный','начальный'),
        ('средний','средний'),
        ('продвинутый','продвинутый')
    )
    level = models.CharField(max_length=50,choices=LEVEL_CHOICES,default='начальный')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.course_name

    def get_average_rating(self):
        reviews = self.review_set.all()
        if reviews.exists():
            return round(sum(review.rating for review in reviews) / reviews.count(), 1)
        return 0

    def get_count_reviews(self):
        return self.review_set.count()


class Lesson(models.Model):
    title = models.CharField(max_length=140)
    video_url = models.FileField(upload_to='lesson_video/', null=True, blank=True)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return self.title


class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return f'{self.title} - {self.course}'


class Exam(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete= models.CASCADE)

    def __str__(self):
        return f'{self.title}-{self.course}'

class Question(models.Model):
    text = models.CharField(max_length=200)
    create_date = models.DateField(auto_now_add=True)
    DIFFICULTY_CHOICES=(
        ('легкий','легкий'),
        ('средний','средний'),
        ('сложный','сложный')
    )
    difficulty_level = models.CharField(max_length=64, choices=DIFFICULTY_CHOICES, default='легкий')
    Questions = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='exam_questions')
    passing_score = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),
                                                                 MaxValueValidator(5)], null=True, blank=True)
    duration = models.DurationField()

    def __str__(self):
        return f'{self.text}'

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete= models.CASCADE, related_name='options')
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField()


class Certificate(models.Model):
    student = models.OneToOneField(UserProfile, on_delete= models.CASCADE)
    course = models.ForeignKey(Course, on_delete= models.CASCADE)
    issued_at = models.DateField(auto_now_add=True)
    certificate_url = models.FileField(upload_to='certificates/', null=True, blank=True)

    def __str__(self):
        return f'{self.student}-{self.course}-{self.certificate_url}'


class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete= models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    parent_review = models.ForeignKey('self',related_name='replies',null=True,blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}-{self.rating}'


class Favourite(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class FavouriteCourse(models.Model):
    cart = models.ForeignKey(Favourite, on_delete=models.CASCADE, related_name='items')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='favorite_course')

    def __str__(self):
        return f'{self.course}-{self.cart}'


class Chat(models.Model):
    client = models.ManyToManyField(UserProfile)
    created_date = models.DateField(auto_now_add=True)


class Massage(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(null=True,blank=True)
    created_date = models.DateField(auto_now_add=True)
