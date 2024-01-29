import os
import subprocess

# Source: https://docs.python.org/3/library/os.html
if not os.path.exists("venv"):
    # Create virtualenv
    subprocess.run(["python3", "-m", "venv", "venv"])
    print("Virtualenv created!")

# Activate virtualenv
if os.name == "nt":
    activate_script = os.path.join("venv", "Scripts", "activate")
    print("Windows detected!")
else:
    activate_script = os.path.join("venv", "bin", "activate")
    print("UNIX detected!")

# Source: https://stackoverflow.com/questions/1871549/determine-if-python-is-running-inside-virtualenv and https://docs.python.org/3/library/os.html
if os.getenv("VIRTUAL_ENV") is None:
    subprocess.run(["source", activate_script], shell=True)
    print("Virtualenv activated!")


subprocess.run(["pip3", "install", "-r", "requirements.txt"])
print("Django installed!")
subprocess.run(["npm", "install"])
print("npm packages installed!")
subprocess.run(["npx", "esbuild", "main.js", "--bundle", "--minify", "--sourcemap", "--outfile=./emojis/static/main.min.js"])
print("esbuild complete!")
subprocess.run(["python3", "manage.py", "runserver", "0.0.0.0:8000"])
print("Server running!")
