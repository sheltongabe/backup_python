##
# @package	script
# @file		sync_command.py
# @brief	extend the CompositeCommand to define a pull then push to the workspace to sync them up
#
# @date		2018-12-30
# @author	sheltongabe

# Imports
try:
	from design_patterns.composite_command import CompositeCommand
	from pull_command import PullCommand
	from push_command import PushCommand
	from configuration import CONFIGURATION
except:
	print('Imports for File: scripts/sync_command.py failed')

##
# @class	SyncCommand
# @brief	Extend the CompositeCommand to define a pull and push between the worksapce and backup to sync them
class SyncCommand(CompositeCommand):
	## Default Constructor
	def __init__(self):
		pass