### CreateDjango
```shell
$ django-admin startproject <project_name>
$ cd <project_name>
$ django-admin startapp <app_name>
```
### Urls
- Edit <project_name>/settings.py/INSTALLED_APPS = [...<project_name>]
- Edit <app_name>/urls.py/
- 引用自当前app中的views.py中的函数
```python
from django.urls import path
from . import views

urlpatterns = [
    path('weaks/', views.index),
]

```

### Start 
```shell
$ python manage.py runserver
```

