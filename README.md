# Bionik-TwitchGo-Bot

# Installation on a new machine
1. Setup new python virtual environment (venv)
2. Install ROS 2 (here is how to do it in Ubuntu-based environment): https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html
**NOTE: If you want to install it on any Debian-based distro, change (in above instruction 3-rd command in section "Setup Sources"):

```echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```
for 
```
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $VERSION_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

3. Install dependencies with pip from file requirements.txt.
```
pip install -r requirements.txt
```
