"""
directory_utilities.py
By: JOR
Date: 01OCT23
Forked from: JOR IAC notes
"""

import os, platform

# Define global variables
current_working_directory = None

def detect_os()->str:
    # Detect the OS in use
    return platform.system()

def detect_working_directory()->str:
    # Returns the directory this script was run from
    return os.getcwd()
