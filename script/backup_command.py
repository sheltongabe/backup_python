##
# @package	script
# @file		backup_command.py
# @brief	Implement the Command Pattern for Backup Commands
#
# @date 	2018-12-24
# @author	sheltongabe

# Import Command class, and ...
try:
	from design_patterns.command import Command
except:
	print("Unable to import neccassary modules for backup_command.py")
	exit(-1)

##
# @class	BackupCommand
# @brief	Command to execute a specific action related to backups on a workspace
class BackupCommand (Command):

	## Default Constructor, takes a workspace to operate on
	def __init__(self, workspace_name, workspace):
		Command.__init__(self)

		## Workspace name
		self.workspace_name = workspace_name
		## Workspace Source Path
		self.workspace = workspace

	## implement the execute from the command
	def execute(self):
		Command.execute(self)