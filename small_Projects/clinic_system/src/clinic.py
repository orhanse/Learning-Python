###############################################
# clinic.py
#
###############################################
from src.patient import Patient
from src.doctor import Doctor
from src.appointment import Appointment

class Clinic:
    patients = dict()
    doctors = dict()
    appointments = list()


    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.appointments = []


    def addPatient(self, patient):
        self.patients[patient.pid] = patient


    def addDoctor(self, doctor):
        self.doctors[doctor.pid] = doctor


    def getPatient(self, patientID):
        if patientID in self.patients:
            p  = self.patients[patientID]
            return p
        raise ValueError('Patient not found')


    def showAvailableDoctors(self):
        available = [d for d in self.doctors.values() if d.isAvailable()]

        if not available:
            print('No available doctor right now.')
            return
        
        print('\nAvailable Doctors: ')
        for d in available:
            print(f'ID: {d.pid}, Name: {d.name}, Speciality: {d.speciality}')


    def getDoctor(self, doctorID) -> Doctor:
        if doctorID in self.doctors:
            d  = self.doctors[doctorID]
            return d
        raise ValueError('Doctor not found')


    def scheduleAppointment(self, patient : Patient, doctor : Doctor, date : str):
        appt = Appointment(patient.name, doctor.name, date)
        self.appointments.append(appt)
        patient.addAppointment(appt)
        doctor.addPatient(patient)


    def doctorEntry(self):
        doctorID = input('Enter doctor ID (for login): ')

        try:
            doctor = self.getDoctor(doctorID)
            print(f'Welcome {doctor.name}')
            doctor.showPatientList()

            while True:
                print("\nOptions:")
                print("1. Cure patient")
                print("2. Exit")
            
                intputValue = input('Choice: ')
                try:
                    choice = int(intputValue)
                except:
                    print('ERROR: Invalid Entry')
                    continue
                
                if choice == 1:
                    pid = input('Enter patient ID to cure (or press Enter for first): ')
                    patientID = pid.strip() if pid else None
                    cured = doctor.cure(patientID)
                    print(f'Cured: {cured.name}')

                elif choice == 2:
                    print('Goodbye.')
                    break

                else:
                    print('ERROR: Wrong choice. Try Again')   

        except ValueError:
            print('Doctor not found.')
            newDoctor = Doctor.register(doctorID)
            self.addDoctor(newDoctor)
            print(f'Dr. {newDoctor.name} is registered successfully.')


    def patientEntry(self):
        patientID = input('Patient ID: ')

        try:
            patient = self.getPatient(patientID)
            print(f'Welcome {patient.name}')

            while True:
                print('\n Patient Menu: ')
                print("1. View appointments")
                print("2. Book an appointment")
                print("3. Exit")
            
                intputValue = input('Choice: ')
                try:
                    choice = int(intputValue)
                except:
                    print('ERROR: Invalid Entry')
                    continue

                if choice == 1:
                    patient.showCurrentAppoinments()

                elif choice == 2:
                    self.showAvailableDoctors()
                    docID = input('Enter doctor ID (Empty for first available): ')
                    if docID.strip() == '':
                        available = [d for d in self.doctors if d.available]
                        if not available:
                            print('No doctor available')
                            continue
                        doc = available[0]
                    else:
                        doc = self.getDoctor(docID)
    
                    date = input('Enter date(YYYY-mm-dd): ')
                    self.scheduleAppointment(patient, doc, date)
                    print('Appointment booked.')

                elif choice == 3:
                    break

                else:
                    print('ERROR: Wrong choice. Try Again')

        except ValueError:
            print('Patient not found.')
            newPatient = Patient.register(patientID)
            self.addPatient(newPatient)
            print(f'{newPatient.name} is registered successfully.')