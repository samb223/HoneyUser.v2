import os
import platform
import time
import yaml
from platform import system
from utils.helpers import load_config
import platform as py_platform  # avoid name conflict
if py_platform.system() == "Windows":
    from osplatform import windows as platform_module
elif py_platform.system() == "Linux":
    from osplatform import linux as platform_module
else:
    raise NotImplementedError("Unsupported OS")
from activity.simulator import simulate_activity
from monitor.detector import Monitor
from alert.logger import Logger
from alert.emailer import Emailer
import threading

should_exit = threading.Event()

def listen_for_exit():
    while True:
        cmd = input()
        if cmd.strip().lower() == "exit":
            print("[!] Exit command received. Stopping HoneyUser...")
            should_exit.set()
            break



def start_activity_simulation(config):
    while True:
        simulate_activity(config)

def get_platform_module():
    if system() == "Windows":
        print("[+] Detected platform: Windows")
        return windows
    elif system() == "Linux":
        print("[+] Detected platform: Linux")
        return linux
    else:
        raise NotImplementedError("Unsupported OS")

def main():
    print("[+] Loading configuration...")
    config = load_config("config.yaml")

    print("[+] Checking if decoy user exists...")
    # Create decoy user
    if not platform_module.user_exists(config['user']['name']):
        print(f"[+] Creating decoy user: {config['user']['name']}")
        platform_module.create_user(config['user'])
    else:
        print(f"[!] Decoy user '{config['user']['name']}' already exists.")

    print("[+] Initializing alert/logging system...")
    logger = Logger(config)
    emailer = Emailer(config)

    print("[+] Starting event monitor...")
    monitor = Monitor(config)

    # Start the activity simulation in a background thread
    activity_thread = threading.Thread(target=start_activity_simulation, args=(config,))
    activity_thread.daemon = True  # Ensures the thread exits when the main program exits
    activity_thread.start()

    # Main event loop for monitoring and alerting
    # Start listener thread
    listener_thread = threading.Thread(target=listen_for_exit, daemon=True)
    listener_thread.start()

    print("[+] Monitoring events. Type 'exit' to stop.")
    while not should_exit.is_set():
        events = monitor.check_events()
        for event in events:
            logger.log_event(event)
            if config['alerts']['email_enabled']:
                print("[+] Sending alert email...")
                emailer.send_alert(event)
        time.sleep(2)

if __name__ == "__main__":
    main()

