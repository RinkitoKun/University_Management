from utils.datastructures import LinkedList
from models.course import Course  # Assuming you have the Course class defined elsewhere
from models.room import Room  # Import Room class

class Schedule:
    def __init__(self):
        self.schedule = LinkedList()  # Using LinkedList to store scheduled events or courses

    def add_course(self, course, room):
        """Add a course to the schedule with an associated room"""
        self.schedule.append((course, room))  # Store both the course and the room
        print(f"Course '{course.name}' assigned to {room}.")

    def remove_course(self, course, room):
        """Remove a course from the schedule"""
        current = self.schedule.head
        prev = None
        while current:
            if current.data[0] == course and current.data[1] == room:
                if prev:
                    prev.next = current.next
                else:
                    self.schedule.head = current.next
                print(f"Course '{course.name}' removed from room {room}.")
                return
            prev = current
            current = current.next
        print(f"Course '{course.name}' not found in room {room}.")

    def view_schedule(self):
        """Display all courses in the schedule"""
        current_node = self.schedule.head
        if not current_node:
            print("No courses scheduled.")
            return
        print("Scheduled Courses:")
        while current_node:
            course, room = current_node.data
            print(f"- {course.name}, Room: {room.room_number} ({room.capacity} seats), {course.professor.name} (Professor)")
            current_node = current_node.next

    def get_schedule(self):
        """Return the list of scheduled courses along with rooms"""
        return self.schedule.display()
