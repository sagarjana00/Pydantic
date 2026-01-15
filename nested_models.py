from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: int


class Patient(BaseModel):

    name:str
    gender: str
    age: int
    address: Address

address_dict = {'city':'Haldia', 'state': 'West Bengal', 'pin':721654}

address1 = Address(**address_dict)

patient_dict = {'name': 'Sagar', 'gender':'Male', 'age': 21, 'address': address1}

patient1 = Patient(**patient_dict)

print(patient1)

print(patient1.name)
print(patient1.age)
print(patient1.gender)
print(patient1.address.city)
print(patient1.address.state)
print(patient1.address.pin)