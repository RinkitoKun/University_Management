from models.schedule import Schedule
from models.course import Course  # Assuming a Course class exists
from models.room import Room  # Import Room class
from models.person import Person  # Import the Person class from the correct module

class Professor(Person):
    def __init__(self, professor_id, name, email, password, phone, gender, address, specialization):
        super().__init__(name, email, password, phone, gender, address)
        self.professor_id = professor_id
        self.specialization = specialization
        self.assigned_courses = []
        self.schedule = Schedule()  # Associate the schedule with the professor

    def assign_course(self, course, room):
        """Assign a course to the professor's schedule along with a room"""
        self.assigned_courses.append(course)
        self.schedule.add_course(course, room)

    def view_courses(self):
        return self.assigned_courses

    def view_schedule(self):
        """Professor can view their schedule with rooms"""
        self.schedule.view_schedule()
