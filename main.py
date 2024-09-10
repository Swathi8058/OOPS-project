from GoalAbstractClass import FitnessGoal, LearningGoal, HobbyGoal
from UpdationAbstractClass import DailySchedule, ShortTermGoalManager, get_validated_input


def main():
    daily_schedule = DailySchedule()  # Create daily schedule instance
    short_term_goal_manager = ShortTermGoalManager()  # Create short-term goal manager instance

    while True:
        print("\nMAIN MENU:")
        print("1. Create Daily Schedule")
        print("2. Manage Short-Term Goals")
        print("3. Display All Goals")
        print("4. Exit")

        option = input("Select an option: ").strip()  # Get option from user

        if option == "1":
            # Create daily schedule
            goal_count = int(input("How many goals do you want to schedule for today? "))
            for _ in range(goal_count):
                print("\nSelect Goal Type:")
                print("1. Fitness Goal")
                print("2. Learning Goal")
                print("3. Hobby Goal")
                goal_type = input("Enter choice: ").strip()

                name = input("Enter the goal name: ")
                priority = get_validated_input("Enter priority (1-5): ", lambda x: int(x) if 1 <= int(x) <= 5 else ValueError("Priority must be between 1 and 5."))

                if goal_type == "1":
                    daily_schedule.add_goal(FitnessGoal(name, priority))  # Add fitness goal
                elif goal_type == "2":
                    daily_schedule.add_goal(LearningGoal(name, priority))  # Add learning goal
                elif goal_type == "3":
                    daily_schedule.add_goal(HobbyGoal(name, priority))  # Add hobby goal
                else:
                    print("Invalid choice.")

            # Sort goals by priority before asking for progress
            daily_schedule.goals.sort(key=lambda g: g._priority)

            # After adding goals, prompt to update their progress in priority order
            for goal in daily_schedule.goals:
                progress = get_validated_input(f"Enter progress for '{goal._name}' (Priority: {goal._priority}) (0-100): ", lambda x: int(x) if 0 <= int(x) <= 100 else ValueError("Progress must be between 0 and 100."))
                daily_schedule.mark_task_completed(goal._name, progress)

            # Check if all tasks are completed
            if not daily_schedule.all_tasks_completed():
                # If not, remind the user and ask if they want to manage short-term goals
                while True:
                    choice = input("Not all tasks are done. Do you want to manage short-term goals anyway? (yes/no): ").strip().lower()
                    if choice == 'yes':
                        # Move to short-term goals management
                        break
                    elif choice == 'no':
                        # If no, redirect to complete pending tasks
                        print("Please complete all pending tasks first.")
                        for goal in daily_schedule.goals:
                            if goal._progress < 100:
                                progress = get_validated_input(f"Enter progress for '{goal._name}' (Priority: {goal._priority}) (0-100): ", lambda x: int(x) if 0 <= int(x) <= 100 else ValueError("Progress must be between 0 and 100."))
                                daily_schedule.mark_task_completed(goal._name, progress)
                        # Recheck if all tasks are completed after the second update
                        if daily_schedule.all_tasks_completed():
                            print("All tasks completed. Returning to the main menu...")
                        break
                    else:
                        print("Invalid input. Please enter 'yes' or 'no'.")

        elif option == "2":
            # Manage short-term goals
            while True:
                print("\nSHORT-TERM GOALS MENU:")
                print("1. Add a New Short-Term Goal")
                print("2. Update Progress for a Short-Term Goal")
                print("3. Display Short-Term Goals")
                print("4. Exit to Main Menu")

                sub_option = input("Select an option: ").strip()

                if sub_option == "1":
                    name = input("Enter the goal name: ")
                    deadline = input("Enter the deadline (YYYY-MM-DD): ")
                    short_term_goal_manager.add_goal(name, deadline)  # Add new short-term goal
                elif sub_option == "2":
                    name = input("Enter the name of the goal: ")
                    progress = get_validated_input("Enter progress (0-100): ", lambda x: int(x) if 0 <= int(x) <= 100 else ValueError("Progress must be between 0 and 100."))
                    short_term_goal_manager.update_progress(name, progress)  # Update progress for short-term goal
                elif sub_option == "3":
                    short_term_goal_manager.display_goals()  # Display short-term goals
                elif sub_option == "4":
                    break
                else:
                    print("Invalid option. Please choose again.")

        elif option == "3":
            # Display all goals
            print("\nDisplaying all goals...")
            daily_schedule.display_goals()
            short_term_goal_manager.display_goals()

        elif option == "4":
            print("Exiting the program. Have a nice Day :)")
            break
        else:
            print("Invalid option. Please choose again.")

       

if __name__ == "__main__":
    main()
