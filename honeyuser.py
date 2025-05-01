
import os
import platform
import time
import yaml
from platform import system
from utils.helpers import load_config
from osplatform import linux, windows
from activity.simulator import simulate_activity
from monitor.detector import Monitor
from alert.logger import Logger
from alert.emailer import Emailer


def get_platform_module():
    if system() == "Windows":
        return windows
    elif system() == "Linux":
        return linux
    elif system() == "Darwin":
        return macos
    else:
        raise NotImplementedError("Unsupported OS")


def main():
    config = load_config("config.yaml")
    platform_module = get_platform_module()

    # Create decoy user
    if not platform_module.user_exists(config['user']['name']):
        platform_module.create_user(config['user'])

    # Simulate activity
    simulate_activity(config)

    # Monitor
    monitor = Monitor(config)
    monitor.start()

    # Alert/logging setup
    logger = Logger(config)
    emailer = Emailer(config)

    while True:
        events = monitor.check_events()
        for event in events:
            logger.log_event(event)
            if config['alerts']['email_enabled']:
                emailer.send_alert(event)
        time.sleep(10)


if __name__ == "__main__":
    main()
