from rest_framework import serializers
from .models import CVform, Achievements, Contact, Education, Experience, Project, Skill


class AchievementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Achievements
        fields = ["achievement_name", "achievement_time"]

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ["platform_name", "profile_link"]

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


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ["skills"]

class CVformSerializer(serializers.ModelSerializer):

    achievements = AchievementSerializer(many=True)
    contacts = ContactSerializer(many=True)
    educatiosn = EducationSerializer(many=True)
    experiences = ExperienceSerializer(many=True)
    projects = ProjectSerializer(many=True)
    skills = SkillSerializer(many=True)

    class Meta:
        model = CVform
        fields = "__all__"
                     
    def create(self, validated_data):

        achievements_data = validated_data.pop("achievements")
        contacts_data = validated_data.pop("contacts")
        educations_data = validated_data.pop("educations")
        experiences_data = validated_data.pop("experiences")
        projects_data = validated_data.pop("projects")
        skills_data = validated_data.pop("skills") 

        cvform = CVform.objects.create(**validated_data) 


        for a in achievements_data: 
            cvform.achievements.create(**a) # type: ignore

        for c in contacts_data:
            cvform.contacts.create(**c) # type: ignore

        for ed in educations_data:
            cvform.educations.create(**ed) # type: ignore

        for ex in experiences_data:
            cvform.experiences.create(**ed) # type: ignore

        for p in projects_data:
            cvform.projects.create(**p) # type: ignore

        for s in skills_data:
            cvform.skills.create(**s) # type: ignore