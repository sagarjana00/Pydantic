from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]

    @field_validator('email', mode='after')
    @classmethod
    def email_validator(cls, value):

        valid_domains= ['hdfc.com','icici.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Not a Valid domain')
        return value
    
    @field_validator('name', mode='after')
    @classmethod
    def transform_name(cla, value):
        return value.upper()


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.married)
    print("inserted into database")

def update_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print("Updated")

patient_info = {'name': 'Nitish','email':'abc@hdfc.com','age':30, 'weight':74.65, 'married':True,'allergies':['Dust','Pollen'],'contact_details': {'phone': '7001531459'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)