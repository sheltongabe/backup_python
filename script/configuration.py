##
# @package	script
# @file		configuration.py
# @brief	Load the configuration file for the script into a shared dictionary
#
# @date		2018-12-16
# @author	sheltongabe

# Path to the configuration file
__CONFIGURATION_FILE = "../configuration.json"

# Configuration
CONFIGURATION = {}

# Try to import required modules to read configuration file
# Then read the configuration file
try:
	import json
	with open(__CONFIGURATION_FILE) as file:
		CONFIGURATION = json.load(file)
except:
	print("Failed to load configuration file for script: " + __CONFIGURATION_FILE)
	exit(-1)