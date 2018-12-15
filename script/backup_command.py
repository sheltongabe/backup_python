#!/usr/bin/python3
##
# @package	script
# @file		backup_command.py
# @brief	Implement the Command Pattern for Backup Commands
#
# @date 	2018-12-15
# @author	sheltongabe

# Import Command class, and ...
try:
	from design_patterns import Command
except:
	print("Unable to import neccassary modules for backup_command.py")
	exit(-1)

##
# @class	BackupCommand
# @brief	Command to execute a specific action related to backups on a workspace
class BackupCommand (Command):

	## Default Constructor, takes a list of workspaces
	def __init__(self, workspaces):
		Command.__init__(self)
		self.__workspaces = workspaces
		self.__BACKUP_PATHS = []
	
	## implement the execute from the command
	def execute(self):
		Command.execute(self)