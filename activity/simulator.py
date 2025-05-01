import os
import time
import platform

def simulate_activity(config):
    system = platform.system()
    username = config['user']['name']

    if system == "Windows":
        user_home = f"C:\\Users\\{username}"
        shell_history = os.path.join(user_home, "AppData", "Roaming", "Microsoft", "Windows", "PowerShell", "PSReadLine", "ConsoleHost_history.txt")
    else:
        user_home = config['user']['home']
        shell_history = os.path.join(user_home, ".bash_history")

    # Simulate shell commands
    if config['activity']['simulate_shell']:
        os.makedirs(os.path.dirname(shell_history), exist_ok=True)
        with open(shell_history, "a") as f:
            f.write("ls -la\nwhoami\npwd\n")

    # Simulate fake browsing activity
    if config['activity']['simulate_browsing']:
        docs_dir = os.path.join(user_home, "Documents")
        os.makedirs(docs_dir, exist_ok=True)
        with open(os.path.join(docs_dir, "work_notes.txt"), "w") as f:
            f.write("Project: HoneyUser Deception System\n")

    time.sleep(config['activity']['interval_minutes'] * 60)
