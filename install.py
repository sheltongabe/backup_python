#!/usr/bin/python3
##
# @file	install.py
# @brief	Setup the directories that are used for this program
# @date		2018-12-15
# @author	sheltongabe

# You need to rename configuration-example.json -> configuration.json
_CONFIGURATION_FILE = "./configuration.json"

# Import required modules / packages
try:
	import os, os.path, json
except:
	print("Failed to import required modules")
	exit(-1)

# Import Configurations
try:
	with open(_CONFIGURATION_FILE) as json_file:
		json_data = json.load(json_file)
		_BACKUPS_DIR = json_data["BACKUPS_PATH"]
		_ARCHIVE_DIR = _BACKUPS_DIR + 'archive/'
except:
	print("Failed to read configuration file: " + _CONFIGURATION_FILE)
	exit(-1)

_INSTALL_DIRS = (_BACKUPS_DIR, _ARCHIVE_DIR)

##
# @brief	Setup directories for the program
def createInstallDirs():
	for dir in _INSTALL_DIRS:
		if(not makeDir(dir)):
			exit(-1)

##
# @brief	Make the directory passed
# @param	string	Path to directory
# @return	False	if the creation fails
# @return	True	if it is successful
def makeDir(path):
	# Try and make the directory to hold archives
	try:
		if(os.path.exists(path)):
			print("Error: Directory " + path + " already exists")
		else:
			os.makedirs(path, mode=0o700)
	except:
		print("Failed to create the " + path + " directory.")
		return False

	return True

## 
# @brief	Entry for the program, and set's up the directories required
def main():
	createInstallDirs()

if(__name__ == "__main__"):
	main()