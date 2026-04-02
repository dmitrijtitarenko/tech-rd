---
name: Scheduling and Monitoring
description: >
  Automated technology monitoring with three modes: Watchlist (track specific technologies),
  Triggers (condition-based alerts), and Digest (curated weekly newsletter). Uses the
  schedule skill for task automation. Triggered by "monitor", "watch", "alert me",
  "weekly digest", "track changes".
---

# Scheduling and Monitoring

## Three Monitoring Modes

### Mode 1: Watchlist

User maintains a list of specific technologies to monitor. Weekly automated scans compare current state to previous snapshot.

Alerts trigger on:
- New releases or version changes
- Security advisories (CVE, deprecation warnings)
- Adoption spike signals
- End-of-life or deprecation announcements
- Breaking API changes

Output: Change report with diffs highlighting what changed and why it matters.

### Mode 2: Triggers

User defines conditions that, when met, automatically generate alerts.

Example trigger conditions:
- "Alert if dependency gets critical CVE"
- "Notify on new NIST AI safety standard"
- "Alert when competing product adds feature X"
- "Notify if adoption rate exceeds 30% in our industry"

Output: Alert notification sent immediately when condition is met. Includes context and recommended action.

### Mode 3: Digest

Broad weekly or daily scan across user-relevant technology domains. Personalized based on research history and stated priorities.

Captures:
- Major releases in tracked categories
- Emerging patterns and trends
- Industry shifts and announcements
- Standards updates and compliance changes

Output: Curated tech newsletter formatted for Notion or Slack delivery.

## Implementation

Uses scheduled-tasks MCP tools:
- `create_scheduled_task`: Set up recurring or one-time monitoring
- `list_scheduled_tasks`: View all active monitors
- `update_scheduled_task`: Modify existing schedules

Scheduling options:
- Cron expressions for recurring scans (daily, weekly, monthly)
- One-time scans for specific dates
- Manual trigger for ad-hoc checks

## Storage and Delivery

Results saved to:
- Notion KB if enabled (structured database records)
- Slack channel for real-time notifications
- Markdown files for archival and analysis

Each result includes:
- Discovery date
- Technology identifier
- Change type and description
- Confidence level
- Recommended next steps
