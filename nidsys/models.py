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

class PreviousAddr(models.Model):
	regid = models.ForeignKey(Registration, default=None, on_delete=models.CASCADE)
	prevaddr = models.TextField(default=None, blank=False)
	fromdate = models.TextField(default=None, blank=False)
	todate = models.TextField(default=None, blank=False)

	class meta:
		db_table = 'previousaddr'
		verbose_name = 'Previous Addresses' 