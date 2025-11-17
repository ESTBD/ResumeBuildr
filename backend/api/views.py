from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
<<<<<<< HEAD
from .models import CVform
from .serializers import CVformSerializer 

from phonenumber_field.serializerfields import PhoneNumberField

from google import genai 


# CVform view
class CVformViewSet(viewsets.ModelViewSet):
    queryset = CVform.objects.all()    # all fields are available on api
    serializer_class = CVformSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data 
        
        achievements_data = validated_data.get("achievements", [])
        contacts_data = validated_data.get("contacts", []) 
        educations_data = validated_data.get("educations", [])
        experiences_data = validated_data.get("experiences", [])
        projects_data = validated_data.get("projects", []) 
        skills_data = validated_data.get("skills", []) 

        # Create object using serializer's create()
        cvform = serializer.save() 

        achievements = ""
        contacts = ""
        educations = ""
        experiences = ""
        projects = ""
        skills = ""

        if achievements_data : 
            achievements = "Achievements: "

            for achievement in achievements_data:
                achievements += f"Name: {achievement.get('achievement_name') or ''} "
                achievements += f"Time: {achievement.get('achievement_time') or ''} "

        if contacts_data: 
            contacts = "Contacts: "

            for contact in contacts_data:
                contacts += f"Platform: {contact.get('platform_name') or ''} "
                contacts += f"URL: {contact.get('profile_link') or ''} "
                
        if educations_data: 
            educations = "Educations: "

            for education in educations_data:
                educations += f"School/College: {education.get('schoolname') or ''} "
                educations += f"Degree: {education.get('degree') or ''} "
                educations += f"Start: {education.get('starttime') or ''} "
                educations += f"End: {education.get('endtime') or ''} "
                educations += f"Result: {education.get('result_type') or ''} "
                educations += f"Score: {education.get('score') or ''} "


        if experiences_data: 
            experiences = "Experiences: "

            for experience in experiences_data:
                experiences += f"Company: {experience.get("company") or ''} " 
                experiences += f"Role: {experience.get("role") or ''}"
                experiences += f"Start: {experience.get("job_starttime") or ''} "
                experiences += f"End: {experience.get("job_endtime") or ''} "
                experiences += f"Description: {experience.get("description") or ''} "

        if projects_data: 
            projects = "Projects: "

            for project in projects_data:
                projects += f"Project: {project.get("project_name") or ''} "
                projects += f"URL: {project.get("project_link") or ''} " 
                projects += f"Start: {project.get("project_starttime") or ''}"
                projects += f"End: {project.get("project_endtime") or ''} "
                projects += f"Description: {project.get("project_description") or ''} "  

        if skills_data:
            skills = "Skills: "

            for skill in skills_data:
                skills += f"Skills: {skill.get("skills") or ''} "  


        # API response 
        response_data = {
            "prompt": "Make a CV for using following information "
            f"Name: {cvform.firstname} {cvform.lastname} "
            f"Email address: {cvform.email} "
            f"Home address: {cvform.address} "
            f"Current work: {cvform.jobtitle} "
            f"Achievements: {achievements}"
            f"Contacts: {contacts}"
            f"Educations: {educations}" 
            f"Experiences: {experiences}"
            f"Projects: {projects}"
            f"Skills: {skills}" 
        }

        return Response(response_data, status=201)
=======

>>>>>>> feature/backend
