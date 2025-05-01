import subprocess
import ctypes

def user_exists(username):
    try:
        subprocess.check_output(["net", "user", username], stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError:
        return False

def create_user(user_config):
    subprocess.run(["net", "user", user_config["name"], user_config["password"], "/add"], check=True)
