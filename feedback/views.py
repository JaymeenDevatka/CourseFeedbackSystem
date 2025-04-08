from django.shortcuts import render, redirect
from .models import Course, Feedback

def feedback_form(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        course_id = request.POST['course']
        comment = request.POST['comment']
        course = Course.objects.get(id=course_id)
        Feedback.objects.create(course=course, comment=comment)
        return render(request, 'feedback/thanks.html')
    return render(request, 'feedback/form.html', {'courses': courses})

def feedback_report(request):
    data = Feedback.objects.values('sentiment').order_by('sentiment')
    sentiments = {'Positive': 0, 'Negative': 0, 'Neutral': 0}
    for item in data:
        sentiments[item['sentiment']] += 1
    return render(request, 'feedback/report.html', {'sentiments': sentiments})
