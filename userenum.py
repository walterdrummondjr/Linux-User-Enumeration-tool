import subprocess
import logging





# List of commands that will run:
# 1st command: id  - Shows the users id, group id and group membership
# 2nd command: whoami - Shows who you are logged in as
# 3rd command: groups - Shows all groups for the current logged in user
# 4th command: echo $PATH - Shows which directory the current user has access to
# 5th command: grep -e /bin/bash /etc/passwd - Shows any users assigned to the Bash shell
# 6th command: lastlogin - Shows all user’s login name, port, and last login time

commands = "echo '\\033[94mBegnining........ \\033[0m' && id && whoami && groups && echo $PATH && grep -e /bin/bash /etc/passwd && lastlog && echo '\\033[92mEnumeration complete....... \\033[0m'"


#Run commands and displays output to the terminal
output = subprocess.run(commands, shell=True, capture_output=True, text=True)


# Displays commmands output to the terminal
print(output.stdout)
