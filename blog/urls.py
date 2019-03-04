from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
    Directory: C:\Users\Public\Desktop\django\blog


Mode                LastWriteTime         Length Name                                                                                                                                          
----                -------------         ------ ----                                                                                                                                          
d-----       04.03.2019     17:53                migrations                                                                                                                                    
d-----       04.03.2019     17:54                __pycache__                                                                                                                                   
-a----       04.03.2019     17:54             87 admin.py                                                                                                                                      
-a----       04.03.2019     17:51             88 apps.py                                                                                                                                       
-a----       04.03.2019     17:53            545 models.py                                                                                                                                     
-a----       04.03.2019     17:51             63 tests.py                                                                                                                                      
-a----       04.03.2019     19:34              0 urls.py                                                                                                                                       
-a----       04.03.2019     17:51             66 views.py                                                                                                                                      
-a----       04.03.2019     17:51              0 __init__.py                                                                                                                                   


