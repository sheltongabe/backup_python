#!/usr/bin/python3

##
# @package	scripts
# @file		test.py
# @brief	Serve to run test-cases on the script
#
# @date		2018-12-14
# @author	sheltongabe

# Attempt imports
try:
	from main import runBackup
except:
	print("Failed to import neccessary modules for tests")
	exit(-1)

runBackup('push', ['wget'])
runBackup('push', ['all'])
runBackup('pull', ['wget'])
runBackup('pull', ['all'])