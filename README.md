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
