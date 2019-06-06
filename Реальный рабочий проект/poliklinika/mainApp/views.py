from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from django.db.models import Q
import datetime
from .models import Doctor, Medicina, Service, TimeReception, Reception, Service, Draft, Analysis, Patient, OutPatientCard, Treatment

# Create your views here.
def index(request):
    #medicina = Medicina.objects.all()
    #context = {'medicina': medicina, 'title': 'Поликлиника'}
    return render(request, 'mainApp/index.html')

def doctors(request):
    doctor = Doctor.objects.all()
    med = {
        'nevrop':Medicina.objects.get(name='Невропатология'),
        'androl':Medicina.objects.get(name='Андрология'),
        'aneste':Medicina.objects.get(name='Анестезиология'),
        'venero':Medicina.objects.get(name='Венерология'),
        'gastro':Medicina.objects.get(name='Гастроэнтерология'),
        'gineko':Medicina.objects.get(name='Гинекология'),
        'kardio':Medicina.objects.get(name='Кардиология'),
        'logope':Medicina.objects.get(name='Логопедия'),
        'mammol':Medicina.objects.get(name='Маммология'),
        'nevrol':Medicina.objects.get(name='Неврология'),
        'neuroh':Medicina.objects.get(name='Нейрохирургия'),
        'otolor':Medicina.objects.get(name='Отоларингология'),
        'oftalm':Medicina.objects.get(name='Офтальмология'),
        'pediat':Medicina.objects.get(name='Педиатрия'),
        'prokto':Medicina.objects.get(name='Проктология'),
        'terapi':Medicina.objects.get(name='Терапия'),
        'urolog':Medicina.objects.get(name='Урология'),
        'hirurg':Medicina.objects.get(name='Хирургия'),
        'endokr':Medicina.objects.get(name='Эндокринология')
    }
    context = {
        'title':'Врачи',
        'doc_nevrop' : Doctor.objects.filter(medicina=med['nevrop']),
        'doc_androl' : Doctor.objects.filter(medicina=med['androl']),
        'doc_aneste' : Doctor.objects.filter(medicina=med['aneste']),
        'doc_venero' : Doctor.objects.filter(medicina=med['venero']),
        'doc_gastro' : Doctor.objects.filter(medicina=med['gastro']),
        'doc_gineko' : Doctor.objects.filter(medicina=med['gineko']),
        'doc_kardio' : Doctor.objects.filter(medicina=med['kardio']),
        'doc_logope' : Doctor.objects.filter(medicina=med['logope']),
        'doc_mammol' : Doctor.objects.filter(medicina=med['mammol']),
        'doc_nevrol' : Doctor.objects.filter(medicina=med['nevrol']),
        'doc_neuroh' : Doctor.objects.filter(medicina=med['neuroh']),
        'doc_otolor' : Doctor.objects.filter(medicina=med['otolor']),
        'doc_oftalm' : Doctor.objects.filter(medicina=med['oftalm']),
        'doc_pediat' : Doctor.objects.filter(medicina=med['pediat']),
        'doc_prokto' : Doctor.objects.filter(medicina=med['prokto']),
        'doc_terapi' : Doctor.objects.filter(medicina=med['terapi']),
        'doc_urolog' : Doctor.objects.filter(medicina=med['urolog']),
        'doc_hirurg' : Doctor.objects.filter(medicina=med['hirurg']),
        'doc_endokr' : Doctor.objects.filter(medicina=med['endokr'])
    }
    return render(request, 'mainApp/doctors.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Акканут создан для {username}!')
            return redirect("/login")
    else:
        form = UserRegisterForm()
        return render(request, 'registration/registration.html', {'form': form})

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile/profile.html')
    else:
        return redirect("/login")

def profile_data(request):
    if request.user.is_authenticated:
        return render(request, 'profile/profile_data.html')
    else:
        return redirect("/login")

