from django.test import TestCase
from requests import get, post

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InRlc3QxQHRlc3QucnUiLCJleHAiOjE2ODU1MTg4MTEsImVtYWlsIjoidGVzdDFAdGVzdC5ydSJ9.E1fvF16z8z-9IVFoBBmRO2HCDly3RbQXZPLBzPDWyJ8"
r = get(
        url='http://localhost:8000/api/get_all_users/',
        headers={"Authorization": f"Bearer {token}"}
    )


# data = {
#     'title': 'MEGATEST',
#     'date_create': '2023-05-31'
# }
# r = post(
#     url='http://localhost:8000/api/providers/',
#     data=data,
#     headers={"Authorization": f"Bearer {token}"}
# )
print(r.json())