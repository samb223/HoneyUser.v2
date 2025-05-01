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

    print(f"[+] Starting activity simulation for decoy user: {username}\n")
    print(f"[+] Detected OS: {system}\n")

    # On Linux, set up a periodic cron job for ongoing activity
    if system == "Linux":
        script_path = os.path.abspath("honeyuser.py")  # Adjust path if needed
        install_cron_job_as_user(script_path, username)
    
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

def install_cron_job_as_user(script_path, username):
    if platform.system() != "Linux":
        return

    cron_line = f"*/5 * * * * /usr/bin/python3 {script_path} # HoneyUser cron job\n"
    try:
        existing_cron = subprocess.run(
            ["crontab", "-u", username, "-l"],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True
        ).stdout

        if cron_line.strip() not in existing_cron:
            new_cron = existing_cron + cron_line
            subprocess.run(["crontab", "-u", username, "-"], input=new_cron, text=True)
            print(f"[+] Cron job installed for user '{username}'.")
        else:
            print("[*] Cron job already exists.")
    except Exception as e:
        print(f"[!] Failed to manage crontab: {e}")
