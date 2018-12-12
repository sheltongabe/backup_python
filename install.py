#!/usr/bin/python3
##
# @file	install.py
# @brief	Setup the directories that are used for this program

_BACKUPS_DIR = './backups/'
_ARCHIVE_DIR = _BACKUPS_DIR + 'archive/'

try:
	import os, os.path
except:
	print("Failed to import required modules")
	exit(-1)

## 
# @brief	Entry for the program, and set's up the directories required
def main():
	if(not makeDir(_BACKUPS_DIR)):
		exit(-1)
	if(not makeDir(_ARCHIVE_DIR)):
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

if(__name__ == "__main__"):
	main()