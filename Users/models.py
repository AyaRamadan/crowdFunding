from django.db import models

class Users(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	email=models.EmailField(editable=False)
	password=models.CharField(max_length=255)
	phone=models.IntegerField()
	Img=models.CharField(max_length=255)
	class Meta:
		db_table = "Users"

class User_optional_Info(models.Model):
	BirthDate=models.DateField(auto_now=False, auto_now_add=False,null=True)
	faceBook=models.URLField(null=True)
	country=models.CharField(max_length=100,null=True)
	user=models.ForeignKey('Users',on_delete=models.CASCADE)
	class Meta:
		db_table = "User_optional_Info"
