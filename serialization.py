from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: int


class Patient(BaseModel):

    name:str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {'city':'Haldia', 'state': 'West Bengal', 'pin':721654}

address1 = Address(**address_dict)

patient_dict = {'name': 'Sagar','gender':'Male', 'age': 21, 'address': address1}

patient1 = Patient(**patient_dict)

# temp = patient1.model_dump()

# temp = patient1.model_dump_json()

# temp = patient1.model_dump(include=['name','gender'])

temp = patient1.model_dump(exclude_unset=True)

# temp = patient1.model_dump(exclude={'address':['state']})

print(temp)
print(type(temp))
