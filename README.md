# django-jwt
A Django simple Application with Authentication

In this repo the_site is project, having two apps 'auth' and 'home'

Steps how JWT based authentication is implemented
1. pip install djangorestframework_simplejwt

2. Settings.py
```
INSTALLED_APPS = [
    'rest_framework',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
```

3. urls.py
```
In the_site.auth.urls
    path('hello/', views.HelloView.as_view(), name='hello'),
In the_site.urls
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
```

4. In auth.views.py
```
from django.views import View

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
```

5. Do below steps:
  1. python manage.py migrate
  2. python manage.py createsuperuser
  3. pip3 install httpie
  4. Generate Tokens by visiting webpage: http://127.0.0.1:8000/api/token/
      OR from cli do  ```curl -u username http://127.0.0.1:8000/api/token/```
  5. http http://127.0.0.1:8000/auth/hello/ "Authorization: Bearer <access-token>"
<img width="1440" alt="Screenshot 2021-07-22 at 19 03 22" src="https://user-images.githubusercontent.com/41416816/126687146-419f27d9-acc5-4b46-b30f-9fad81d8457d.png">

  6. After 5 minutes, access token will expire. We can get new access token using refresh token
  http post http://127.0.0.1:8000/api/token/refresh/ refresh=<refresh-token>
  <img width="1440" alt="Screenshot 2021-07-22 at 19 05 02" src="https://user-images.githubusercontent.com/41416816/126687356-f0b2c21f-dfc9-480b-bfdc-a4bfe5770b00.png">

  
