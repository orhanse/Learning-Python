from person import Person

class Patient(Person):
    appointments = list()
    illnesses = list()
    
    def _init__(self, name: str, pid: str, ilsness):
        super().__init__(name, pid)
        self.appointments = []
        self.illnesses.append(ilsness)
    
    @classmethod
    def register(cls, pid):
        print('Registering a new patient...')
        name = input('Patient Name: ')
        illness = input('Illness: ')
        
        return cls(name, pid, illness)

    def showCurrentAppoinments(self):
        if not self.appointments:
            print('No current appointments.')
            return
        
        print('Your Appointments: ')
        for d in self.appointments:
            print(f' - {d.name}, Speciality: {d.speciality}')
    
    def showAvailableDoctors(self, doctors : list):
        available = [d for d in doctors.values() if d.isAvailable()]

        if not available:
            print('No available doctor right now.')
            return
        
        print('Available Doctors: ')
        for d in available:
            print(f'ID: {d.id}, Name: {d.name}, Speciality: {d.speciality}')

    def book(self, doctors : list, doctorID = None):
        availableDoctors = [d for d in doctors.values() if d.isAvailable()]
        if not availableDoctors:
            print('No available doctors.')
            return
        
        if doctorID:
            booked = False
            for doctor in availableDoctors:
                if doctor.id == doctorID:
                    doctor.patients.append(self)
                    self.appointments.append(doctor)
                    print(f'Booked doctor: {doctor.name}')
                    booked = True
            
            if not booked:
                print('Doctor not available or invalid ID.')
        
        else:
            doctor = availableDoctors[0]
            doctor.patients.append(self)
            self.appointments.append(doctor)
            print(f'Booked first avaialable doctor: {doctor.name}')
