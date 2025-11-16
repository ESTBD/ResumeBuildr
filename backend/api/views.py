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

        # API response
        response_data = {
            "message": "Form retrieved!", 
            "Name": cvform.firstname + " " + cvform.lastname,
            "Mail": cvform.email, 
        #    "Mobile": cvform.phone, 
            "Address": cvform.address, 
            "Work": cvform.jobtitle,
            "Achievements": achievements_data, 
            "Contacts": contacts_data, 
            "Education": educations_data, 
            "Experiences": experiences_data, 
            "Projects": projects_data, 
            "Skills": skills_data,
        } 

        return Response(response_data, status=201)