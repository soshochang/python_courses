from django.shortcuts import render, redirect
from .models import Course
from IPython import embed #Remember you need to pip install ipython into your environment first!

# Create your views here.
def index(request):
  # Course.objects.create(name="c1",description="d1")
  # courses = Course.objects.all()
  # print courses
  context = {
    "courses": Course.objects.all()
  }

  return render(request, "courses/index.html", context)

def add_course(request):
  embed()
  if request.method == "POST":
    embed()
    Course.objects.create(name=request.POST['name'],description=request.POST['description'])
    

  # request.session['name'] = request.POST['first_name']
  return redirect('/')


















def remove_course(request, id):
  print "deleting"
  c = Course.objects.get(pk=id)
  c.delete()
  return redirect('/')  

def remove_course_page(request, id):
  # print "deleting"
  # c = Course.objects.get(pk=id)
  # c.delete()
  context = {
    "course": Course.objects.get(pk=id)
  }
  return render(request, 'courses/remove.html', context)  