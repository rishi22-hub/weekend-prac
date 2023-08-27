from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import branch,Student,college
from .forms import CollegeForm,StudentForm,BranchForm
def get_branches(request):
    college_id = request.GET.get('college_id')
    branches = branch.objects.filter(college_id=college_id)
    branch_list = [{"id": branch.id, "name": branch.name} for branch in branches]
    return JsonResponse(branch_list, safe=False)




def get_branch(request):
    college_name = request.GET.get('college')
    branches_data = []
    print(college_name)
    if college_name:
        try:
            college_instance = college.objects.get(name=college_name)
            branch_objects = branch.objects.filter(college=college_instance)
            
            for obj in branch_objects:
                branch_info = {
                    'id': obj.id,
                    'name': obj.name  # Adjust field name if different
                }
                branches_data.append(branch_info)
                
        except college.DoesNotExist:
            return JsonResponse({'error': 'College not found'}, status=404)

    return JsonResponse({'branches': branches_data})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('student')
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})


def add_college(request):
    if request.method == 'POST':
        form = CollegeForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('college')
    else:
        form = CollegeForm()

    return render(request, 'add_college.html', {'form': form})


def add_branch(request):
    if request.method == 'POST':
        form = BranchForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('branch')
    else:
        form = BranchForm()

    return render(request, 'add_branch.html', {'form': form})



cols = ['name','college','branch','jeerank']
def show_students(request):
    student=Student.objects.all()
    print(student)
    names = Student.objects.values_list('name', flat=True).distinct()
    colleges = college.objects.values_list('name', flat=True).distinct()  # Assuming College has a 'name' field
    branches = branch.objects.values_list('name', flat=True).distinct()  # Assuming Branch has a 'name' field
    
    extra_cols=["location","col1","col2","col3"]
    if request.method == 'POST':
        cols.append(request.POST.get('selected_column'))
    context={
        'names': names,
    'colleges': colleges,
    'branches': branches,
        'data':student,
        'fix_col':cols,
        'cols':extra_cols
    }
    return render(request,'show_student.html',context)



def home(request):
    context={}
    return render(request,"home.html",context)



def add_col(request):
   
    return render(request,"show_student.html",{})