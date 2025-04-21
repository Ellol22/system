from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Student, Doctor

@api_view(['POST'])
def api_sign_up(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')
    user_type = data.get('user_type')
    national_id = data.get('national_id')
    email = data.get('email')
    mobile = data.get('mobile')
    name = data.get('name')

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username is already taken.'}, status=status.HTTP_400_BAD_REQUEST)

    if user_type == '2':  # Student
        try:
            student = Student.objects.get(national_id=national_id)
            if student.user:
                return Response({'error': 'This national ID is already registered with a Student account.'}, status=status.HTTP_400_BAD_REQUEST)
            
            user = User.objects.create_user(username=username, password=password, email=email, first_name=name)
            student.user = user
            student.mobile = mobile
            student.save()

            return Response({'message': 'Student account created successfully.'}, status=status.HTTP_201_CREATED)

        except Student.DoesNotExist:
            return Response({'error': 'National ID not found in the student database.'}, status=status.HTTP_404_NOT_FOUND)

    elif user_type == '1':  # Doctor
        try:
            doctor = Doctor.objects.get(national_id=national_id)
            if doctor.user:
                return Response({'error': 'This national ID is already registered with a Doctor account.'}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create_user(username=username, password=password, email=email, first_name=name)
            doctor.user = user
            doctor.mobile = mobile
            doctor.save()

            return Response({'message': 'Doctor account created successfully.'}, status=status.HTTP_201_CREATED)

        except Doctor.DoesNotExist:
            return Response({'error': 'National ID not found in the doctor database.'}, status=status.HTTP_404_NOT_FOUND)

    return Response({'error': 'Invalid user_type. Must be "1" for Doctor or "2" for Student.'}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def api_log_in(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        return Response({'message': 'Login successful.'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid username or password.'}, status=status.HTTP_401_UNAUTHORIZED)