def profile_patient(request):
    if request.user.is_authenticated:
        return render(request, 'profile/profile_patient.html')
    else:
        return redirect("/login")

def profile_medcard(request):
    if request.user.is_authenticated:
        return render(request, 'profile/profile_patient_card.html')
    else:
        return redirect("/login")

def profile_analyse(request):
    if request.user.is_authenticated:
        an_user = Patient.objects.filter(user = request.user)
        analyse = ""
        if not an_user:
            return render(request, 'profile/profile_analyse.html', {'analyse': an_user})
        else:
            an_user = Patient.objects.get(user = request.user)
            card = OutPatientCard.objects.filter(patient=an_user)
            if card:
                card = OutPatientCard.objects.get(patient=an_user)
                analyse = Analysis.objects.filter(out_patient_card=card)
                return render(request, 'profile/profile_analyse.html', {'analyse': analyse})
            else:    
                return render(request, 'profile/profile_analyse.html', {'analyse': card})
    else:
        return redirect("/login")

def uslugi(request):
    med = {
        'nevrop':Medicina.objects.get(name='Невропатология'),
        'androl':Medicina.objects.get(name='Андрология'),
        'aneste':Medicina.objects.get(name='Анестезиология'),
        'venero':Medicina.objects.get(name='Венерология'),
        'gastro':Medicina.objects.get(name='Гастроэнтерология'),
        'gineko':Medicina.objects.get(name='Гинекология'),
        'kardio':Medicina.objects.get(name='Кардиология'),
        'logope':Medicina.objects.get(name='Логопедия'),
        'mammol':Medicina.objects.get(name='Маммология'),
        'nevrol':Medicina.objects.get(name='Неврология'),
        'neuroh':Medicina.objects.get(name='Нейрохирургия'),
        'otolor':Medicina.objects.get(name='Отоларингология'),
        'oftalm':Medicina.objects.get(name='Офтальмология'),
        'pediat':Medicina.objects.get(name='Педиатрия'),
        'prokto':Medicina.objects.get(name='Проктология'),
        'terapi':Medicina.objects.get(name='Терапия'),
        'urolog':Medicina.objects.get(name='Урология'),
        'hirurg':Medicina.objects.get(name='Хирургия'),
        'endokr':Medicina.objects.get(name='Эндокринология')
    }
    context = {
        'title':'Услуги',
        'doc_nevrop' : Service.objects.filter(medicina=med['nevrop']),
        'doc_androl' : Service.objects.filter(medicina=med['androl']),
        'doc_aneste' : Service.objects.filter(medicina=med['aneste']),
        'doc_venero' : Service.objects.filter(medicina=med['venero']),
        'doc_gastro' : Service.objects.filter(medicina=med['gastro']),
        'doc_gineko' : Service.objects.filter(medicina=med['gineko']),
        'doc_kardio' : Service.objects.filter(medicina=med['kardio']),
        'doc_logope' : Service.objects.filter(medicina=med['logope']),
        'doc_mammol' : Service.objects.filter(medicina=med['mammol']),
        'doc_nevrol' : Service.objects.filter(medicina=med['nevrol']),
        'doc_neuroh' : Service.objects.filter(medicina=med['neuroh']),
        'doc_otolor' : Service.objects.filter(medicina=med['otolor']),
        'doc_oftalm' : Service.objects.filter(medicina=med['oftalm']),
        'doc_pediat' : Service.objects.filter(medicina=med['pediat']),
        'doc_prokto' : Service.objects.filter(medicina=med['prokto']),
        'doc_terapi' : Service.objects.filter(medicina=med['terapi']),
        'doc_urolog' : Service.objects.filter(medicina=med['urolog']),
        'doc_hirurg' : Service.objects.filter(medicina=med['hirurg']),
        'doc_endokr' : Service.objects.filter(medicina=med['endokr'])
    }
    return render(request, 'mainApp/uslugi.html', context)

def test(request):
    return render(request, 'test.html')


