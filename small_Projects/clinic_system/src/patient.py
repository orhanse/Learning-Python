###############################################
# patient.py
###############################################
from src.person import Person

class Patient(Person):
    myAppointments = list()
    illness = str()


    def __init__(self, name : str, pid : str, illness : str):
        super().__init__(name, pid)
        self.illness = illness
        self.appointments = []


    @classmethod
    def register(cls, pid):
        print('Registering a new patient...')
        name = input('Patient Name: ')
        illness = input('Illness: ')

        return cls(name, pid, illness)


    def addDoctor(self, doctorID):
        self.myAppointments.append(doctorID)


    def __str__(self):
        return f'Patient(name={self.name}, ID={self.pid}, illness={self.illness})'

