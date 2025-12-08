import pytest
from src.patient import Patient
from src.appointment import Appointment


patientOne = Patient('Selman', '30', 'Kolit')
patientTwo = Patient('Ali', '28', 'Cancer')

appoinment = Appointment(patientOne.pid, '42', '2025-01-01')


def testPatientInitialization():
    assert patientOne.name == 'Selman'
    assert patientOne.pid == '30'
    assert patientOne.illness == 'Kolit'
    assert hasattr(patientOne, 'appointments')
    assert patientOne.appointments == {}


def testAddAppointment():
    patientOne.addAppointment(appoinment)
    assert len(patientOne.appointments) == 1


def test_patient_str():
    assert str(patientOne) == 'Patient(name=Selman, ID=30, illness=Kolit)'
