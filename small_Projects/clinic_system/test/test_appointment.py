from src.appointment import Appointment

appointment = Appointment('Selman', 'Dr. John', '2025-01-01')

def testAppointmentCreation():
    assert appointment.patientName == 'Selman'
    assert appointment.doctorName == 'Dr. John'
    assert appointment.date == '2025-01-01'


def testAppointmentStr():
    assert str(appointment) == 'Appointment(patient=Selman, doctor=Dr. John, date=2025-01-01)'
