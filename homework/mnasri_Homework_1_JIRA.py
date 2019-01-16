# Python Study Group
# Homework #1: Connect to public JIRA and pull information from a project.

# Reference: https://jira.readthedocs.io/en/master/examples.html

# This script uses client in anonymous mode against jira.atlassian.com 

from jira import JIRA
import re

# Default behavior, client connects to JIRA instance started from Atlassian SDK.
# Override using "options" parameter.
options = {
	'server' : 'https://jira.atlassian.com'}
jira = JIRA(options)

# Get all projects viewable by anynymous users.
projects = jira.projects()

print(projects)

