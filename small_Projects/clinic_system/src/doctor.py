###############################################
# doctor.py
###############################################
from src.person import Person

class Doctor(Person):
    MAX_PATIENTS = 5

    def __init__(self, name: str, pid: str, speciality: str):
        super().__init__(name, pid)
        self.speciality = speciality
        self.available = True
        self.patients = []


    @classmethod
    def register(cls, pid):
        print('\nRegistering a new doctor...')
        name = input('Enter doctor name: ')
        speciality = input('Enter speciality: ')
        
        return cls(name, pid, speciality)


    def isAvailable(self):
        return self.available and len(self.patients) < self.MAX_PATIENTS


    def addPatient(self, patientID):
        if self.isAvailable():
            self.patients.append(patientID)

            if len(self.patients) >= self.MAX_PATIENTS:
                self.available = False
        
        else:
            raise ValueError('Doctor is full.')


    def cure(self):
        if not self.patients:
            raise ValueError('No patients to cure')
        
        patientID = self.patients.pop()
        return patientID


    def __str__(self):
        return f'Doctor(name={self.name}, speciality={self.speciality})'
