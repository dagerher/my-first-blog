from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

    Directory: C:\Users\Public\Desktop\django\blog


Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
d-----       04.03.2019     17:53                migrations                                                            
d-----       04.03.2019     20:22                static                                                                
d-----       04.03.2019     19:44                templates                                                             
d-----       04.03.2019     17:54                __pycache__                                                           
-a----       04.03.2019     17:54             87 admin.py                                                              
-a----       04.03.2019     17:51             88 apps.py                                                               
-a----       04.03.2019     20:48              0 forms.py                                                              
-a----       04.03.2019     17:53            545 models.py                                                             
-a----       04.03.2019     17:51             63 tests.py                                                              
-a----       04.03.2019     20:43           4750 urls.py                                                               
-a----       04.03.2019     20:41            491 views.py                                                              
-a----       04.03.2019     17:51              0 __init__.py                                                           


