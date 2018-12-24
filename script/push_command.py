##
# @package	script
# @file		push_command.py
# @brief	define a command that copies from the workspace directory here
#
# @date		2018-12-16
# @author	sheltongabe

# Attempt imports
try:
	from backup_command import BackupCommand
except:
	print("Error including Backup command and other modules needed for: script/PushCommand")
	exit(-1)

##
# @class	PushCommand
# @brief	Extend the BackupCommand to push files from a workspace to here
class PushCommand (BackupCommand):
	
	## Default Constructor, takes to operate on
	def __init__(self, workspace):
		BackupCommand.__init__(self, workspace)

	## Override execute to push for each workspace
	def execute(self):
		pass