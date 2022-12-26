from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages

from .models import (Staffs, Students, Result, MessageToStudent, Events)
from .form import (CustomUserCreationForm, StaffForm, StudentForm, 
                   MessageToStudentForm, MessageToStaffForm, 
                   EventsForm, ContactUsForm)

# Create your views here.

def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('staff-account')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'username does not exist')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'user logged in succussfully!')
            return redirect('staff-account')
        else:
            messages.error(request, 'username or password is incorrect.')
    
    return render(request, 'login_register.html', {'page':page})


def logoutUser(request):
    logout(request)
    messages.success(request, 'User was logged out!')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            return redirect('staff-account')
    
    context = {'form':form, 'page':page}
    return render(request, 'login_register.html', context)


def Home(request):
    page = 'home'
    return render(request, 'Base.html', {'page':page})


# COLLEGE STAFFS
def StaffList(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    staff = Staffs.objects.filter(name__icontains=search_query)
    # staff = Staffs.objects.all()
    context = {'staffs':staff, 'search_query':search_query}
    return render(request, 'staff_list.html', context)

    
def StaffDetails(request, pk):
    staff = Staffs.objects.get(id=pk)
    subject = staff.subjects_set.all()
    context = {'staff':staff, 'subjects':subject}
    return render(request, 'staff_details.html', context)


@login_required(login_url='login')
def StaffAccount(request):
    staff = request.user.staffs
    subject = staff.subjects_set.all()
    context = {'staff':staff, 'subjects':subject}
    return render(request, 'staff_account.html', context)


@login_required(login_url='login')
def Updatestaff(request, pk):
    staff = Staffs.objects.get(id=pk)
    form = StaffForm(instance=staff)
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staff', pk)
    context = {'forms':form}
    return render(request, 'form.html', context)


@login_required(login_url='login')
def StaffInbox(request):
    staff = request.user.staffs
    messageobj = staff.messagetostaff_set.all()
    unreadCount = messageobj.filter(is_read=False).count()
    context = {'messageobj':messageobj, 'unreadCount':unreadCount}

    return render(request, 'staff_inbox.html', context)


def StaffViewMessage(request, pk):
    staff = request.user.staffs
    messageobj = staff.messagetostaff_set.get(id=pk)
    # messageobj = MessageToStaff.objects.get(id=pk)

    if messageobj.is_read == False:
        messageobj.is_read = True
        messageobj.save()
    
    context = {'messageobj':messageobj}
    return render(request, 'message.html', context)


def StaffCreateMessage(request, pk):
    staff = Staffs.objects.get(pk=pk)
    form = MessageToStaffForm()

    if request.method == 'POST':
        form = MessageToStaffForm(request.POST)
        if form.is_valid():
            messageobj = form.save(commit=False)
            messageobj.recipient = staff
            messageobj.save()
            messages.success(request, 'Message sent successfully')
            return redirect('staff', pk)
    
    context = {'form':form}
    return render(request, 'message_form.html', context)


def StaffDeleteMessage(request, pk):
    staff = request.user.staffs
    messageobj = staff.messagetostaff_set.get(id=pk)
    messageobj.delete()
    return redirect('staff-inbox')



# STUDENTS
def StudentsList(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    students = Students.objects.filter(
        Q(name__icontains=search_query) |
        Q(roll_no__icontains=search_query) |
        Q(course__name__icontains=search_query)|
        Q(gender__icontains=search_query)
    )
    # students = Students.objects.all()
    total = students.count()
    context = {'students':students, 'total':total, 'search_query':search_query}
    return render(request, 'student_list.html', context)


def StudentDetails(request, pk):
    student = Students.objects.get(id=pk)
    context = {'student':student}
    return render(request, 'student_details.html', context)


@login_required(login_url='login')
def CreateStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student-List')

    context = {'forms':form}
    return render(request, 'form.html', context)


@login_required(login_url='login')
def UpdateStudent(request, pk):
    student = Students.objects.get(pk=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student', pk)

    context = {'forms':form}
    return render(request, 'form.html', context)


@login_required(login_url='login')
def DeleteStudent(request, pk):
    student = Students.objects.get(pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student-List')

    return render(request, 'delete.html', {'student':student})


def StudentResult(request):

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        try:
            student = Students.objects.get(roll_no__icontains=search_query)
            result = Result.objects.get(student=student)
            context = {'result':result, 'search_query':search_query}
            return render(request, 'result.html', context)
        except:
            return render(request, 'result.html')

    return render(request, 'result.html')

    
def StudentInbox(request):
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        try:
            student = Students.objects.get(roll_no__icontains=search_query)
            messageobj = MessageToStudent.objects.filter(recipient=student)

            total = messageobj.count()

            context = {'messageobj':messageobj, 'search_query':search_query, 'total':total}
            return render(request, 'Inbox.html', context)
        except:
            return render(request, 'Inbox.html')

    return render(request, 'Inbox.html')


def StudentViewMessage(request, pk):
    messageobj = MessageToStudent.objects.get(id=pk)

    if messageobj.is_read == False:
        messageobj.is_read = True
        messageobj.save()
    
    context = {'messageobj':messageobj}
    return render(request, 'message.html', context)



def CreateStudentMessage(request, pk):
    recipient = Students.objects.get(pk=pk)
    form = MessageToStudentForm()

    if request.method == 'POST':
        form = MessageToStudentForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.recipient = recipient
            message.save()
            messages.success(request, 'Message sent successfully')
            return redirect('student', pk)
    
    context = {'recipient':recipient, 'form':form}
    return render(request, 'message_form.html', context)


def StudentDeleteMessage(request, pk):
    messageobj = MessageToStudent.objects.get(id=pk)
    messageobj.delete()
    return redirect('student-inbox')


# Events
def EventsList(request):
    events = Events.objects.all()
    return render(request, 'events.html', {'events':events})


@login_required(login_url='login')
def AddEvents(request):
    form = EventsForm()
    if request.method == 'POST':
        form = EventsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events')

    return render(request, 'form.html', {'forms':form})


@login_required(login_url='login')
def DeleteEvents(request, pk):
    events = Events.objects.get(pk=pk)
    events.delete()
    return redirect('events')


def contactusview(request):
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        form.save()
        messages.success(request, 'Your data submitted successfully!')
        return redirect('contactus')
    
    context = {'forms':form}
    return render(request, 'form.html', context)

