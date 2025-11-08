from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task, Category

def index(request):
    tasks=Task.objects.all()

    #lấy tất cả các task từ cơ sở dữ liệu
    return render(request,'index.html',{'tasks':tasks})

def newlisttodo(request):
    categories=Category.objects.order_by('name')
    selected_category_id=request.GET.get('category','')
    selected_category=None
    if selected_category_id.isdigit():
        selected_category=Category.objects.filter(id=int(selected_category_id)).first
    qs=Task.objects.all()
    if selected_category is not None:
        qs=qs.filter(category=selected_category)


    todo_tasks=qs.filter(status='todo')
    working_tasks=qs.filter(status='working')
    done_tasks=qs.filter(status='done')
    edit_id=request.GET.get('edit_id')
    edit_id=int(edit_id) if edit_id and edit_id.isdigit() else None
    print(edit_id)
    context={
        'categories':categories,
        'select_category_id':selected_category_id if selected_category else '',
        'todo_tasks':todo_tasks,
        'working_tasks':working_tasks,
        'done_tasks':done_tasks,
        'edit_tasks':edit_id,
    }
    return render(request,'newtodo.html',context)

def add_category(request):
    print('vao')
    if request.method=='POST':
        name=request.POST.get('category_name','').strip()
        if name:
            print(name)
            Category.objects.create(name=name)
    return redirect('newlisttodo')

#thêm task vào cơ sở dữ liệu
def add_task(request):
    if request.method=='POST':
        #lấy trường dữ liệu task_description từ form
        task_description=request.POST.get('task_description')
        status=request.POST.get('status','todo')
        category_id=request.POST.get('category_id','').strip()
        category=None
        if category_id.isdigit():
            category=Category.objects.filter(id=int(category_id)).first()
        if task_description:
            #lưu task vào cơ sở dữ liệu
            Task.objects.create(description=task_description,status=status)
        # chuyển hướng về trang chính
        return redirect('newlisttodo')
    else:
        # chuyển hướng về trang chính
        return redirect('newlisttodo')
#xóa task khỏi cơ sở dữ liệu

def delete_task(request,task_id):
    #lấy task theo id
    task=get_object_or_404(Task,id=task_id)
    #xoá task
    task.delete()
    # chuyển hướng về trang chính
    return redirect('newlisttodo')
    
def edit_task(request,task_id):
    task=Task.objects.get(Task,id=task_id)
    if request.method =='POST':
        description = request.POST.get('description','').strip()
        status = request.POST.get('status', task.status)
        if description:
            task.description = description
        if status in dict(Task.STATUS_CHOICES):
            task.status = status
        task.save()
        return redirect('newlisttodo')
    


















def baitho(request):
    return HttpResponse('Xin Chào Baitho')
# Create your views here.

def amDuong(request,a):
    a=int(a)
    if a>0:
        return HttpResponse(f'{a} là số dương')
    else:
        return HttpResponse(f'{a} là số âm')
    
def phepNhan(request,a):
    a=int(a)
    result=''
    for i in range(1,11,1):
        result+=f'{a}x{i}={a*i}<br>'
    
    return HttpResponse(result)

