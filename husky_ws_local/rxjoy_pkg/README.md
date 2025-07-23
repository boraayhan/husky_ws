# Installation
``git clone`` into desired workspace. Use ``colcon build`` to install. Further reading available [here](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Colcon-Tutorial.html)

# Usage
Start a docker session with the flag ``--net=host``. Attach container to vscode and start a portforwarding of 5555. Change the port of "localhost:5556" in joy_receiver.py to match the port output by the forwarding. (You can use any method of port fowarding, not just vscode)
Run the publisher script found at: https://github.com/ariarobotics/robotic-autonomy/blob/main/ros2/99_mini_labs/joy_publisher.py

# Credit
Thanks to Abolfazl Babanazari of the Colorado School of Mines for creating the initial code segment that was used to achieve the final joy_receiver.py
