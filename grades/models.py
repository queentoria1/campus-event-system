from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Course(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.code} - {self.name}"

class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='scores')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='scores')
    score = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)]
    )
    
class Meta:
        unique_together = ('student', 'course')

        def __str__(self):
            return f"{self.student} | {self.course.code}: {self.score}"