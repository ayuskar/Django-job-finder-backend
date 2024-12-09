from django.contrib.auth.models import User
from .models import Profile, Job, JobApplication
from .serializers import JobSerializer, ProfileSerializer, JobApplicationSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework import filters 

class JobListView(ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [filters.SearchFilter]  
    search_fields = ['title', 'location', 'salary']  

@api_view(['POST'])
def applyforjob(request, job_id):
    job = Job.objects.get(id=job_id)
    application, created = JobApplication.objects.get_or_create(job=job, applicant=request.user)
    if created:
        return Response({'message': 'Application successful!'})
    return Response({'message': 'You have already applied for this job.'}, status=400)

class JobCreateView(CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAdminUser]

class JobUpdateView(UpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAdminUser]

class JobDeleteView(DestroyAPIView):
    queryset = Job.objects.all()
    permission_classes = [IsAdminUser]

@api_view(['GET'])
def viewapplications(request, job_id):
    if not request.user.is_staff:
        return Response({'error': 'Permission denied.'}, status=403)
    
    job = Job.objects.get(id=job_id)
    applications = JobApplication.objects.filter(job=job)
    serializer = JobApplicationSerializer(applications, many=True)
    return Response(serializer.data)
