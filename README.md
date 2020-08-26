# Django Feed Reader

## Setup mySQL with a command line:
    Run this command on your terminal, and after few seconds, mysql will be listening on port 5051:
      docker pull mysql:8.0.1 && docker run --name mysql_server -e MYSQL_ALLOW_EMPTY_PASSWORD=1 -p 5051:3306 -d mysql:8.0.1

    Prerequisite: MacOS or Ubuntu/ Linux, thus this command is untested on Ubuntu.
                  Docker is installed and running
                  Port 5051 is unused and ready to be used

    Explanation: Firstly, I pull an image of mysql (8.0.1) which is published on Docker hub
                 Then I run the image with:
                      name : mysql_server
                      MYSQL_ALLOW_EMPTY_PASSWORD=1 : No need to provide a password
                      -p 5051:3306 : Map the port 3306 of the container to our local port 5051
## Installation:

#### Step 1: Create and activate a virtual env
    For this project, I used virtualenv, however you can choose whichever you like. Make sure to activate it after configuring.
#### Step 2: Install all required library, using this command:
    pip3 install -r requirement.txt

## Grab items with function grab_items.py:
    Command: python3 grab_items.py -u <urls> -p <absolute_path_to_log_file>

    -u, --urls: list of urls, separated with commas
    -p, --path: absolute path to log file

    This command will get the rss feed from urls and print out a list of items (JSON format). 
    It also add new record into the provided log file (create new if needed)
