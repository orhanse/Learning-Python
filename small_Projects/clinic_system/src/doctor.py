###############################################
# doctor.py
###############################################
from src.person import Person

class Doctor(Person):
    MAX_PATIENTS = 5
    patients = dict()
    speciality = str()
    available = bool()


    def __init__(self, name: str, pid: str, speciality: str):
        super().__init__(name, pid)
        self.speciality = speciality
        self.available = True
        self.patients = {}


    @classmethod
    def register(cls, pid):
        print('\nRegistering a new doctor...')
        name = input('Enter doctor name: ')
        speciality = input('Enter speciality: ')
        
        return cls(name, pid, speciality)


    def isAvailable(self):
        return self.available and len(self.patients) < self.MAX_PATIENTS
    

    def showPatientList(self):
        if not self.patients:
            print('No patient waiting...')
            return
        
        print('\nPatients Booked: ')
        for p in self.patients:
            print(f' - {p}')


    def addPatient(self, patient):
        if self.isAvailable():
            self.patients[patient.name] = patient

            if len(self.patients) >= self.MAX_PATIENTS:
                self.available = False
        
        else:
            raise ValueError('Doctor is full.')


    def cure(self, patientID = None):
        if not self.patients:
            raise ValueError('No patients to cure')
        
        if patientID is None:
            patient = self.patients.popitem(last = False)
            return patient
        
        if patientID in self.patients:
            patient = self.patients[patientID]
            del self.patients[patientID]
            return patient
        
        raise ValueError('Patient not found')


    def __str__(self):
        return f'Doctor(name={self.name}, speciality={self.speciality})'
