

tasks = []

while True:
    try:
         option = input('Welcome! Would you like to: \n -> Add task \n -> View task \n -> Delete task \n -> Quit the application \n').lower()
    
         if option == "add task":
           userInput  = input('What task would you like to add? \n')
           tasks.append(userInput)
                 
         elif option == "view task":
          if tasks:
            print("Your tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
          else:
            print("No tasks available.")
      
         elif option == "delete task":
          if tasks:
            userInput = input('What task would you like to delete? \n')
            if userInput in tasks:
                tasks.remove(userInput)
                print(f"Task deleted: {userInput}")
            else:
                print("Task not found.")
          else:
            print("No tasks to delete.")
    
         elif option == "quit the application":
          print("Good bye!")
          break

         else:
           print("Invalid input. Please try again.")

    except ValueError as VE:
        print(f"ValueError occured: {VE}")
    
    except TypeError as TE:
        print(f"TypeError occured: {TE}")

    except Exception as E:
        print(f"An unexpected error occured: {E}")

    finally:
        print("This is the end of this interaction. Taking you back to the main menu \n ")