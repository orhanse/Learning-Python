from doctor import Doctor
from patient import Patient


doctors = {}
patients = {}


def doctorEntry():
    doctorID = input('Enter doctor ID: ')
    
    if doctorID in doctors:
        doctor = doctors[doctorID]
        print(f'Welcome Dr. {doctor.name}')
        doctor.showPatientList()

        while True:
            print("\nOptions:")
            print("1. Cure patient")
            print("2. Exit")
            
            intputValue = input('Choice: ')
            try:
                choice = int(intputValue)
            except:
                print('ERROR: Invalid Entry')
                continue
        
            if choice == 1:
                pid = input('Enter patient ID to cure (or press Enter for first): ')
                patientID = pid.strip() if pid else None
                doctor.cure(patientID)

            elif choice == 2:
                print('Goodbye.')
                break
            else:
                print('ERROR: Wrong choice. Try Again')
    
    else:
        print('Doctor not found. Registering new one...')
        newDoctor = Doctor.register(doctorID)
        doctors[newDoctor.id] = newDoctor
        print('Doctor registered successfully.')


def patientEntry():
    patientID = input('Patient ID: ')
    
    if patientID in patients:
        patient = patients[patientID]
        print(f'Welcome {patient.name}')

        while True:
            print("\nPatient Menu:")
            print("1. View appointments")
            print("2. Book new appointment")
            print("3. Exit")

            intputValue = input('Choice: ')
            try:
                choice = int(intputValue)
            except:
                print('ERROR: Invalid Entry')
                continue
            
            if choice == 1:
                patient.showCurrentAppoinments()

            elif choice == 2:
                patient.showAvailableDoctors(doctors)
                doctorID = input("Enter doctor ID to book or press Enter for first available (-1 to cancel): ")

                if doctorID == -1:
                    continue

                doctorID = doctorID.strip()
                patient.book(doctors, doctorID if doctorID else None)

            elif choice == 3:
                print('Goodbye.')
                break

            else:
                    print('ERROR: Wrong choice. Try Again')
    
    else:
        print('Patient not found. Registering new one...')
        newPatient = Patient.register(patientID)
        patients[newPatient.id] = newPatient
        print('Patient registered successfully.')


def main():
    while True:
        print('\n----- Hospital System -----')
        print('1. Doctor Entry')
        print('2. Patient Entry')
        print('3. Exit')

        intputValue = input('Choice: ')
        try:
            choice = int(intputValue)
        except:
            print('ERROR: Invalid Entry')
            continue
        
        if choice == 1:
            doctorEntry()
        
        elif choice == 2:
            patientEntry()
        
        elif choice == 3:
            print('Goodbye.')
            break

        else:
            print('ERROR: Wrong choice. Try Again')


if __name__ == '__main__':
    main()