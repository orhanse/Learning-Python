import json
from src.patient import Patient
from src.doctor import Doctor
from src.appointment import Appointment
from src.clinic import Clinic


def loadJson(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f'File not found: {path}. Starting empty.')
        return []
    except json.JSONDecodeError:
        print(f'Invalid JSON in {path}. Starting empty.')
        return []


def saveJson(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)


def loadPatients(clinic : Clinic, path = 'files/patients.json'):
    data = loadJson(path)
    for p in data:
        patient = Patient(p['name'], p['pid'], p['illness'])
        patient.myAppointments = p.get('appointments', [])
        clinic.patients[patient.pid] = patient


def loadDoctors(clinic : Clinic, path = 'files/doctors.json'):
    data = loadJson(path)
    for d in data:
        doctor = Doctor(d['name'], d['pid'], d['speciality'])
        doctor.patients = d.get('patients', [])
        clinic.doctors[doctor.pid] = doctor


def loadAppoinments(clinic : Clinic, path = 'files/appointments.json'):
    data = loadJson(path)
    for a in data:
        appt = Appointment(a['patient_id'], a['doctor_id'])
        clinic.appointments.append(appt)


def savePatients(clinic : Clinic, path = 'files/patients.json'):
    data = list()
    for p in clinic.patients.values():
        data.append({
            "name": p.name,
            "pid": p.pid,
            "illness": p.illness,
            "appointments": p.myAppointments
        })

    saveJson(path, data)


def saveDoctors(clinic, path='files/doctors.json'):
    data = list()
    for d in clinic.doctors.values():
        data.append({
            "name": d.name,
            "pid": d.pid,
            "speciality": d.speciality,
            "patients": d.patients
        })
    
    saveJson(path, data)


def saveAppointments(clinic : Clinic, path = 'files/appointments.json'):
    data = list()
    for appt in clinic.appointments:
        data.append({
            "patient_id": appt.patientID,
            "doctor_id": appt.doctorID
        })
    
    saveJson(path, data)
