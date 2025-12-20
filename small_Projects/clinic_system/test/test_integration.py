from src.clinic import Clinic, Patient, Doctor

clinic = Clinic()

patientIntegOne = Patient('Selman', '30', 'Kolit')
patientInteTwo = Patient("Ali", '28', 'Cancer')

doctorOne = Doctor('Dr. Ahmet', '42', 'Cardiology')
doctorTwo = Doctor('Dr. Kate', '72', 'Ortho')
doctorThree = Doctor('Dr. Kemal', '34', 'Eye')

def testCreateFullFlow():
    print(f'Before appoinment: {patientIntegOne.myAppointments}')
    clinic.addPatient(patientIntegOne)
    clinic.addDoctor(doctorOne)
    clinic.scheduleAppointment(patientIntegOne, doctorOne)
    assert len(clinic.appointments) == 1
    assert len(clinic.patients[patientIntegOne.pid].myAppointments) == 1
    assert len(clinic.doctors[doctorOne.pid].patients) == 1


def testPatientAttachedToDoctor():
    clinic.addPatient(patientIntegOne)
    clinic.addDoctor(doctorOne)
    clinic.scheduleAppointment(patientIntegOne, doctorOne)
    assert patientIntegOne.myAppointments[0] == doctorOne.pid
    assert doctorOne.patients[0] == patientIntegOne.pid


def testAppointmentAttachedToPatient():
    clinic.addPatient(patientIntegOne)
    clinic.addDoctor(doctorOne)
    clinic.scheduleAppointment(patientIntegOne, doctorOne)
    assert len(doctorOne.patients) == 1
    assert doctorOne.patients[0] == patientIntegOne.pid
    


def testPatientAndDoctorLookup():
    clinic.addPatient(patientIntegOne)
    clinic.addDoctor(doctorOne)
    found_p = clinic.getPatient(patientIntegOne.pid)
    found_d = clinic.getDoctor(doctorOne.pid)
    assert found_p.name == patientIntegOne.name
    assert found_d.name == doctorOne.name


def testMultiplePatientsMultipleDoctors():
    clinic.addPatient(patientIntegOne)
    clinic.addPatient(patientInteTwo)
    clinic.addDoctor(doctorTwo)
    clinic.addDoctor(doctorTwo)
    assert len(clinic.patients) == 2
    assert len(clinic.doctors) == 2


def testMultipleAppointmentsFlow():
    clinic = Clinic()
    clinic.addPatient(patientInteTwo)
    clinic.addDoctor(doctorTwo)
    clinic.addDoctor(doctorThree)
    clinic.scheduleAppointment(patientInteTwo, doctorTwo)
    clinic.scheduleAppointment(patientInteTwo, doctorThree)
    print(clinic.patients[patientInteTwo.pid].myAppointments)
    assert len(clinic.appointments) == 2
    assert len(clinic.doctors[doctorTwo.pid].patients) == 1
    assert len(clinic.doctors[doctorThree.pid].patients) == 1
    assert len(clinic.patients[patientInteTwo.pid].myAppointments) == 2
    print(clinic.patients[patientInteTwo.pid].myAppointments)

