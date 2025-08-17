from jira import JIRA
from discord_webhook import DiscordWebhook

# EDIT THESE BEOFRE RUNNING THE SCRIPT.
user = "email"            # Your Jira account email
api_token = "token"       # Your Jira API token
server = "https://your-domain.atlassian.net"  # Your Jira server URL
webhook_url = "WEBHOOK_URL"  # Discord webhook URL

header = "🕔 Unassigned Jira Issues Created in the Last 5 Minutes 🕔"
# Connect to Jira
jira = JIRA(server=server, basic_auth=(user, api_token))

# Get all tickets

tickets = jira.search_issues('created >= -5m AND resolution = Unresolved AND assignee IS empty ORDER BY created DESC')

total = len(tickets)

if total == 0:
    print("No tickets found.")
else:
    webhook = DiscordWebhook(url=webhook_url, content=header)
    response = webhook.execute()

    for ticket in tickets:
        message_content = f"Ticket ID: {ticket.id}, Summary: {ticket.fields.summary}"
        webhook = DiscordWebhook(url=webhook_url, content=message_content)
        response = webhook.execute()
    






