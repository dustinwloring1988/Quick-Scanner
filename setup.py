# setup.py

import os
import subprocess

# Create the required folder structure
if not os.path.exists("vuln"):
    os.makedirs("vuln")

if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

if not os.path.exists("scan_results"):
    os.makedirs("scan_results")

# Check if the required tools are installed
try:
    import nmap
    import masscan
except ImportError:
    # Install the required tools using pip
    subprocess.call(["apt", "update"])
    subprocess.call(["sudo", "apt", "upgrade", "-y"])
    subprocess.call(["sudo", "apt", "install", "-y", "masscan"])
    subprocess.call(["sudo", "apt", "install", "-y", "nmap"])

# Download the exclude.conf file
os.system("curl -LJO https://github.com/robertdavidgraham/masscan/raw/master/data/exclude.conf")
os.rename("exclude.conf", "exclude.txt")
