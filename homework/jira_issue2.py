# need to install the package before able to import.
# Please run:
# > pip install jira
# at cmd line first

from jira import JIRA
import datetime
date1 = datetime.datetime.strftime(datetime.datetime.now()-datetime.timedelta(2),'%Y-%m-%d')
keep: int = '10'
# using this site as a ref: https://jira.readthedocs.io/en/master/examples.html#searching
# This connects to a JIRA started on your local machine at http://localhost:2990/jira, which not coincidentally is the default address for a JIRA instance started from the Atlassian Plugin SDK.
# You can manually set the JIRA server to use:
options = {
    'server': 'https://jira.atlassian.com'}
jira = JIRA(options)
# Get all projects viewable by anonymous users.
# https://jira.atlassian.com/browse/
projects = jira.projects()
f = open("jira_output2.md","w")
f.writelines("# JIRA JQL results \n Query last **"+keep+"** issues created <span style=\"color:blue\"> " + date1 + '</span> \n \n')
# Summaries of last 'keep' issues created in last 'date1' days
f.writelines("| Key | Icon | Requester | Due Date | Status | Summary | \n")
f.writelines("| --- | --- | ---| --- | --- | --- | \n")
for issue in jira.search_issues('createdDate <= ' + date1 + ' order by created desc', maxResults = keep):
    f.writelines('| [{}](https://jira.atlassian.com/browse/{}) | ![icon]({} "{}") | **{}**' .format(issue.key, issue.key, issue.fields.issuetype.iconUrl, issue.fields.issuetype.name, issue.fields.reporter.displayName))
    f.writelines('| {} | {} | {} |\n'.format(issue.fields.duedate, issue.fields.status, issue.fields.summary))

f.close()
