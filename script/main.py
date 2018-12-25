#!/usr/bin/python3
##
# @package	script
# @file		main.py
# @brief	Entry point for the main script that handles backup requests
#
# @date		2018-12-15
# @author	sheltongabe

# Attempt neccassary Imports
try:
	from sys import argv
	from backup_command_abstract_factory import BackupCommandAbstractFactory
except:
	print("Unable to import sys in script/main.py")
	exit(-1)

##
# @brief	Workhorse function that will actually create and execute the command that is inputed,
# 			on the workspace specified
# @details
# Do any validation that is needed on the parameters, construct, and execute the command
#
# @param	string	Action / command
# @param	string	Workspace-name (lookup in the configuration file)
def runBackup(action, workspaceNames):
	# AbstractFactory to handle construction of all of the Commands
	factory = BackupCommandAbstractFactory()

	# Build Commands
	commands = factory.build(action[0], workspaceNames)

	# Run Commands
	for command in commands:
		command.execute()

## Entry point for backup has 2 parameters in addition to the exectuable: (action, workspace)
def main():
	# If there are not precisely 3 arguments (executable, action, workspace), exit
	if(not len(argv) >= 3):
		print("Insufficient arguments:")
		print("\tNeed to name an action (push, pull, sync, archcive, unarchive)")
		print("\tAnd to name a workspace-name, or all to operate on all workspaces.")
		exit(-1)
	else:
		# Run the backup with (action, workspace-name)
		runBackup(argv[1], argv[2:])

if(__name__ == "__main__"):
	main()