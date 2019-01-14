# need to install the packages before able to import.
# Please run:
# > pip install requests
# > pip install jira
# at cmd line first

from jira import JIRA

# using this site as a ref: https://jira.readthedocs.io/en/master/examples.html#searching
# This connects to a JIRA started on your local machine at http://localhost:2990/jira, which not coincidentally is the default address for a JIRA instance started from the Atlassian Plugin SDK.
# You can manually set the JIRA server to use:
options = {
    'server': 'https://jira.atlassian.com'}
jira = JIRA(options)
# Get all projects viewable by anonymous users.
# https://jira.atlassian.com/browse/
projects = jira.projects()

# Summaries of 3 issues created in last 1 days
for issue in jira.search_issues('createdDate >= -1d order by created desc', maxResults=3):
    print('{}: {}'.format(issue.key, issue.fields.summary))

# struggling to write this to file, but able to print to screen!
