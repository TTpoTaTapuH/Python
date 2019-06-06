from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from mainApp.views import index, doctors, register, profile, profile_data, profile_patient, profile_medcard
from mainApp.views import profile_analyse, test, uslugi, profile_draft, profile_to_priem, profile_priems, add_draft, info_doctor, write_reception, del_draft
app_name='mainApp'
urlpatterns = [
    path('', index, name='index'),
    path('registration/', register, name='register'),
    path('doctors/<int:reception_id>/<int:doctor_id>/', write_reception, name='write_reception'),
    path('doctor/<int:doctor_id>/', info_doctor, name='info_doctor'),
    path('doctor/', doctors, name='doctor'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', profile, name='profile'),
    path('profile/data/', profile_data, name='profile_data'),
    path('profile/patient/', profile_patient, name='profile_patient'),
    path('profile/medcard/', profile_medcard, name='profile_medcard'),
    path('profile/analyse/', profile_analyse, name='profile_analyse'),
    path('profile/draft/', profile_draft, name='profile_draft'),
    path('profile/to_priem/', profile_to_priem, name='profile_to_priem'),
    path('profile/priems/', profile_priems, name='profile_priems'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('uslugi/<int:service_id>/', add_draft, name='add_draft'),
    path('profile/del_draft/<int:draft_id>/', del_draft, name='del_draft'),
    path('uslugi/', uslugi, name='uslugi'),
    path('test/', test),
    #path('profile/', ),
]