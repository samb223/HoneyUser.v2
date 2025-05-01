import os
import time

def simulate_activity(config):
    user_home = config['user']['home']
    if config['activity']['simulate_shell']:
        bash_history = os.path.join(user_home, ".bash_history")
        with open(bash_history, "a") as f:
            f.write("ls -la\nwhoami\npwd\n")
    if config['activity']['simulate_browsing']:
        docs_dir = os.path.join(user_home, "Documents")
        os.makedirs(docs_dir, exist_ok=True)
        with open(os.path.join(docs_dir, "work_notes.txt"), "w") as f:
            f.write("Project: HoneyUser Deception System\n")
    time.sleep(config['activity']['interval_minutes'] * 60)
