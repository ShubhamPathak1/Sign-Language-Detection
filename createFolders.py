import os 

main_dir = "Data"

actions = os.listdir("Data")
# actions = ['No Sign Detected']

if not os.path.exists(main_dir):
    os.makedirs(main_dir)

for action in actions:
    action_dir = os.path.join(main_dir, action)
    if not os.path.exists(action_dir):
        os.makedirs(action_dir)
    for i in range(60):
        sub_dir = os.path.join(action_dir, str(i))
        if not os.path.exists(sub_dir):
            os.makedirs(sub_dir)
