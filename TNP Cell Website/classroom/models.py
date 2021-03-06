from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
from django.contrib.auth.models import User
import datetime


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Quiz(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes')
    name = models.CharField(max_length=255)
    # subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='quizzes')
    password = models.CharField(blank=True, null=True, max_length=10)

    def __str__(self):
        return self.name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField('Question', max_length=255)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField('Answer', max_length=255)
    is_correct = models.BooleanField('Correct answer', default=False)

    def __str__(self):
        return self.text


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    quizzes = models.ManyToManyField(Quiz, through='TakenQuiz')
    # interests = models.ManyToManyField(Subject, related_name='interested_students')

    def get_unanswered_questions(self, quiz):
        answered_questions = self.quiz_answers \
            .filter(answer__question__quiz=quiz) \
            .values_list('answer__question__pk', flat=True)
        questions = quiz.questions.exclude(pk__in=answered_questions).order_by('text')
        return questions

    def __str__(self):
        return self.user.username


class TakenQuiz(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='taken_quizzes')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='taken_quizzes')
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)


class StudentAnswer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='quiz_answers')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='+')

#For Training and Place Cell - IIIT Vadodara    
OFFER = (
    (('Job'), ('Job')),
    (('Internship'), ('Internship')),
    (('Job + Internship'), ('Job + Internship'))
)
SELECTION_PROCESS = (
    (('Shortlisting from Resumes'), ('Shortlisting from Resumes')),
    (('Written Test = Aptitude'), ('Written Test - Aptitude')),
    (('Group Discussion'), ('Group Discussion')),
    (('Personal Interview (Technical + HR)'), ('Personal Interview (Technical + HR)')),
    (('Written Test - Technical'), ('Written Test - Technical')),
)

class OrganizationalDetails(models.Model):
    class Meta:
        verbose_name_plural = 'OrganizationalDetail'

    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, blank=True, null=True) 
    organization_name = models.CharField(max_length= 255, blank= True, unique= True)
    organization_email = models.EmailField(max_length= 70, blank= True, null=True, unique= True)
    organization_description = models.CharField(max_length= 255)
    #organization_logo = models.ImageField(upload_to='organization_logo', blank=True)

    def __str__(self):
        return self.organization_name


class PersonalDetails(models.Model):
    class Meta:
        verbose_name_plural = 'PersonalDetail'

    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, blank=True, null=True)
    organization = models.OneToOneField(OrganizationalDetails, on_delete=models.CASCADE, blank=True, null=True, related_name='personal_details')
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length= 70,blank= True, null=True, unique= True)
    mobile = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + str(self.email) + " " + str(self.mobile)

class Job(models.Model):
    class Meta:
        verbose_name_plural = 'Job'
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    organization = models.ForeignKey(OrganizationalDetails, on_delete = models.CASCADE, blank=True, null=True, related_name='Job')
    date_of_posting = models.DateField(default=datetime.date.today)
    offer = models.CharField(choices=OFFER, default=3, max_length=50)
    primary_profile = models.CharField(max_length= 255)
    location = models.CharField(max_length= 255)
    no_of_position = models.IntegerField()
    apply_deadline = models.DateField(default=datetime.date.today)
    drive_date = models.DateField(default=datetime.date.today)
    organization_sector = models.CharField(max_length= 255)
    job_description = models.CharField(max_length= 255)
    package = models.DecimalField(decimal_places=2,max_digits=4)
    required_skills = models.CharField(max_length= 255)
    min_CPI = models.DecimalField(decimal_places=2,max_digits=4)
    selection_process = models.CharField( choices=SELECTION_PROCESS, default=1, max_length=50)
    other_details = models.CharField(max_length= 255)

    def __str__(self):
        return (str(self.date_of_posting) + " " + str(self.offer) + " " + self.primary_profile + " " + self.location + " " + str(self.no_of_position) + " " + 
                str(self.apply_deadline) + " " + str(self.drive_date) + " " + self.organization_sector + " " + 
                self.job_description + " " + str(self.package) + " " + self.required_skills + " " + str(self.min_CPI) + " " + 
                str(self.selection_process) + " " + self.other_details)


class TakenJob(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='quizes')
    applied_job = models.ForeignKey(Job, on_delete=models.CASCADE, null='TRUE',blank='TRUE' , related_name='applied_job')

    def __str__(self):
        return str(self.student.user)

class Submitter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(default=datetime.date.today)