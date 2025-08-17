from jira import JIRA

# ==============================
# 🔑 Authentication details
# ==============================
user = "your-email@example.com"          # Your Jira email
api_token = "your-api-token"             # Jira API token
server = "https://your-domain.atlassian.net"  # Jira server URL

# Connect to Jira
jira = JIRA(server=server, basic_auth=(user, api_token))


# ==============================
# 📝 Create a new Jira issue
# ==============================
new_issue = jira.create_issue(fields={
    "project": {"key": "SCRUM"},                  # Project key
    "summary": "Test issue from Python 🚀",       # Title of the issue
    "description": "Created via Python API",      # Description text
    "issuetype": {"name": "Story"},               # Task / Bug / Story / Incident etc.
    # "priority": {"name": "High"},               # Optional: set priority
    "labels": ["automation", "python-api"],       # Optional: add labels
    # "assignee": {"accountId": "user-account-id"} # Optional: assign directly
})

print(f"✅ Created: {new_issue.key}")


# ==============================
# 🔍 Useful extras (uncomment to use)
# ==============================


# 👉 View all available fields for a project/issuetype:
# meta = jira.createmeta(projectKeys="SCRUM", issuetypeNames="Task", expand="projects.issuetypes.fields")
# fields = meta['projects'][0]['issuetypes'][0]['fields']
# for fid, fdata in fields.items():
#     print(f"{fid} --> {fdata['name']} (Required: {fdata.get('required', False)})")

# 👉 Search issues (example: last 10 unresolved tasks)
# issues = jira.search_issues('project=SCRUM AND resolution=Unresolved ORDER BY created DESC', maxResults=10)
# for issue in issues:
#     print(f"{issue.key}: {issue.fields.summary}")
