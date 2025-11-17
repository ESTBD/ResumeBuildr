from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CVform
from .serializers import CVformSerializer

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
                achievements += 'Name: ' + achievement.get("achievement_name") + ' '
                achievements += 'Time: ' + achievement.get("achievement_time") + ' '

        if contacts_data: 
            contacts = "Contacts: "

            for contact in contacts_data:
                contacts += "Platform: " + contact.get("platform_name") + ' '
                contacts += "Link: " + contact.get("profile_link") + ' '

        if educations_data: 
            educations = "Educations: "

            for education in educations_data:
                educations += "School/College: " + education.get("schoolname") + ' '
                educations += "Degree: " + education.get("degree") + ' '
                educations += "Start: " + education.get("starttime") + ' '
                educations += "End: " + education.get("endtime") + ' '
                educations += "Result: " + education.get("result_type") + "Score: " + education.get("score") + ' '

        if experiences_data: 
            experiences = "Experiences: "

            for experience in experiences_data:
                experiences += "Company: " + experience.get("company") + ' '
                experiences += "Role: " + experience.get("role") + ' '
                experiences += "Start: " + experience.get("job_starttime") + ' '
                experiences += "End: " + experience.get("job_endtime") + ' '
                experiences += "Description: " + experience.get("description") + ' ' 

        if projects_data: 
            projects = "Experiences: "

            for project in projects_data:
                projects += "Company: " + project.get("project_name") + ' '
                projects += "Role: " + project.get("project_link") + ' '
                projects += "Start: " + project.get("project_starttime") + ' '
                projects += "End: " + project.get("project_endtime") + ' '
                projects += "Description: " + project.get("project_description") + ' '

        if skills_data:
            skills = "Skills: "

            for skill in skills_data:
                skills += "Skills: " + skill.get("skills") + ' '


        # API response 
        response_data = {
            "prompt": "Make a CV for using following information "
            f"Name: {cvform.firstname} {cvform.lastname} "
            f"Email address: {cvform.email} "
            f"Home address: {cvform.address} "
            f"Current work: {cvform.jobtitle} "
            f"Achievements: {achievements}"
            f"Contacts: {contacts}"
            f"Educations: {education}" 
            f"Experiences: {experiences}"
            f"Projects: {projects}"
            f"Skills: {skills}" 
        }

        return Response(response_data, status=201)