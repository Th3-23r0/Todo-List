import actions

running = True

while running:
    action = input("What do you want to do? (A = add,  R = remove, U = update, S = change status, L = list, RE = reset, E = exit, H = help) \n").lower()

    if action in ["exit", "e"]:
        running = False

    elif action in ["add", "a"]:
        actions.add()

    elif action in ["update", "u"]:
        actions.update()

    elif action in ["remove", "r"]:
        actions.remove()

    elif action in ["list", "l"]:
        actions.list()

    elif action in ["reset", "re"]:
        actions.reset()

    elif action in ["status", "s"]:
        actions.status()

    elif action in ["help", "h"]:
        actions.help()

    else:
        print("Invalid input. Please enter A, R, E, or RE.")
