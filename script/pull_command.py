##
# @package	script
# @file		pull_command.py
# @brief	define a command that copies from the workspace directory here
#
# @date		2018-12-16
# @author	sheltongabe

# Attempt imports
try:
	from backup_command import BackupCommand
	from configuration import CONFIGURATION
	import subprocess
except:
	print("Error including Backup command and other modules needed for: script/PullCommand")
	exit(-1)

##
# @class	PullCommand
# @brief	Extend the BackupCommand to push files from a workspace to here
class PullCommand (BackupCommand):
	
	## Default Constructor, takes to operate on
	def __init__(self, workspace_name, workspace):
		BackupCommand.__init__(self, workspace_name, workspace)

	## 
	# @brief	Override execute to push for each workspace
	# @return 	boolean		Did the command execute successfully
	def execute(self):
		# Fork a subprocess and wait for its completion
		# Make sure a directory exists for the backup
		completedProcess = subprocess.run(
				['rsync', '-rup', '--chmod=u=rwX,g=,o=', '-z', self.workspace_name, self.workspace],
				cwd=CONFIGURATION['BACKUPS_PATH'], stderr=None)

		return completedProcess.returncode == 0