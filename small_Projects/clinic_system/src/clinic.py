###############################################
# clinic.py
#
###############################################
from src.patient import Patient
from src.doctor import Doctor
from src.appointment import Appointment

class Clinic:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.appointments = []


    def addPatient(self, patient : Patient):
        self.patients[patient.pid] = patient


    def addDoctor(self, doctor : Doctor):
        self.doctors[doctor.pid] = doctor


    def removeFirstAppointment(self, patientID, doctorID):
        for i, appt in enumerate(self.appointments):
            if appt.patientID == patientID and appt.doctorID == doctorID:
                del self.appointments[i]
                return True
        return False



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


    def showPatientAppoinments(self, patient : Patient):
        if not patient.myAppointments:
            print('No current appointments.')
            return
        
        print('Your Appointments: ')
        for d in patient.myAppointments:
            doctor = self.getDoctor(d)
            print(f'Dr. {doctor.name} - Speciality: {doctor.speciality}')


    def showPatientList(self, doctor : Doctor):
        if not doctor.patients:
            print('No current appointments.')
            return

        print('Your Patients: ')
        for p in doctor.patients:
            patient = self.getPatient(p)
            print(f'{patient.name} - Illness: {patient.illness}')

    def scheduleAppointment(self, patient : Patient, doctor : Doctor):
        appt = Appointment(patient.pid, doctor.pid)
        self.appointments.append(appt)
        patient.addDoctor(doctor.pid)
        doctor.addPatient(patient.pid)


    def doctorEntry(self):
        doctorID = input('Enter doctor ID (for login): ')

        try:
            doctor = self.getDoctor(doctorID)
            print(f'Welcome {doctor.name}')
            self.showPatientList(doctor)

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
                    curedPatientID = doctor.cure()
                    patient = self.getPatient(curedPatientID)
                    patient.removeDoctor(doctor.pid)
                    self.removeFirstAppointment(patient.pid, doctor.pid)
                    print(f'Cured: {patient.name}')

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
                    self.showPatientAppoinments(patient)

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
    
                    self.scheduleAppointment(patient, doc)
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