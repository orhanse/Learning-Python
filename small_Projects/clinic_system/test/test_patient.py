import pytest
from src.patient import Patient
from src.appointment import Appointment


patientOne = Patient('Selman', '30', 'Kolit')
patientTwo = Patient('Ali', '28', 'Cancer')

appoinment = Appointment(patientOne.pid, '42')


def testPatientInitialization():
    assert patientOne.name == 'Selman'
    assert patientOne.pid == '30'
    assert patientOne.illness == 'Kolit'
    assert hasattr(patientOne, 'myAppointments')
    assert patientOne.myAppointments == []


def testAddAppointment():
    patientOne.addDoctor(appoinment)
    assert len(patientOne.myAppointments) == 1


def test_patient_str():
    assert str(patientOne) == 'Patient(name=Selman, ID=30, illness=Kolit)'
