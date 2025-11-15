from django.db import models
from phonenumber_field import modelfields


# CV form model

class CVform(models.Model):

# personal infos
    firstname = models.CharField(max_length=128, blank=False, null=False)
    lastname = models.CharField(max_length=128, blank=False, null=False) 
    email = models.EmailField(blank=False, null=False)
    phone = modelfields.PhoneNumber()
    address = models.CharField(max_length=256, blank=False, null=False)
    jobtitle = models.CharField(max_length=128, blank=False, null=False)


class Achievements(models.Model):

    achievement_name = models.CharField(max_length=128)
    achievement_time = models.CharField(max_length=64)
    cvform = models.ForeignKey(CVform, on_delete=models.CASCADE, related_name='achievements')

class Contact(models.Model):

    platform_name = models.CharField(max_length=128, null=True)
    profile_link = models.CharField(max_length=128, null=True) 
    cvform = models.ForeignKey(CVform, on_delete=models.CASCADE, related_name='contacts')


class Education(models.Model):

    RESULT_TYPE = [('C', 'cgpa'), ('G', 'gpa')]

    schoolname = models.CharField(max_length=128)
    degree = models.CharField(max_length=64)
    starttime = models.CharField(max_length=64)
    endtime = models.CharField(max_length=64)
    result_type = models.CharField(max_length=32, choices=RESULT_TYPE, default='C')
    score = models.IntegerField()
    cvform = models.ForeignKey(CVform, on_delete=models.CASCADE, related_name='educations')


class Experience(models.Model):

    company = models.CharField(max_length=128)
    role = models.CharField(max_length=128)
    job_starttime = models.CharField(max_length=64)
    job_endtime = models.CharField(max_length=64)
    description = models.TextField() 
    cvform = models.ForeignKey(CVform, on_delete=models.CASCADE, related_name='experiences')

class Project(models.Model):

    project_name = models.CharField(max_length=128)
    project_link = models.CharField(max_length=128)
    project_starttime = models.CharField(max_length=64)
    project_endtime = models.CharField(max_length=64)
    project_description = models.TextField() 
    cvform = models.ForeignKey(CVform, on_delete=models.CASCADE, related_name='projects')
    

class Skill(models.Model):

    skills = models.TextField()
    cvform = models.ForeignKey(CVform, on_delete=models.CASCADE, related_name='skills')


