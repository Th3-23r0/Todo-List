import time as t
import json
import os
import shutil
import id_actions

ID = 0

def add():

    ID = id_actions.load_id()


    task = input("What do you want to add? \n") #allows user to input task

    ID += 1

    tasks_dir = "Tasks"
    os.makedirs(tasks_dir, exist_ok= True)

    file_path = os.path.join(tasks_dir, f"{ID}.json")

    task_data = {
        "task name": task,
        "creation date (ctime)": t.ctime(),
        "status": "TODO", #WORK ON THIS
        "id": ID
    } #task data

    with open(file_path, "w") as file: #creates a JSON new file 
        json.dump(task_data, file, indent=4) #dumps contents of task_data_json_string to a json file
    print(f"The ID of this task is {ID} \n")

    id_actions.save_id(ID)

def remove():

    delete_id = input("Which task do you want to delete? (use task ID) \n")

    if os.path.exists("Tasks"):
        os.chdir("Tasks")
        os.remove(f"{delete_id}.json")
        print("Deleted Task! \n")

        os.chdir("..")

        id = id_actions.load_id()
        id_actions.save_id(id)
    
    else:
        print("You do not have any tasks to remove \n")
    
def list():
    tasks_dir = "Tasks"

    if not os.path.exists(tasks_dir):
        print("You have no tasks.\n")
        return

    task_files = os.listdir(tasks_dir)
    if not task_files:
        print("You have no tasks.\n")
        return

    print("Your tasks:\n")
    for filename in task_files:
        if filename.endswith(".json"):
            file_path = os.path.join(tasks_dir, filename)
            with open(file_path, "r") as f:
                task_data = json.load(f)
                task_name = task_data.get("task name", "Unknown task")
                task_id = task_data.get("id", "No ID")
                creation_date = task_data.get("creation date (ctime)", "Creation Date Not Found")
                print(f"Task: {task_name} \n\tCreation Date: {creation_date} \n\tID: {task_id}")
    
def reset():
    confirm = input("Are you sure you want to reset everything (Y/N)").lower()

    if confirm in ["yes", "y"]:


        if os.path.exists("id.txt"):
            os.remove("id.txt")
        else:
            print("You do not have an ID file to reset \n")

        if os.path.exists("Tasks"):
            shutil.rmtree("Tasks")
        else:
            print("You have no tasks \n")

def update():
    
    id = input("What task do you want to update")
    path = os.path.join("Tasks", f"{id}.json")

    if not os.path.exists(path):
        print("This task doesn't exist \n")

    if os.path.exists(path):

        with open(path, "r") as f:
            data = json.load(f)

        data.get("task name")
        y = input("What do you want to change the task to? \n")

        data["task name"] = y

        with open(path, "w") as f:
            json.dump(data, f, indent=4)

def status():
    
    id = input("What tasks status do you want to update? \n")

    path = os.path.join("Tasks", f"{id}.json")

    if os.path.exists(path):

        with open(path, "r") as f:
            status_to = input("What do you want to change the status to (C = complete, I = in progress, T = todo, CA = cancel)\n").lower()

            data = json.load(f)

            print(data)



        if status_to in ["complete", "c"]:
            
            data["status"] = "COMPLETE"

            with open(path, "w") as f:
                json.dump(data, f, indent = 4)

            print(f"Updated task {id} to completed \n")

        elif status_to in ["in progress", "i"]:
            data["status"] = "IN PROGRESS"

            with open(path, "w") as f:
                json.dump(data, f, indent = 4)

            print(f"Updated task {id} to in progress \n")

        elif status_to in ["todo", "t"]:

            data["status"] = "TODO"

            with open(path, "w") as f:
                json.dump(data, f, indent = 4)

            print(f"Updated task {id} to todo \n")

    else:
        print("You have no tasks")