import os
import subprocess

# Check if virtualenv exists
if not os.path.exists("venv"):
    # Create virtualenv
    subprocess.run(["python", "-m", "venv", "venv"])
    print("Virtualenv created!")

# Activate virtualenv
if os.name == "nt":
    activate_script = os.path.join("venv", "Scripts", "activate")
    print("Windows detected!")
else:
    activate_script = os.path.join("venv", "bin", "activate")
    print("UNIX detected!")

if not os.environ.get("VIRTUAL_ENV"):
    subprocess.run(["source", activate_script], shell=True)
    print("Virtualenv activated!")


subprocess.run(["pip", "install", "-r", "requirements.txt"])
print("Django installed!")
subprocess.run(["npm", "install"])
print("npm packages installed!")
subprocess.run(["npx", "esbuild", "main.js", "--bundle", "--minify", "--sourcemap", "--outfile=./emojis/static/main.min.js"])
print("esbuild complete!")
subprocess.run(["python", "manage.py", "runserver", "0.0.0.0:8000"])
print("Server running!")
