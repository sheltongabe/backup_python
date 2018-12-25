##
# @package	script
# @file		backup_command_abstract_factory.py
# @brief	Setup Abstract Factory for building commands
#
# @date		2018-12-24
# @author	sheltongabe

# Attempt imports
try:
	from design_patterns.abstract_factory import AbstractFactory
	from push_command import PushCommand
	from configuration import CONFIGURATION
except:
	print("Failed to import neccassary items in backup_command_abstract_factory.py.")
	exit(-1)

##
# @class 	BackupCommandAbstractFactory
# @brief	Construct backup commands based on the inputed action and list of workspaces-names
class BackupCommandAbstractFactory(AbstractFactory):

	## Default Constructor
	def __init__(self):
		AbstractFactory.__init__(self)

		# Create the map for the building functions based on the actions
		BackupCommandAbstractFactory.__BUILD_INDEX = {
			"push" : self.buildPushCommand
		}
	
	##
	# @brief	The main build function that is the entry, 
	# @details	
	# It takes in an action, and a list of workspace-names.  It will
	# determine the path of the workspaces from the configuration file.
	# If the workspace is not found it will print an error and continue to
	# building the next one, if all is specified as the first workspace,
	# all the workspaces will be affacted.
	#
	# @param	string		Action to take
	# @param	[list]		List of workspace-names
	# @return	[list]		List of built commands
	def build(self, action, workspaceNames):
		# Get workspace paths from workspace names
		workspaces = self.getWorkspaces(workspaceNames)

		# Build a list of commands from the workspace paths with the __BUILD_INDEX
		commandList = []
		for workspaceName in workspaces:
			commandList.append(BackupCommandAbstractFactory.__BUILD_INDEX[action](
					workspaceName, workspaces[workspaceName]))
		
		return commandList

	##
	# @brief	Take in the workspace names and return the workspace paths
	#
	# @param	[list]		list of workspace names
	# @return	{dict}		dictionary of workspace names and paths
	def getWorkspaces(self, workspaceNames):
		# List of workspace paths
		workspacePaths = {}

		# First check if the first element is 'all', in which case return all of the workspaces
		if(workspaceNames[0] == "all"):
			for key in CONFIGURATION['workspaces']:
				workspacePaths[key] = CONFIGURATION['workspaces'][key]

		else:
			for workspaceName in workspaceNames:
				workspacePaths[workspaceName] = CONFIGURATION['workspaces'][workspaceName]
		
		return workspacePaths
	
	## Build a PushCommand
	def buildPushCommand(self, workspace):
		return PushCommand(workspace)