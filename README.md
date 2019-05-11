# python-port-scanner
It is a python based side project for scanning open ports in a server that works with windows only if 'tnc' command is enabled. Other OS and commands will be added based on requests and after completion of the windows part.

## Code Approval and Branch Structure:
The base branch is 'master -> origin/master'.
The branch where we develop and review the code and changes is 'develop -> origin/develop'
Contributors should first create there own branches with the following naming conventions:
1. Contributor Tag + _ + Task name phrase + _ + date today in the format (dd_mm_yyyy)
2. Contributor Tag is the name by which contributor commit the code (eg, Dhruv, thisisdg etc.)
3. Task name is the phrase of the task subject that you are going to work with in that branch.
4. And the date  on which you have created that branch.
5. So according to the above conventions, the name of the branch would be like the following:
    thisisdg_cascadedInputs_5_11_2019
6. Every conflict will be resolved in the same branch that you are working with. The PR will be raised pointing to develop branch and then the code will be review in develop branch.

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
