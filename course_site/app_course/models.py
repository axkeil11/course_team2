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
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
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


class Lesson(models.Model):
    title = models.CharField(max_length=140)
    video_url = models.FileField(upload_to='lesson_video/')
    documents = models.ImageField(upload_to='lesson_file/')
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Question(models.Model):
    text = models.CharField(max_length=200)
    create_date = models.DateField(auto_now_add=True)
    DIFFICULTY_CHOICES=(
        ('легкий','легкий'),
        ('средний','средний'),
        ('сложный','сложный')
    )
    difficulty_level = models.CharField(max_length=64, choices=DIFFICULTY_CHOICES, default='легкий')

    def __str__(self):
        return f'{self.text}-{self.difficulty_level}'


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete= models.CASCADE, related_name='options')
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField()

    def __str__(self):
        return f'{self.text}-{self.question}'


class Exam(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete= models.CASCADE)

    def __str__(self):
        return f'{self.title}-{self.course}'


class Questions(models.Model):
    Questions=models.ForeignKey(Exam, on_delete= models.CASCADE, related_name='exam_questions')
    passing_score = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),
                                                                 MaxValueValidator(5)], null=True,blank=True)
    duration = models.DurationField(60)


class Certificate(models.Model):
    student = models.OneToOneField(UserProfile, on_delete= models.CASCADE)
    course = models.ForeignKey(Course, on_delete= models.CASCADE)
    issued_at = models.DateField(auto_now_add=True)
    certificate_url = models.FileField(upload_to='certificates/')

    def __str__(self):
        return f'{self.student}-{self.course}-{self.certificate_url}'


class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete= models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user}-{self.rating}'
