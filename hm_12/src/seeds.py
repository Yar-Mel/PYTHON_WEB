import random

import requests
from faker import Faker
from datetime import date, timedelta

fake = Faker()

api_url = "http://localhost:8000/contacts/create"

current_date = date.today()

start_date = current_date - timedelta(days=10)
end_date = current_date + timedelta(days=10)

num_fake_contacts = 10

access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdHJpbmdAdGVzdCIsImV4cCI6MTY5NjA2NzM5MCwic2NvcGUiOiJhY2Nlc3NfdG9rZW4ifQ.7yJ8fZ4F7q2O6-sQRBw-Ueawj-21BuJjuk-bHGSJR0I"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

for _ in range(num_fake_contacts):
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    phone_number = fake.phone_number()
    birth_date = current_date + timedelta(days=random.randint(-10, 10))
    additional_info = fake.text()

    birth_date_str = birth_date.isoformat()
    contact_data = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone_number": phone_number,
        "birth_date": birth_date_str,
        "additional_info": additional_info,
    }

    response = requests.post(api_url, json=contact_data, headers=headers)

    if response.status_code == 200:
        print(f"Create: {first_name} {last_name}")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
