from rest_framework import serializers
from material.models import Material, Course, PastQuestion, Department



class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ["url", "course", "title", "comment","upload_on","file", "code", "flag_url", "department_name", "download_url"]
        
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields= ["url", "code", "title", "info", "materials"]


class DepartmentCoursesSerializer(serializers.ModelSerializer):
    course_set = CourseSerializer(many=True)
    class Meta:
        model = Department
        fields = "__all__"
        
    def get_courses(self, obj):
      return obj.course_set.all()
        
