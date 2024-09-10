from abc import ABC, abstractmethod
from datetime import datetime

# Abstract base class 1
class Goal(ABC):
    
#Initialize a goal with a name, priority, progress, and achievements.
    def __init__(self, name, priority=1):
        self._name = name # Internal use
        self._progress = 0
        self._priority = self._validate_priority(priority)  # Validating and setting priority
        self._achievements = []  # List to store achievements with timestamps

    @staticmethod
    def _validate_priority(priority): #Ensure priority is between 1 and 5.
        if 1 <= priority <= 5:
            return priority
        else:
            raise ValueError("Priority must be between 1 and 5.")

    @staticmethod
    def _validate_progress(progress): #Ensure progress is between 0 and 100.
        return min(100, max(0, progress))

    @abstractmethod
    def update_progress(self, progress): #Abstract method to update progress; must be implemented in subclasses.
        pass

    @abstractmethod
    def display_status(self):  #Abstract method to display the status; must be implemented in subclasses.
        pass

    def add_achievement(self, achievement): #Add an achievement with a timestamp.
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get current timestamp
        self._achievements.append(f"{timestamp} - {achievement}")  # Append achievement with timestamp

    def __str__(self):  #Return a string representation of the goal's status.
        achievements = ', '.join(self._achievements) if self._achievements else 'None'  # Format achievements
        return (f"\n** {self._name} **\n"
                f"\nProgress: {self._progress}%\n"
                f"Priority: {self._priority}\n"
                f"Achievements: {achievements}")


# Subclass for fitness goals
class FitnessGoal(Goal):
    def update_progress(self, progress): #Update progress ensuring it's between 0 and 100.
        self._progress = self._validate_progress(progress)  # Use base class method to validate progress

    def display_status(self): #Display the status of the fitness goal.
        print(f"\n🏃 Fitness Goal Status:\n{self}")  # Print goal status 


# Subclass for learning goals
class LearningGoal(Goal):
    def update_progress(self, progress): #Update progress ensuring it's between 0 and 100.
        self._progress = self._validate_progress(progress)  # Use base class method to validate progress

    def display_status(self): #Display the status of the learning goal.
        print(f"\n📚 Learning Goal Status:\n{self}")  # Print goal status 


# Subclass for hobby goals
class HobbyGoal(Goal):
    def update_progress(self, progress): #Update progress ensuring it's between 0 and 100.
        self._progress = self._validate_progress(progress)  # Use base class method to validate progress

    def display_status(self): #Display the status of the hobby goal.
        print(f"\n🎸 Hobby Goal Status:\n{self}")  # Print goal status 


# Subclass for short-term goals with a deadline
class ShortTermGoal(Goal):
    def __init__(self, name, deadline, priority=1):
        super().__init__(name, priority)  # Initialize base class
        self._deadline = self._validate_deadline(deadline)  # Validate and set deadline

    @staticmethod
    def _validate_deadline(deadline):
        #Validate date format YYYY-MM-DD.
        try:
            datetime.strptime(deadline, '%Y-%m-%d')  # Check if date is in the correct format
            return deadline
        except ValueError:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD.")

    def update_progress(self, progress):
        #Update progress ensuring it's between 0 and 100.
        self._progress = self._validate_progress(progress)  # Use base class method to validate progress

    def display_status(self):
       #Display the status of the short-term goal.
        print(f"\n📅 Short-Term Goal Status:\n{self}")  # Print goal status


