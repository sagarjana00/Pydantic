from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title="Name of patient", description="Give the name of the patient less than 50 characters", examples=['Nitish', 'Sagar'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=False,description="Is the patient married or not")]

    allergies: Annotated[Optional[List[str]], [Field(default=None,max_length=5)]]

    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.married)
    print("inserted into database")

def update_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print("Updated")

patient_info = {'name': 'Nitish','email':'abc@gmail.com','linkedin_url':'https://linkedin.com/1322','age':30, 'weight':74.65, 'married':True,'allergies':['Dust','Pollen'],'contact_details': {'phone': '7001531459'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)
