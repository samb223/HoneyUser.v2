import os
import time
import platform

# Simulate user activity as in honeyuser.py's activity simulator
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

def test_activity_simulation():
    # Sample config to test activity
    config = {
        'user': {
            'name': 'honeyuser',
            'home': '/home/honeyuser',  # Use the Windows home directory or any directory you want to test
        },
        'activity': {
            'simulate_shell': True,
            'simulate_browsing': True,
            'interval_minutes': 1
        }
    }
    
    # Run simulation
    print("Running activity simulation...")
    simulate_activity(config)

    # Check if files were created (Windows check)
    if platform.system() == "Windows":
        user_home = f"C:\\Users\\{config['user']['name']}"
        shell_history = os.path.join(user_home, "AppData", "Roaming", "Microsoft", "Windows", "PowerShell", "PSReadLine", "ConsoleHost_history.txt")
        docs_dir = os.path.join(user_home, "Documents", "work_notes.txt")
        
        assert os.path.exists(shell_history), "PowerShell history file not created!"
        assert os.path.exists(docs_dir), "Work notes document not created!"
        
        print("Test passed on Windows!")
    
    # Check if files were created (Linux/macOS check)
    elif platform.system() in ["Linux", "Darwin"]:
        shell_history = os.path.join(config['user']['home'], ".bash_history")
        docs_dir = os.path.join(config['user']['home'], "Documents", "work_notes.txt")
        
        assert os.path.exists(shell_history), "Bash history file not created!"
        assert os.path.exists(docs_dir), "Work notes document not created!"
        
        print("Test passed on Linux/macOS!")
    else:
        print("Unsupported platform")

if __name__ == "__main__":
    test_activity_simulation()
