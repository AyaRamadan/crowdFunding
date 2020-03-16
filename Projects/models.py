from django.db import models
from Users.models import Users

class Categories(models.Model):
	name=models.CharField(max_length=100)
	

class Projects(models.Model):
	Title=models.CharField(max_length=100)
	Details=models.TextField()
	target=models.IntegerField()
	start_date=models.DateField(auto_now=False, auto_now_add=False)
	end_date=models.DateField(auto_now=False, auto_now_add=False)
	report=models.IntegerField(null=True)
	featured=models.BooleanField(null=True)
	user=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='UserID')
	category=models.ForeignKey('Categories',on_delete=models.CASCADE)
	tags = models.ManyToManyField('Tags',through='project_tags')
	donations=models.ManyToManyField(Users, through='user_donations',related_name='UserDonations')
	class Meta:
		db_table = "Projects"
	

class Pictures(models.Model):
	Path=models.CharField(max_length=255)
	project=models.ForeignKey('Projects',on_delete=models.CASCADE)
	class Meta:
		db_table = "Project_Pictures"

class Tags(models.Model):
	name=models.CharField(max_length=255)
	class Meta:
		db_table = "Tags"

class Rates(models.Model):
	rate=models.DecimalField(max_digits=2,decimal_places=1)
	project=models.ForeignKey('Projects',on_delete=models.CASCADE)
	user=models.ForeignKey(Users,on_delete=models.CASCADE)
	class Meta:
		db_table = "Project_Rates"

class Comments(models.Model):
	body=models.TextField()
	report=models.IntegerField()
	project=models.ForeignKey('Projects',on_delete=models.CASCADE)
	user=models.ForeignKey(Users,on_delete=models.CASCADE)
	class Meta:
		db_table = "Project_Comments"

class project_tags(models.Model):
	tag=models.ForeignKey('Tags',on_delete=models.CASCADE)
	project=models.ForeignKey('Projects',on_delete=models.CASCADE)
	class Meta:
		unique_together =['tag','project']
		db_table = "project_tags"


class user_donations(models.Model):
	user=models.ForeignKey(Users,on_delete=models.CASCADE)
	project=models.ForeignKey('Projects',on_delete=models.CASCADE)
	Amount=models.IntegerField()
	class Meta:
		unique_together =['user','project']
		db_table = "User_Donations"
