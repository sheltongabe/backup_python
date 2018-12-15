##
# @package	design_patterns
# @file		command.py
# @brief	Declare the basic structure of the Command Pattern
#
# @date		2018-12-11
# @author	sheltongabe

##
# @class	Command
# @brief	A class with a method, execute, that is overriden by child classes
class Command:

	## Constructor
	def __init__(self):
		pass

	## Method called when the Command is executed, the callee is who has the object
	def execute(self):
		pass