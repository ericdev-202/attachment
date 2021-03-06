from django.urls import path
from django.conf.urls import url, include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import peer1, peer2, peer


urlpatterns = [
    #video call urls
    path('peer/', peer, name='peer'),
    path('peer1/', peer1, name='peer1'),
    path('peer2/', peer2, name='peer2'),

    path('video/',views.lecturerpeer,name='lecturerpeer'),
    path('studentvideo/',views.studentpeer,name='studentpeer'),
    path('supervisorvideo/',views.supervisorpeer,name='supervisorpeer'),

    #login and register urls
    path('l/',views.lindex,name='index'),
    path('',views.login_view, name='login_view'),
    path('register/',views.register, name='register'),
    path('Supervisorregister/',views.Supervisorregister, name='supervisor_register'),
    path('Studentregister/',views.Studentregister, name='student_register'),
    path('logout/', views.logout_user, name="logout"),
    # path('adminpage/', views.hod, name='adminpage'),
    
    #lecturer urls
    path('lecturer_page/',views.lecturer,name='lecturer'),
    path('viewstudent/',views.viewallstudent,name='allstudent'),
    # path('viewAssessment/',views.viewallassess,name='viewallAssessment'),
    path('viewsupervisorassess/',views.supervisorassessment,name='viewsupervisorassess'),
    path('lectass/',views.lecturerassement,name='viewall'),
    path('viewcompanydetails/',views.viewCompanydetails,name='allcompanydetails'),
    path('editview/<int:id>', views.getAssess),
    path('logbookdetails/',views.logbookdetails,name='logbookdetails'),
    path('viewlog/<str:regno>',views.logbookview),
    path('reportview/',views.reportview,name='reportviews'),
    path('assessed/',views.showassessed,name='assessed'),
    path('lecassess/<int:id>', views.LecAssess),  
    path('lecupdate/<int:id>', views.LecUpdate), 
    path('assessview/<int:id>',views.viewassess),
 




    #students url
    # path('add',views.add),
    path('viewlecassess/<int:id>',views.viewassess),
    path('companydetails/',views.compdet,name='companydetails'),
    path('sky/',views.skytry),
    path('student/',views.student,name='student'),
    path('student_det/',views.addStudent,name='new_student'),
    path('editstudent/<int:id>',views.editstudent),
    path('updatestudent/<int:id>',views.updatestudent),
    path('elogbook/',views.elogbook,name='logbook'),
    path('editlog/<int:id>',views.editlog),
    path('editcompany/<int:id>',views.editcompany),
    path('updatecompany/<int:id>',views.updatecompany),
    path('updatelog/<int:id>',views.updatelog),
    path('deletelogbook',views.deletelogbook,name='deletelogbook'),
    path('deletecompany',views.deletecompany,name='deletecompany'),
    path('deletereport',views.deletereport,name='deletereport'),
    path('deletestudentdetails',views.deletestudentdetails,name='deletestudentdetails'),
    path('new_entry',views.elogbook_entry,name='elogbook'),
    path('view/',views.ViewStudent,name='viewstudent'),
    path('upload/',views.model_form_upload,name='report'),
    path('view_report/',views.report,name='view_report'), 
    path('company/',views.addCompany,name='companyde'),
    path('viewCompany/',views.viewCompany,name='ViewCompany'), 
    path('editcompany/<int:id>',views.editcompany),
    path('updatecompany/<int:id>',views.updatecompany),



    #suprvisor urls
    # path('',views.student),
    path('companystudent/',views.companystudent,name='compstudent'),
    path('viewlogbook/',views.Logbook,name="viewlogbooks"),
    path('log/<str:regno>',views.ViewLogbook),
    path('assessment/',views.viewassessment,name='assess'),
    path('assess/<int:id>',views.view,name="viewassess"),
    path('supervisor_page/',views.supervisor,name='supervisors'),
    path('studentdetails', views.index,name='details'),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    # path('studentcmnyfilter/',views.filteredcompany,name='stfilcom')
    # path('delete/<int:id>', views.destroy),  


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)