# Overview
HoneyUser is a cross-platform Python tool designed to create decoy user accounts and simulate user activity to generate real, logged system events. It is specifically useful for monitoring systems for unauthorized access or unusual activity. This tool generates activity on a decoy account to mimic legitimate user actions and log events that can be monitored for security analysis.

# Features
Decoy Account Creation: Simulate a user account (honeyuser) for generating realistic system activity.

Simulate User Activity:

Shell command history (e.g., ls, pwd, whoami).

Fake browsing activities (e.g., creating documents in the user’s "Documents" folder).

Event Monitoring: Checks system logs (e.g., Windows Event Logs) for any failed login attempts or unusual activity related to the honeyuser account.

Cross-Platform: Works on both Windows and Linux systems.

Logging: Logs events triggered by the decoy account into a file for analysis.

# Requirements
Python 3.6 or higher

Windows or Linux OS

# Python Libraries:
The following Python libraries are required to run HoneyUser:

wmi (for Windows event logging)

platform (standard library, no installation needed)

os (standard library, no installation needed)

time (standard library, no installation needed)

subprocess (standard library, no installation needed)

json (standard library, no installation needed)

To install the necessary dependencies, you can use the following commands:

bash
Copy
Edit
pip install wmi
#Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/HoneyUser.git
cd HoneyUser
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
# Configuration
The HoneyUser tool can be configured through the config.json file. Here is an example configuration:

json
Copy
Edit
{
  "user": {
    "name": "honeyuser",
    "home": "/home/honeyuser"  # Path to user's home directory (Linux only)
  },
  "activity": {
    "simulate_shell": true,
    "simulate_browsing": true,
    "interval_minutes": 1  # Activity interval in minutes
  }
}
Configuration options:
user:

"name": Name of the decoy user (e.g., honeyuser).

"home": Path to the user's home directory (only needed for Linux).

activity:

"simulate_shell": Whether to simulate shell command history (True/False).

"simulate_browsing": Whether to simulate fake browsing activity (True/False).

"interval_minutes": Interval (in minutes) for how often user activity is simulated.

# Usage
Run the tool:

bash
Copy
Edit
python honeyuser.py
Monitoring:

The script will continuously monitor for login attempts and activity related to the decoy user (honeyuser).

The activity will be simulated according to the configuration.

Logs:

Logs will be saved in the logs/ directory.

The log file honeyuser_events.log will contain events, such as failed login attempts and system activities related to the honeyuser account.

Viewing Logs: To view the logs, simply open the logs/honeyuser_events.log file. The file will contain entries similar to:

yaml
Copy
Edit
2025-04-30 08:10:22 - [!] honeyuser triggered EventCode 4625: An account failed to log on.
# Troubleshooting
No events showing up in logs:

Ensure that the honeyuser account exists on the system.

Ensure that logs are enabled for the appropriate system events.

# Permissions issues:

For Linux, the tool may require root access to read system logs (/var/log/auth.log).
