import pytest
from src.clinic import Clinic, Patient, Doctor

clinic = Clinic()
patientOne = Patient('Kate', '72', 'Cancer')
doctorOne = Doctor('Dr. Ali', '34', 'Dermatology')

def testClinicAddPatient():
    clinic.addPatient(patientOne)
    assert len(clinic.patients) == 1


def testClinicAddDoctor():
    clinic.addDoctor(doctorOne)
    assert len(clinic.doctors) == 1


def testClinicScheduleAppointment():
    clinic.addPatient(patientOne)
    clinic.addDoctor(doctorOne)
    clinic.scheduleAppointment(patientOne, doctorOne, '2025-01-02')
    assert len(clinic.appointments) == 1

