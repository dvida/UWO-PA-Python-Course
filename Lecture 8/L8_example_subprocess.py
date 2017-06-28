""" In this script, an example how to call external scripts and commands is given. """

import subprocess


# Full path to script you would like to call
script_path = './test.sh'


# If you just want to call an external script or command, you can do this:
subprocess.call(script_path, shell=True)


# And that's it!

###############

# Calling a script and getting the result requires a bit more commands:


# Let us define a command we would like to call, with all the extra options
command = 'uname -a'

# Call the script
p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
 
# Talk with date command i.e. read data from stdout and stderr. Store this info in tuple.
(output, err) = p.communicate()
 
# Wait for date to terminate. Get return returncode #
p_status = p.wait()

# Print script output
print "Command output : ", output