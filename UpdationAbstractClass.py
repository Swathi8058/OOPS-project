from abc import ABC, abstractmethod
from GoalAbstractClass import ShortTermGoal

# Abstract base class 2
class Updation(ABC):
    @abstractmethod
    def add_goal(self, goal):
        #Abstract method to add a goal; must be implemented in subclasses.
        pass

    @abstractmethod
    def display_goals(self):
        #Abstract method to display goals; must be implemented in subclasses.
        pass


# Class for managing daily schedule and goals
class DailySchedule(Updation):
    def __init__(self):
        self.goals = []  # List to store daily goals

    def add_goal(self, goal):
        #Add a goal to the daily schedule.
        self.goals.append(goal)  # Append goal to the list

    def display_goals(self):
       #Display all goals for the day in a more readable format.
        print("\n*** Today's Tasks ***")
        if not self.goals:
            print("No goals added to today's schedule.")  # Handle empty goal list
        else:
            for idx, goal in enumerate(self.goals, start=1):
                print(f"\n{idx}. {goal._name} | Priority: {goal._priority} | Progress: {goal._progress}%\n")

    def mark_task_completed(self, goal_name, progress): #Mark a task as completed and update its progress.
        goal_name = goal_name.lower()  # Convert goal name to lowercase for case-insensitive matching
        goal = next((g for g in self.goals if g._name.lower() == goal_name), None)  # Find goal
        if goal:
            goal.update_progress(progress)  # Update goal progress
            print(f"\nUpdated progress for '{goal._name}': {goal._progress}%\n")
            if goal._progress == 100:
                print(f"\n🎉Congratulations! Task {goal._name} is completed successfully :)\n")  
        else:
            print(f"\nTask '{goal_name}' not found in daily schedule.\n")  # Handle case where goal is not found

    def all_tasks_completed(self):
        #Check if all daily tasks are completed.
        return all(goal._progress == 100 for goal in self.goals)  # Return True if all goals are complete


# Class for managing short-term goals
class ShortTermGoalManager(Updation):
    def __init__(self):
        self._goals = []  # List to store short-term goals
        self._completed_goals = []  # List to store completed goals

    def add_goal(self, name, deadline):
        """Add a new short-term goal."""
        try:
            goal = ShortTermGoal(name, deadline)  # Create a new ShortTermGoal
            self._goals.append(goal)  # Add goal to the list
            print(f"Added new short-term goal: {name}")
        except ValueError as e:
            print(e)  # Print error message if date format is incorrect

    def display_goals(self):
        #Display all short-term goals and completed goals in a readable format.
        if self._goals:
            print("\n*** Short-Term Goals ***")
            for idx, goal in enumerate(self._goals, start=1):
                print(f"\n{idx}. {goal._name} | Progress: {goal._progress}% | Deadline: {goal._deadline}\n")
        else:
            print("\nNo short-term goals.")
    
        if self._completed_goals:
            print("\n🎉 Completed Short-Term Goals:\n")
            for idx, goal in enumerate(self._completed_goals, start=1):
                print(f"\n{idx}. {goal._name} | Completed on {goal._achievements[-1].split(' - ')[0]}\n")

        self._goals = [goal for goal in self._goals if goal._progress < 100]  # Remove completed goals from the list

    def update_progress(self, name, progress):
        #Update progress for a short-term goal.
        goal_name = name.lower()  # Convert goal name to lowercase for case-insensitive matching
        goal = next((g for g in self._goals if g._name.lower() == goal_name), None)  # Find goal
        if goal:
            goal.update_progress(progress)  # Update goal progress
            print(f"\nUpdated progress for '{goal._name}': {goal._progress}%")
            if goal._progress == 100:
                goal.add_achievement("Task completed successfully")  # Add achievement on completion
                print(f"\nCongratulations! Task {goal._name} is completed successfully :)\n")  
        else:
            print(f"\nTask '{goal_name}' not found in short-term goals.\n")  # Handle case where goal is not found


def get_validated_input(prompt, validation_func):
    #Get validated input from the user.
    while True:
        try:
            value = validation_func(input(prompt))  # Get input and validate
            return value
        except ValueError as e:
            print(e)  # Print error message if validation fails

