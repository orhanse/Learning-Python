from src.appointment import Appointment

appointment = Appointment('301', '101')

def testAppointmentCreation():
    assert appointment.patientID == '301'
    assert appointment.doctorID == '101'


def testAppointmentStr():
    assert str(appointment) == 'Appointment(patient=301, doctor=101)'
