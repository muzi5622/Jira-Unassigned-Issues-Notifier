# Jira Unassigned Issues Notifier

This script checks for **newly created unassigned Jira issues within the last 5 minutes** and sends notifications to a **Discord channel** using a webhook.

---

## 🚀 Features
- Connects to your Jira instance via API.
- Searches for issues:
  - Created within the last **5 minutes**.
  - Still **Unresolved**.
  - With **no assignee**.
- Sends notifications to a **Discord channel** with issue details.

---

## 🛠 Requirements
Make sure you have the following installed:

```bash
pip install jira discord-webhook
````

---

## ⚙️ Configuration

Edit the script and update the following variables:

```python
user = "email"            # Your Jira account email
api_token = "token"       # Your Jira API token
server = "https://your-domain.atlassian.net"  # Your Jira server URL
webhook_url = "WEBHOOK_URL"  # Discord webhook URL
```

### How to get:

* **Jira API Token**: [Get it here](https://id.atlassian.com/manage-profile/security/api-tokens).
* **Discord Webhook**: [Guide](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks).

---

## ▶️ Usage

Run the script:

```bash
python jira_notifier.py
```

* If no issues are found:

  ```
  No tickets found.
  ```

* If issues exist: They are sent to your configured **Discord channel** with their ID and summary.

---

## 📌 Example Discord Output

```
<img width="760" height="124" alt="image" src="https://github.com/user-attachments/assets/2a4ea960-31d7-4081-9d3a-1f479a1346ce" />


---
