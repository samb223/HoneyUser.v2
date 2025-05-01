import subprocess
import pwd

def user_exists(username):
    try:
        pwd.getpwnam(username)
        return True
    except KeyError:
        return False

def create_user(user_config):
    cmd = [
        "sudo", "useradd", "-m",
        "-s", user_config["shell"],
        "-d", user_config["home"],
        user_config["name"]
    ]
    subprocess.run(cmd, check=True)
    subprocess.run(["sudo", "chpasswd"], input=f"{user_config['name']}:{user_config['password']}".encode(), check=True)
