from typing import Any
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Employee, EmployeeWorkSchedule


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = (
            'id', 
            'id_num', 
            'username',  
            'phone_number', 
            'email', 
            'department',)


class EmployeeWorkScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeWorkSchedule
        fields = (
            'id', 
            'employee_id', 
            'employee_work_schedule_day', 
            'employee_work_schedule_day_period',)


class UserRegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=Employee.objects.all())])

    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Employee
        fields = ['username', 'email', 'password', 'password2', ]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    # def save(self, request):
    def save(self, *args, **kwargs):
        user = Employee(
            email=self.validated_data['email'],
            name=self.validated_data['username'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'})

        user.set_password(password)
        user.save()
        # user.user_permissions.set(['is_active'], True)
        return user
