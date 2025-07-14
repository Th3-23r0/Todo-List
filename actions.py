import time as t
import json
import os
import id_actions

ID = 0

def add():

    task_file_path = "tasks.json"

    task_name = input("What do you want to add?\n")

    ID = id_actions.load_id()
    ID += 1

    if os.path.exists(task_file_path):
        with open(task_file_path, "r") as f:
            try:
                tasks = json.load(f)
            except json.JSONDecodeError:
                tasks = {}
    else:
        tasks = {}

    task_data = {
        "Task Name": task_name,
        "Task ID": ID,
        "Date Added": t.ctime(),
        "Status": "TODO"
    }

    tasks[str(ID)] = task_data

    id_actions.save_id(ID)

    with open(task_file_path, "w") as f:
        json.dump(tasks, f, indent = 4)

    print(f"{task_name} has been added (ID:{ID})")
#finished add
def remove():

    global_id = id_actions.load_id()

    ID = input("Which task do you want to delete? (use task ID) \n")
    path = "tasks.json"

    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                tasks = json.load(f)
        except json.JSONDecodeError:
            print("file not found")
            tasks = {}

        if ID in tasks:
            del tasks[ID]
            global_id -= 1
            id_actions.save_id(global_id)
        else:
            print("You do not have a task to delete\n")

        with open(path, "w") as f:
            json.dump(tasks, f, indent = 4)
            

    else:
        print("You do not have any tasks \n")
#finished remove  
def list():
    task_file_path = "tasks.json"

    if os.path.exists(task_file_path):

        with open(task_file_path, "r") as f:
            try:
                tasks_string = json.load(f)
            except json.JSONDecodeError:
                print("Tasks file is corrupted")

        for task_id, task_data in tasks_string.items():
            task_name = task_data["Task Name"]
            creation_date = task_data ["Date Added"]
            task_status = task_data["Status"]

            print(f"Task Name: {task_name} \n\n\tCreation Date: {creation_date}\n\tStatus: {task_status}\n\tID: {task_id}\n")

    else:
        print("You do not have any tasks")
#finished list
def reset():
    confirm = input("Are you sure you want to reset everything (Y/N)").lower()

    if confirm in ["yes", "y"]:


        if os.path.exists("id.txt"):
            os.remove("id.txt")
        else:
            print("You do not have an ID file to reset \n")

        if os.path.exists("tasks.json"):
            os.remove("tasks.json")
        else:
            print("You have no tasks \n")
#finished reset
def update():
    
    id = input("What task do you want to update (use task ID)\n")

    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            tasks = json.load(f)

        if id in tasks:
            ided_task = tasks[id]
        else:
            print("ID doesn't exist")

        change_to = input(f"What do you want to change the task to? (it was \"{ided_task["Task Name"]}\")\n")

        ided_task["Task Name"] = change_to

        with open("tasks.json", "w") as f:
            json.dump(tasks, f, indent = 4)
#finished update
def status():
    
    id = input("What tasks status do you want to update? \n")


    if os.path.exists("tasks.json"):

        with open("tasks.json", "r") as f:

            status_to = input("What do you want to change the status to (C = complete, I = in progress, T = todo)\n").lower()

            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print("file is corrupted")
            task = data[id]


        if status_to in ["complete", "c"]:
            
            task["Status"] = "COMPLETE"

            with open("tasks.json", "w") as f:
                json.dump(data, f, indent = 4)

            print(f"Updated task {id} to completed \n")

        elif status_to in ["in progress", "i"]:
            task["Status"] = "IN PROGRESS"

            with open("tasks.json", "w") as f:
                json.dump(data, f, indent = 4)

            print(f"Updated task {id} to in progress \n")

        elif status_to in ["todo", "t"]:

            task["Status"] = "TODO"

            with open("tasks.json", "w") as f:
                json.dump(data, f, indent = 4)

            print(f"Updated task {id} to todo \n")

    else:
        print("You have no tasks")
#finished status
def help():
    print("""

Add = Add a task to your task list
Remove = Remove a task from your task list
Update = Update the name of a task
Change Status = Changes the status of a task (the default status of a task is "TODO")
List = Lists all tasks, IDs, creation times, and status'
Reset = Removes all tasks and resets the ID to 0
Exit = Exits the program
Help = Shows you the list of keywords and what they do

""")