from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('methods/', views.methods, name='methods'),
    path('about/', views.about, name='about'),
    path('appointment/', views.appointment, name='appointment'),
    path('success_appointment/', views.success_appointment, name='success_appointment'),
    path('methods/diagnose_methods', views.diagnose_methods, name='diagnose_methods'),
    path('methods/healing_methods', views.healing_methods, name='healing_methods'),
    path('methods/quick_methods', views.quick_methods, name='quick_methods'),
    path('methods/quick_methods/aesthetic_gynecology', views.aesthetic_gynecology, name='aesthetic_gynecology'),
    path('methods/quick_methods/hysteroscopy', views.hysteroscopy, name='hysteroscopy'),
    path('methods/quick_methods/laparatomy', views.laparatomy, name='laparatomy'),
    path('methods/quick_methods/laparoscopy', views.laparoscopy, name='laparoscopy'),
    path('methods/quick_methods/radio_wave_treatment', views.radio_wave_treatment, name='radio_wave_treatment'),
    path('methods/quick_methods/vaginoplastiki', views.vaginoplastiki, name='vaginoplastiki'),
    path('methods/quick_methods/urinary_incontinence', views.urinary_incontinence, name='urinary_incontinence'),
    path('methods/quick_methods/vulvectomy', views.vulvectomy, name='vulvectomy'),
    path('methods/diagnose_methods/colposcopy', views.colposcopy, name='colposcopy'),
    path('methods/diagnose_methods/office_hysteroscopy', views.office_hysteroscopy, name='office_hysteroscopy'),
    path('methods/healing_methods/HPV_treatment', views.HPV_treatment, name='HPV_treatment'),
    path('methods/healing_methods/postanovka_MVS', views.postanovka_MVS, name='postanovka_MVS'),
    path('methods/healing_methods/treatment_infections', views.treatment_infections, name='treatment_infections'),
]
