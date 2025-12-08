import pytest
from unittest.mock import patch
from src.doctor import Doctor

doctor = Doctor('Dr. John', '30', 'Cardiology')

def testDoctorInitialization():
    assert doctor.pid == '30'
    assert doctor.name == 'Dr. John'
    assert doctor.speciality == 'Cardiology'


@patch('builtins.input', side_effect=['Dr. A', 'Cardiology'])
def testDoctorRegister(mock_input):
    doctor = Doctor.register('42')
    assert doctor.name == 'Dr. A'
    assert doctor.pid == '42'
    assert doctor.speciality == 'Cardiology'
