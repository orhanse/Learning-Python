###############################################
# patient.py
###############################################
from src.person import Person

class Patient(Person):
    appointments = dict()
    illness = str()


    def __init__(self, name : str, pid : str, illness : str):
        super().__init__(name, pid)
        self.illness = illness
        self.appointments = {}


    @classmethod
    def register(cls, pid):
        print('Registering a new patient...')
        name = input('Patient Name: ')
        illness = input('Illness: ')

        return cls(name, pid, illness)


    def showCurrentAppoinments(self):
        if not self.appointments:
            print('No current appointments.')
            return
        
        print('Your Appointments: ')
        for d in self.appointments.values():
            print(f' - {d.name}, Speciality: {d.speciality}')


    def addAppointment(self, appt):
        self.appointments[appt.doctorName] = appt


    def __str__(self):
        return f'Patient(name={self.name}, ID={self.pid}, illness={self.illness})'

