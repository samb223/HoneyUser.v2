import os
import time
import platform
import subprocess
import ctypes
if platform.system() == "Windows":
    import winreg

def simulate_activity(config):
    system = platform.system()
    username = config['user']['name']

    print(f"[+] Starting activity simulation for decoy user: {username}")
    print(f"[+] Detected OS: {system}")
    
    # Determine the shell history file based on OS
    if system == "Windows":
        user_home = f"C:\\Users\\{username}"
        shell_history = os.path.join(user_home, "AppData", "Roaming", "Microsoft", "Windows", "PowerShell", "PSReadLine", "ConsoleHost_history.txt")
    else:
        user_home = config['user']['home']
        shell_history = os.path.join(user_home, ".bash_history")

    # Simulate shell commands
    if config['activity']['simulate_shell']:
        print(f"[+] Simulating shell activity in: {shell_history}")
        try:
            os.makedirs(os.path.dirname(shell_history), exist_ok=True)
            with open(shell_history, "a") as f:
                f.write("ls -la\nwhoami\npwd\n")
            print("[+] Shell history updated.")
        except Exception as e:
            print(f"[!] Failed to simulate shell activity: {e}")

    # Simulate fake browsing activity
    if config['activity']['simulate_browsing']:
        docs_dir = os.path.join(user_home, "Documents")
        print(f"[+] Simulating document activity in: {docs_dir}")
        try:
            os.makedirs(docs_dir, exist_ok=True)
            with open(os.path.join(docs_dir, "work_notes.txt"), "w") as f:
                f.write("Project: HoneyUser Deception System\n")
            print("[+] Fake browsing document created.")
        except Exception as e:
            print(f"[!] Failed to create browsing artifact: {e}")
    
    wait_time = config['activity']['interval_minutes'] * 60
    time.sleep(wait_time)  # Sleep for the interval time before simulating activity again
