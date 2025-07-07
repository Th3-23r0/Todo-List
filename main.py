import actions

running = True

while running:
    action = input("What do you want to do? (A = add, U = update, S = update status, R = remove, L = list, E = exit, RE = reset) \n").lower()

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

    else:
        print("Invalid input. Please enter A, R, E, or RE.")
