def add_task(tasks, task):
   tasks.append(userInput)
   print(f"Task added: {task}")

def view_task(tasks):
   print("Your tasks:")
   if tasks:
    for i, task in enumerate(tasks, start=1):
      print(f"{i}, {task}")
   else:
      print("No tasks available")

def del_tasks(tasks, task):
   if task in tasks:
      tasks.remove(task)
   else:
      print("No tasks to delete.")

def quit_app():
  print("Good bye!")
  exit()

tasks = []

while True:
    try:
         option = input('Welcome! Would you like to: \n -> Add task \n -> View task \n -> Delete task \n -> Quit the application \n').lower()
    
         if option == "add task":
           userInput  = input('What task would you like to add? \n')
           add_task(tasks, userInput)
                 
         elif option == "view task":
          if tasks:
             view_task(tasks)
      
         elif option == "delete task":
          if tasks:
            userInput = input('What task would you like to delete? \n')
            del_tasks(tasks, userInput)
          else:
             print("No tasks to delete")

          
    
         elif option == "quit the application":
          quit_app()
        
         else:
           print("Invalid input. Please try again.")

    except ValueError as VE:
        print(f"ValueError occured: {VE}")
    
    except TypeError as TE:
        print(f"TypeError occured: {TE}")

    except Exception as E:
        print(f"An unexpected error occured: {E}")

    finally:
        exit()