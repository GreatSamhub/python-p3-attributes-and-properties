class Person:
    APPROVED_JOBS = [
        "Doctor",
        "Engineer",
        "Teacher",
        "Artist",
        "Programmer",
        "Scientist",
        "Writer",
    ]

    def __init__(self, name="John Doe", job="Unemployed"):
        self._name = name.title()
        self._job = job

    def get_name(self):
        return self._name

    def set_name(self, name):
        if ((name.title()) is (str)) and (len(name.title()) < 25):
            self._name = name.title()
        else:
            print("Name must be a string under 25 characters.")

    def get_job(self):
        return self._job

    def set_job(self, job):
        if job in self.APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in the list of approved jobs.")

    name = property(get_name, set_name)
    job = property(get_job, set_job)
