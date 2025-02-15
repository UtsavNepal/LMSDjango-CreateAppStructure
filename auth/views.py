# from django.contrib.auth import authenticate
# from django.http import JsonResponse
# from django.views import View
# from django.contrib.auth.hashers import check_password
# from authentication.models import UserSignup
# import uuid
# import json

# class UserSignupView(View):
#     def post(self, request):
#         try:
#             data = json.loads(request.body)
#             username = data.get("username")
#             email = data.get("email")
#             password = data.get("password")

#             if UserSignup.objects.exists():
#                 return JsonResponse({"error": "Only one librarian can be created."}, status=400)

#             user = UserSignup.objects.create_user(username=username, email=email, password=password)
#             return JsonResponse({
#                 "message": "User created successfully",
#                 "username": user.username,
#                 "email": user.email,
#                 "access_token": user.access_token
#             }, status=201)

#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=400)


# class UserLoginView(View):
#     def post(self, request):
#         try:
#             data = json.loads(request.body)
#             email = data.get("email")
#             password = data.get("password")

#             user = UserSignup.objects.filter(email=email).first()

#             if user and check_password(password, user.password):
#                 return JsonResponse({
#                     "message": "Login successful",
#                     "username": user.username,
#                     "access_token": user.access_token
#                 }, status=200)

#             return JsonResponse({"error": "Invalid email or password"}, status=401)

#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=400)
