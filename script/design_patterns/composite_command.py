##
# @package	design_patterns
# @file		composite_command.py
# @brief	Define a command that holds a list of commands
#
# @date		2018-12-30
# @author	sheltongabe

# Imports
try:
	from command import Command
except:
	print('Failed to import neccassary modules for design_patterns/composite_command.py')
	exit(-1)

##
# @class	CompositeCommand
# @brief	A Command that will hold a list of Commands internally, and execute them all when execute is called
class CompositeCommand(Command):
	## Default Constructor
	def __init__(self):
		Command.__init__(self)

		## @property	Commands to be executed
		self.__commands = []
	
	##
	# @brief	Add a command to the CompositeCommand
	# @param	Command		command to be added
	def addCommand(self, command):
		self.__commands.append(command)

	##
	# @brief	Override execute to execute all of the added commands
	def execute(self):
		for command in self.__commands:
			command.execute()