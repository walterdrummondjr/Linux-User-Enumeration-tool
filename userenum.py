import subprocess
import logging





# List of commands that will run
commands = "echo '\\033[94mBegnining........ \\033[0m' && id && who && whoami && groups && echo $PATH && grep -e /bin/bash /etc/passwd && lastlog && echo '\\033[92mEnumeration complete\\033[0m'"


#Run commands and displays output to the terminal
output = subprocess.run(commands, shell=True, capture_output=True, text=True)



print(output.stdout)
