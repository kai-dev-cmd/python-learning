#Todo list

#step 1 - test list
#i could make an option to create a list
#but i just wanna keep it simple for now

todo_list = ['a', 'b', 'c']

#step 2 - ask for choice

while True: 
    
    choice = input("Type 'add' / 'remove' / 'view' / 'done': ").lower()

#step 3 - if loop choices begins here

#at first i thought of using '+='' before using 'append'
#but i had a feeling '+='' is wrong
#if '+='' it will add each letter/character separately instead of whole
#i also learned there is no need for adding "continue" many times
#the program will know to go back to step 2 by itself unless "break" happens

    #choice 1
    if choice == 'add':
        new_task = input("Add new task: ")
        todo_list.append(new_task) #use append() to put a whole something in list
        print("Task added!")

    #choice 2
    elif choice == 'remove':
        if len(todo_list) == 0: #checks if theres any task first
            print("No task to remove. Add a task first.")
        
        else:
            #show the tasks first to make it easy
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")
            
            try:
                num = int(input("Remove which task number: "))
            except ValueError:
                print("Please enter a number")
                continue #restarts
            
            if 1 <= num <= len(todo_list):
                removed = todo_list.pop(num - 1) #we could also use .remove() but .pop() can be used to return the value in the print using f"...".
                print(f"Removed: {removed}")
            else:
                print("Invalid number.")
        
    #choice 3
    elif choice == 'view':
        if len(todo_list) == 0:
            print("No tasks yet")
        else: #for function means for every item, repeat each
            for index, task in enumerate(todo_list, start=1): #because the index starts at '0' naturally. so we set 'start=1' so that it knows count from 1
                print(f"{index}. {task}")
        
    #choice 4
    elif choice == 'done':
        print("Goodbye!")
        break #program ends
        
    #if invalid
    else:
        print("Instruction not valid. Try again")