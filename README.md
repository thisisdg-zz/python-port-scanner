# python-port-scanner
It is a python based side project for scanning open ports in a server that works with windows only if 'tnc' command is enabled. Other OS and commands will be added based on requests and after completion of the windows part.

## How to run it?
1. Clone this repository to your local drive.
2. Navigate to the path where python-port-scanner folder is located in your local directory.
3. On the root of this repository, check if there is a file name 'portscanner.py'.
4. Open this same path in cmd or your local terminal.
5. Write the following in the cmd:
    python portscanner.py
6. Then python script will start running and then enter inputs according to the flow and requirement.

## Current status of the project:

### Currently following is functional:
1. Accepts a remote IP.
2. Scans all 65536 ports
3. Custom range of ports can be added
4. Status is displayed whether the port is busy or at 'LISTENING' state that is clearly displayed by 'TcpTestSucceeded'.
5. Inputs are not taken by sys.argv[].

### Dependencies:
1. Python 3.x
2. Python package: re, subprocess, time
3. Other python tools that might be required: pip, pyinstaller
4. Editors: Pycharm, notepad++, VS Code or any upto your liking.

### Bugs at top priority:
1. Result should be displayed in a more user friendly manner.
2. Cascaded input of range.
3. There is no fallback condition if the start value is greated than end value in the custom range inputs.
