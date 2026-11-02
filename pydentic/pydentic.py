
from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator


class PatientData(BaseModel):
    name: str = Field(max_length=50)
    email: EmailStr
    age: int = Field(gt=0, lt=120)
    weight: float
    married: bool
    contact_info: dict[str, str]

    @field_validator("email")
    @classmethod
    def validate_bank_email(cls, value):
        allowed_domains = ["icicibank.com", "yesbank.in"]

        domain = value.split("@")[1].lower()

        if domain not in allowed_domains:
            raise ValueError("Only ICICI Bank or YES BANK emails are allowed")

        return value

    @model_validator(mode="after")
    def validate_emergency_contact(self):
        if self.age > 60 and "emergency" not in self.contact_info:
            raise ValueError("Patients older than 60 must have an emergency contact")

        return self


def add_patient_data(patient: PatientData):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.contact_info)
    print("Data added successfully")


patient_data = {
    "name": "Aditya",
    "email": "aditya@icicibank.com",
    "age": 18,
    "weight": 70.5,
    "married": False,
    "contact_info": {
        "email": "aditya@example.com",
        "phone": "123-456-7890"
    }
}

patient = PatientData(**patient_data)
add_patient_data(patient)


def update_patient_data(patient: PatientData):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.contact_info)
    print("Data updated successfully")


patient_data = {
    "name": "Alex",
    "email": "alex@yesbank.in",
    "age": 18,
    "weight": 65.5,
    "married": False,
    "contact_info": {
        "email": "alex@example.com",
        "phone": "987-654-3210"
    }
}

patient_1 = PatientData(**patient_data)
update_patient_data(patient_1)
