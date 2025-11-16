from rest_framework import serializers
from .models import CVform, Achievements, Contact, Education, Experience, Project, Skill


class AchievementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Achievements
        fields = ["achievement_name", "achievement_time"]
        extra_kwargs = {
            "achievement_name": {"required": False, "allow_null": True, "allow_blank": True},
            "achievement_time": {"required": False, "allow_null": True, "allow_blank": True},
        }

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ["platform_name", "profile_link"]
        extra_kwargs = {
            "platform_name": {"required": False, "allow_null": True, "allow_blank": True},
            "profile_link": {"required": False, "allow_null": True, "allow_blank": True},
        }

class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        fields = [
            "schoolname", 
            "degree", 
            "starttime", 
            "endtime", 
            "result_type", 
            "score"
        ]
        extra_kwargs = {
            "schoolname": {"required": False, "allow_null": True, "allow_blank": True},
            "degree": {"required": False, "allow_null": True, "allow_blank": True},
            "starttime": {"required": False, "allow_null": True, "allow_blank": True}, 
            "endtime": {"required": False, "allow_null": True, "allow_blank": True}, 
            "result_type": {"required": False, "allow_null": True, "allow_blank": True},
            "score": {"required": False, "allow_null": True, "allow_blank": True},
        }


class ExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Experience
        fields = [
            "company",
            "role",
            "job_starttime", 
            "job_endtime", 
            "description"
        ]
        extra_kwargs = {
            "company": {"required": False, "allow_null": True, "allow_blank": True},
            "role": {"required": False, "allow_null": True, "allow_blank": True},
            "job_starttime": {"required": False, "allow_null": True, "allow_blank": True}, 
            "job_endtime": {"required": False, "allow_null": True, "allow_blank": True}, 
            "description": {"required": False, "allow_null": True, "allow_blank": True},
        }


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = [
            "project_name", 
            "project_link", 
            "project_starttime", 
            "project_endtime", 
            "project_description"
        ]
        extra_kwargs = {
            "project_name": {"required": False, "allow_null": True, "allow_blank": True},
            "project_link": {"required": False, "allow_null": True, "allow_blank": True},
            "project_starttime": {"required": False, "allow_null": True, "allow_blank": True}, 
            "project_endtime": {"required": False, "allow_null": True, "allow_blank": True}, 
            "project_description": {"required": False, "allow_null": True, "allow_blank": True},
        }



class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ["skills"]
        extra_kwargs = {
            "skills": {"required": False, "allow_null": True, "allow_blank": True},
        }

class CVformSerializer(serializers.ModelSerializer):

    achievements = AchievementSerializer(many=True, required=False)
    contacts = ContactSerializer(many=True, required=False)
    educatiosn = EducationSerializer(many=True, required=False)
    experiences = ExperienceSerializer(many=True, required=False)
    projects = ProjectSerializer(many=True, required=False)
    skills = SkillSerializer(many=True, required=False)

    class Meta:
        model = CVform
        fields = "__all__"
                     
    def create(self, validated_data):

        achievements_data = validated_data.pop("achievements", [])
        contacts_data = validated_data.pop("contacts", [])
        educations_data = validated_data.pop("educations", [])
        experiences_data = validated_data.pop("experiences", [])
        projects_data = validated_data.pop("projects", [])
        skills_data = validated_data.pop("skills", []) 

        cvform = CVform.objects.create(**validated_data) 


        for a in achievements_data: 
            cvform.achievements.create(**a) # type: ignore

        for c in contacts_data:
            cvform.contacts.create(**c) # type: ignore

        for ed in educations_data:
            cvform.educations.create(**ed) # type: ignore

        for ex in experiences_data:
            cvform.experiences.create(**ex) # type: ignore

        for p in projects_data:
            cvform.projects.create(**p) # type: ignore

        for s in skills_data:
            cvform.skills.create(**s) # type: ignore 

        return cvform