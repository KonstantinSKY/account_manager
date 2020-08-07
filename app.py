# Account manager

from services import Service

Service.get_all_from_db()
print(Service.services)

serv = Service({
    "name": "LinkedIn",
    "url": "https://www.linkedin.com",
    "description": "test_description LinkedIn"
})

print(Service.services)
print(serv)
