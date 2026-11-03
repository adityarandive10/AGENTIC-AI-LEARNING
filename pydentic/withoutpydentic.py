def add_patient_data(name, age):
    if type(name) == str and type(age) == int:
        if age > 0:
            print(name)
            print(age)
            print("Data added successfully")
        else:
            raise ValueError("Patient age must be greater than 0")
    else:
        raise TypeError("Invalid data entered")


def update_patient_data(name: str, age: int):
    if type(name) == str and type(age) == int:
        if age > 0:
            print(name)
            print(age)
            print("Data updated successfully")
        else:
            raise ValueError("Patient age must be greater than 0")
    else:
        raise TypeError("Invalid data entered")


patient_age = 19

if patient_age < 25:
    raise ValueError("Patient age must be 25 or above")