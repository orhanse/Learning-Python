from src.clinic import Clinic, Patient, Doctor

clinic = Clinic()

patientOne = Patient('Selman', '30', 'Kolit')
patientTwo = Patient("Ali", '28', 'Cancer')

doctorOne = Doctor('Dr. Ahmet', '42', 'Cardiology')
doctorTwo = Doctor('Dr. Kate', '72', 'Ortho')
doctorThree = Doctor('Dr. Kemal', '34', 'Eye')

def testCreateFullFlow():
    clinic.addPatient(patientOne)
    clinic.addDoctor(doctorOne)
    clinic.scheduleAppointment(patientOne, doctorOne, '2025-01-01')
    assert len(clinic.appointments) == 1
    assert len(clinic.patients[patientOne.pid].appointments) == 1
    assert len(clinic.doctors[doctorOne.pid].patients) == 1


def testPatientAttachedToDoctor():
    clinic.addPatient(patientOne)
    clinic.addDoctor(doctorOne)
    clinic.scheduleAppointment(patientOne, doctorOne, '2025-01-01')
    assert patientOne.appointments[doctorOne.name].date == '2025-01-01'


def testAppointmentAttachedToPatient():
    clinic.addPatient(patientOne)
    clinic.addDoctor(doctorOne)
    clinic.scheduleAppointment(patientOne, doctorOne, '2025-03-10')
    assert doctorOne.patients[patientOne.name].illness == patientOne.illness


def testPatientAndDoctorLookup():
    clinic.addPatient(patientOne)
    clinic.addDoctor(doctorOne)
    found_p = clinic.getPatient(patientOne.pid)
    found_d = clinic.getDoctor(doctorOne.pid)
    assert found_p.name == patientOne.name
    assert found_d.name == doctorOne.name


def testMultiplePatientsMultipleDoctors():
    clinic.addPatient(patientOne)
    clinic.addPatient(patientTwo)
    clinic.addDoctor(doctorTwo)
    clinic.addDoctor(doctorTwo)
    assert len(clinic.patients) == 2
    assert len(clinic.doctors) == 2


def testMultipleAppointmentsFlow():
    clinic = Clinic()
    clinic.addPatient(patientTwo)
    clinic.addDoctor(doctorTwo)
    clinic.addDoctor(doctorThree)
    clinic.scheduleAppointment(patientTwo, doctorTwo, '2025-01-01')
    clinic.scheduleAppointment(patientTwo, doctorThree, '2025-01-02')
    print(clinic.patients[patientTwo.pid].appointments)
    assert len(clinic.appointments) == 2
    assert len(clinic.doctors[doctorTwo.pid].patients) == 1
    assert len(clinic.doctors[doctorThree.pid].patients) == 1
    assert len(clinic.patients[patientTwo.pid].appointments) == 2
    print(clinic.patients[patientTwo.pid].appointments)