def profile_draft(request):
    if request.user.is_authenticated:
        drafts = Draft.objects.filter(user=request.user).order_by("date")
        context = {'drafts':drafts}
        return render(request, 'profile/profile_draft.html', context)
    else:
        return redirect("/login")

def profile_to_priem(request):
    if request.user.is_authenticated:
        reception = Reception.objects.filter(patient=request.user)
        context = {'reception':reception}
        return render(request, 'profile/profile_to_priem.html', context)
    else:
        return redirect("/login")

def profile_priems(request):
    if request.user.is_authenticated:
        an_user = Patient.objects.filter(user = request.user)
        if not an_user:
            return render(request, 'profile/profile_priems.html', {'treatment': an_user})
        else:
            an_user = Patient.objects.get(user = request.user)
            card = OutPatientCard.objects.filter(patient=an_user)
            if card:
                card = OutPatientCard.objects.get(patient=an_user)
                treatment = Treatment.objects.filter(patient_card=card)
                return render(request, 'profile/profile_priems.html', {'treatment': treatment})
            return render(request, 'profile/profile_priems.html', {'treatment': card})
    else:
        return redirect("/login")

def del_draft(request, draft_id):
    if not request.user.is_authenticated:
        return redirect("/login")
    draft = Draft.objects.get(id=draft_id)
    if draft :
        if request.user.is_authenticated:
            text = 'Вы записаны на приём. Вы можете посмотреть информацию о приёме в профиле.'
            draft.delete()
            return redirect("/profile/draft/")
        else:
            return redirect("/login")
    else:
        return redirect("/profile/draft/")

def add_draft(request, service_id):
    if not request.user.is_authenticated:
        return redirect("/login")
    service = Service.objects.get(id=service_id)
    text = ''
    if request.method == "POST":
        if request.user.is_authenticated:
            text = 'Вы записаны на приём. Вы можете посмотреть информацию о приёме в профиле.'
            draft = Draft()
            draft.user = request.user
            draft.service = service
            draft.save()
            return redirect("/uslugi")
        else:
            return redirect("/login")
    else:
        return render(request,'mainApp/add_draft.html',{'service':service})

def info_doctor(request, doctor_id):
    now = datetime.datetime.now()
    doctor = Doctor.objects.get(id=doctor_id)
    q=Q(doctor=doctor_id) & Q(work_day=now.date()) & Q(time__gte=now.time()) & Q(status="Free") | Q(doctor=doctor_id) & Q(work_day__gt=now.date()) & Q(status="Free")
    #time1 = TimeReception.objects.filter(doctor=doctor_id, work_day=now.date(), time__gte=now.time(), status="Free")
    #time2 = TimeReception.objects.filter(doctor=doctor_id, work_day__gt=now.date(), status="Free").order_by("work_day","time")
    time = TimeReception.objects.filter(q).order_by("work_day","time")
    return render(request, 'mainApp/info_doctor.html',{'doctor':doctor,'time':time})

def write_reception(request, reception_id, doctor_id):
    #user = User.objects.get(id=user_id)
    if not request.user.is_authenticated:
        return redirect("/login")
    treception = TimeReception.objects.get(id=reception_id)
    doctor = Doctor.objects.get(id=doctor_id)
    text = ''
    if request.method == "POST":
        if request.user.is_authenticated:
            if treception.status == "Busy":
                text = 'Это время уже занято! Запишитесь на другое время.'
            else:
                text = 'Вы записаны на приём. Вы можете посмотреть информацию о приёме в профиле.'
                treception.status = "Busy"
                treception.save()
                reception = Reception()
                reception.date=treception.work_day
                reception.time=treception.time
                reception.status = 'Принят'
                reception.doctor = doctor
                reception.patient = request.user
                reception.save()
            return render(request,'mainApp/succes_reception.html',{'text':text})
        else:
            return redirect("/login")
    else:
        return render(request,'mainApp/write_reception.html',{'treception':treception})