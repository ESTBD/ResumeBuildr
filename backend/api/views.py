from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
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
            achievements = "Achievements: \n"

            for achievement in achievements_data:
                achievements += 'Name: ' + achievement.get("achievement_name") + ' '
                achievements += 'Time: ' + achievement.get("achievement_time")
                achievements += '\n'

        # API response 
        response_data = {
            "prompt": "Make a CV for using following information "
            f"Name: {cvform.firstname} {cvform.lastname} "
            f"Email address: {cvform.email} "
            f"Home address: {cvform.address} "
            f"Current work: {cvform.jobtitle} "
            f"Achievements: {achievements}"
        }

        return Response(response_data, status=201)