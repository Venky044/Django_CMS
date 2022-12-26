from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import date

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.

class Staffs(models.Model):
    GENDER_TYPE = (
        ('M', 'Male'), ('F', 'Female')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, choices=GENDER_TYPE)
    education = models.CharField(max_length=100, null=True, blank=True)
    profile_img = models.ImageField(upload_to='Profile-img/', default='Profile-img/user-default.png', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.user.username


class Courses(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Students(models.Model):
    GENDER_TYPE = (
        ('M', 'Male'), ('F', 'Female')
    )
    roll_no = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True, blank=True)
    course = models.ForeignKey(Courses, on_delete=models.DO_NOTHING)
    gender = models.CharField(max_length=100, choices=GENDER_TYPE)
    profile_img = models.ImageField(upload_to='Profile-img/', default='Profile-img/std-image.png', null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Subjects(models.Model):
    name = models.CharField(max_length=20)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staffs, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Result(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    subcode_1 = models.IntegerField()
    subcode_2 = models.IntegerField()
    subcode_3 = models.IntegerField()
    
    @property
    def get_total(self):
        total = self.subcode_1 + self.subcode_2 + self.subcode_3
        return total

    @property
    def get_result(self):
        result = (self.get_total) / 3
        if result < 35:
            return 'Fail'
        return result

    def __str__(self):
        return self.student.name


class MessageToStaff(models.Model):
    recipient = models.ForeignKey(Staffs, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ['is_read', '-created']

    def __str__(self):
        return self.subject + ' | ' + self.recipient.name


class MessageToStudent(models.Model):
    recipient = models.ForeignKey(Students, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ['is_read', '-created']

    def __str__(self):
        return self.subject + ' | ' + self.recipient.name


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    created = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Events(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField()
    created = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    @property
    def Days_till(self):
        event_date = self.date.date()
        remain_days = event_date - date.today()
        return str(remain_days).split(',')[0]


# @receiver(post_save, sender=User)
def createStaff(sender, instance, created, **kwargs):
    if created:
        user = instance
        staff = Staffs.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
        )
        
post_save.connect(createStaff, sender=User)


@receiver(post_save, sender=Staffs)
def updateUser(sender, instance, created, **kwargs):
    staff = instance
    user = staff.user

    if created == False:
        user.first_name = staff.name,
        user.email = staff.email,
        user.save()


@receiver(post_delete, sender=Staffs)
def deleteUser(sender, instance, **kwagrs):
    user = instance.user
    user.delete()