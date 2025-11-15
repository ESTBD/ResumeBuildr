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

    # def create(self, request, *args, **kwargs):
    #     obj_id = request.data.get('id')
    #     if not obj_id:
    #         return Response({"error": "Missing id"}, status=400)

    #     obj = CVform.objects.filter(id=obj_id).first()
    #     if not obj:
    #         return Response({"error": "Not found"}, status=404)
        
        # base CV request 
        # prompt = ( 
        #     f"Make a CV for a person with following details\n" 
        #     f"Name: {obj.firstname} {obj.lastname}\n" 
        #     f"Contact [Mail: {obj.email} | Phone: {obj.phone}]\n" 
        #     f"Platforms: {obj.platform_name} URL: {obj.profile_link}\n"
        #     f"Lives in {obj.address}\n"
        #     f"Wants to work as {obj.jobtitle}\n"
        # )

        # # add achievements if any
        # if obj.achievement_name and obj.achievement_time :
        #     prompt += (f"Achivements: \n{obj.achievement_name} in {obj.achievement_time}\n")

        # # add projects if any
        # if obj.project_name and obj.project_link and obj.project_starttime and obj.project_endtime and obj.project_description:
        #     prompt += (
        #         f"Projects worked in: \n"
        #         f"{obj.project_name}  URL: {obj.project_link}\n"
        #         f"from {obj.project_starttime} to {obj.project_endtime}\n"
        #         f"{obj.project_description}\n"
        #     )

        # # add skills if any
        # if obj.skills:
        #     prompt += (f"{obj.skills}\n") 

        # # add education if literate
        # if obj.schoolname and obj.degree and obj.starttime and obj.endtime and obj.result_type and obj.score:
        #     prompt += (
        #         f"Studied in {obj.schoolname} and has {obj.degree} joined in {obj.starttime} and passed in {obj.endtime}\n"
        #         f"Result: {obj.result_type} with {obj.score}\n"
        #     )
            
        # # add work history if experienced
        # if obj.company and obj.role and obj.description and obj.starttime and obj.endtime:
        #     prompt += (
        #         f"Worked in: {obj.company} as {obj.role} from {obj.job_starttime} to {obj.job_endtime}\n"
        #         f"{obj.description}\n"
        #     )
        
        # client = genai.Client() 

        # # send promopt to Gemini
        # response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt) 

        # return Response({"Generated_CV": response})



