import pytest
from src.patient import Patient
from src.doctor import Doctor
from src.clinic import Clinic


@pytest.fixture
def clinic():
    return Clinic()


@pytest.fixture
def patient_factory():
    def _create(name, pid, illness):
        return Patient(name, pid, illness)
    return _create


@pytest.fixture
def doctor_factory():
    def _create(name, pid, speciality):
        return Doctor(name, pid, speciality)
    return _create
