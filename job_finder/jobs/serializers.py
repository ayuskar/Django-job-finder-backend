from rest_framework import serializers
from .models import  Job, JobApplication
from users.models import Profile
#Profile serializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name', 'skills', 'experience']
#Job serializer
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['title', 'location', 'salary', 'description', 'created_by']
#JobApplication serializer
class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ['job', 'applicant', 'applied_on']
