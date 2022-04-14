from django.db import models

class Registration(models.Model):
	idno = models.TextField(default="")
	fname = models.TextField(default="")
	mname = models.TextField(default="")
	sname = models.TextField(default="")
	bdate = models.TextField(default="")
	address = models.TextField(default="")
	contactno = models.TextField(default="")
	status = models.TextField(default="pending")