###############################################
# appointment.py
###############################################


class Appointment:
    date = str()
    patientName = str()
    doctorName = str()

    def __init__(self, patient_name, doctor_name, date):
        self.patientName = patient_name
        self.doctorName = doctor_name
        self.date = date

    def __str__(self):
        return f'Appointment(patient={self.patientName}, doctor={self.doctorName}, date={self.date})'


