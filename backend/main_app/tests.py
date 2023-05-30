from django.test import TestCase
from requests import get, post

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InRlc3QxQHRlc3QucnUiLCJleHAiOjE2ODU0MTU3NDAsImVtYWlsIjoidGVzdDFAdGVzdC5ydSJ9.i9TcoiqLKHslsC5CMw7EUx5bYLXZ9xq9XTI5FR73JFM"
# r = get(
#         url='http://127.0.0.1:8000/api/providers/contacts/provider_1/',
#         headers={"Authorization": f"Bearer {token}"}
#     )
# print(r.json())

data = {
    'title': 'TEST',
    'date_create': '2023-05-30',
    'created_by': 1
}
r = post(
    url='http://127.0.0.1:8000/api/providers/',
    data=data,
    headers={"Authorization": f"Bearer {token}"}
)
print(r.json())