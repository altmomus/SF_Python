from task_16_9_4_class import Volunteers

dvolunteers = [
    {
        "name": "Ivan",
        "surname": "Ivanov",
        "city": "Moscow",
        "status": "Volunteer"
    },
    {
        "name": "Alex",
        "surname": "Petrov",
        "city": "Rostov",
        "status": "Mentor"
    },
    {
        "name": "Aleksey",
        "surname": "Nikov",
        "city": "[CENSURED]",
        "status": "Guest"
    }
]

lvolunteers = []
for volunteer in dvolunteers:
    lvolunteers.append(Volunteers(volunteer.get('name'),
                                  volunteer.get('surname'),
                                  volunteer.get('city'),
                                  volunteer.get('status')
                                  )
                       )

i = 0
for volunteer in lvolunteers:
    i += 1
    print(f"Volunteer {i}:\t", volunteer.getinfo())
