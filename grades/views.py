from django.shortcuts import render
from django.db.models import Avg
from grades.models import Course, Score, Student

def gradebook_dashboard(request):
    course_top_scorers = []
    for course in Course.objects.all():
        top_3 = Score.objects.filter(course=course).order_by('-score')[:3].select_related('student')
        course_top_scorers.append({
            'course': course,
            'top_scores': top_3
        })

    failing_scores = Score.objects.filter(score__lt=50.0).select_related('student', 'course').order_by('course')

    course_average = Course.objects.annotate(
        avg_score=Avg('scores__score')
    ).order_by('-avg_score')

    context = {
        'course_top_scorers': course_top_scorers,
        'failing_scores': failing_scores,
        'course_averages': course_average,
    }

    return render(request, 'dashboard.html', context)