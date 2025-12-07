from person import Person


class Doctor(Person):
    MAX_PATIENTS = 5
    patients = list()
    speciality = str()
    availabile = bool()

    def __init__(self, name: str, pid: str, speciality: str):
        super().__init__(name, pid)
        self.speciality = speciality
        self.availabile = True
        self.patients = []
    
    @classmethod
    def register(cls, pid):
        print('Registering a new doctor...')
        name = input('Doctor Name: ')
        speciality = input('Doctor Speciality: ')
        
        return cls(name, pid, speciality)
    
    def isAvailable(self):
        return self.availabile and len(self.patients) < self.MAX_PATIENTS
    
    def showPatientList(self):
        if not self.patients:
            print('No patients waiting..')
            return
        
        print('Patients Booked: ')
        for p in self.patients:
            print(f' - {p}')
    
    def cure(self, patientID = None):
        if not self.patients:
            print('No petients to cure.')
            return
        
        if patientID:
            for p in self.patients:
                if p.id == patientID:
                    self.patients.remove(patientID)
                    print(f'Cured Patient: {p}')
                    return

        else:
            p = self.patients.pop(0)
            print(f'Cured Patient: {p}')
