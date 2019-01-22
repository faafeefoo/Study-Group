# need to install the package before able to import.
# Please run:
# > pip install jira
# at cmd line first

from jira import JIRA
import datetime
yest = datetime.datetime.strftime(datetime.datetime.now()-datetime.timedelta(3),'%Y-%m-%d')
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
f.writelines("# JIRA JQL results \n Query last 10 issues created " + yest + '\n \n')
# Summaries of 3 issues created in last 1 days
f.writelines("| Key | Icon | Requestor | Summary | \n")
f.writelines("| --- | --- | ---| --- | \n")
for issue in jira.search_issues('createdDate <= ' + yest + ' order by created desc', maxResults=5):
    f.writelines('| [{}](https://jira.atlassian.com/browse/{}) | ![icon]({} "{}") | _by_ **{}**' .format(issue.key, issue.key, issue.fields.issuetype.iconUrl, issue.fields.issuetype.name, issue.fields.reporter.displayName))
    f.writelines('| {} |\n'.format(issue.fields.summary))
    f.writelines(issue.raw['fields'])
f.close()
