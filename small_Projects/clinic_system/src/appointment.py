###############################################
# appointment.py
###############################################


class Appointment:
    patientID = str()
    doctorID = str()

    def __init__(self, patientID, doctorID):
        self.patientID = patientID
        self.doctorID = doctorID

    def __str__(self):
        return f'Appointment(patient={self.patientID}, doctor={self.doctorID})'


