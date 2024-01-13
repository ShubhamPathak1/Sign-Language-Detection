import os 

main_dir = "Data"

actions = os.listdir("Data")[:3]

if not os.path.exists(main_dir):
    os.makedirs(main_dir)

for action in actions:
    action_dir = os.path.join(main_dir, action)
    if not os.path.exists(action_dir):
        os.makedirs(action_dir)
    for i in range(30, 60):
        sub_dir = os.path.join(action_dir, str(i))
        if os.path.exists(sub_dir):
            os.removedirs(sub_dir)
