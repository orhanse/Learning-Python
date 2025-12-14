from src.loader import (
    loadDoctors, loadPatients, loadAppoinments,
    saveDoctors, savePatients, saveAppointments
)

from src.clinic import Clinic

def clinicMenu():
    clinic = Clinic()

    loadDoctors(clinic)
    loadPatients(clinic)
    loadAppoinments(clinic)

    while True:
        print('\n--- Hospital Appointment System ---')
        print('1. Doctor Login / Register')
        print('2. Patient Entry')
        print('3. Exit')

        intputValue = input('Choice: ')
        try:
            choice = int(intputValue)
        except:
            print('ERROR: Invalid Entry')
            continue

        if choice == 1:
            clinic.doctorEntry()

        elif choice == 2:
            clinic.patientEntry()

        elif choice == 3:
            print('Exiting...')
            saveDoctors(clinic)
            savePatients(clinic)
            saveAppointments(clinic)

            break

        else:
            print('Invalid option.')


def main():

    clinicMenu()
    

if __name__ == '__main__':
    main()