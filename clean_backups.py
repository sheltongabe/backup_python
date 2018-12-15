#!/usr/bin/python3

##
# @file		clean_backups.py
# @brief	Reset the backup storage, mostly for debugging
# @details
# Delete all of the files in the backup and archive folder
# restore the folder structure
#
# @date		2018-12-15
# @author	sheltongabe

# Attempt the imports
try:
	import shutil, json

	# Grab the path to the backups from the install module
	from install import _BACKUPS_DIR, _ARCHIVE_DIR, makeDir
except:
	print("Failed to import neccassary modules.")
	exit(-1)

##
# @brief	Wipe and rebuild the backups folder
def cleanBackups():
	# Delete all files and directories in including _BACKUPS_DIR
	shutil.rmtree(_BACKUPS_DIR, ignore_errors=True)

	# Rebuild the structure
	if(not (makeDir(_BACKUPS_DIR) and makeDir(_ARCHIVE_DIR))):
		exit(-1)

## Entry point for the program
def main():
	cleanBackups()

if(__name__ == "__main__"):
	main()