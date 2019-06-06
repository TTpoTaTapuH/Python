from django.contrib import admin

# Register your models here.
from .models import Doctor, Patient, Analysis, Assistent, Contract, OutPatientCard
from .models import Cashier, MedRequest, Reception, RegistryClerk, MedSister, Treatment, WorkGrafic, Medicina, Service
from .models import TimeReception, Draft, Accountant, Report, Zavhoz
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Assistent)
admin.site.register(Contract)
admin.site.register(OutPatientCard)
admin.site.register(Cashier)
admin.site.register(MedRequest)
admin.site.register(Reception)
admin.site.register(RegistryClerk)
admin.site.register(MedSister)
admin.site.register(Treatment)
admin.site.register(Analysis)
admin.site.register(WorkGrafic)
admin.site.register(Medicina)
admin.site.register(Service)
admin.site.register(TimeReception)
admin.site.register(Draft)
admin.site.register(Accountant)
admin.site.register(Report)
admin.site.register(Zavhoz)