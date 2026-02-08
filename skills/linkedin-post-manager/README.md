# LinkedIn Post Manager Skill

Manage your LinkedIn brand strategy and automate your posting workflow directly from your AI agent.

## Components
- **`~/.agentskills/linkedin_post_queue.json`**: The centralized content store (shared across agents).
- **`queue_trigger_service.py`**: Python engine for queue status, local notifications, and automatic setup.
- **`SKILL.md`**: Instruction set for agent-driven browser automation.

## Design Rationale: Why Browser vs. API?
We chose **Browser Automation** over an official LinkedIn MCP/API for three reasons:
1. **Frictionless Setup**: No API keys or developer approvals required.
2. **Account Safety**: Automation mimics human preparation, keeping you in control.
3. **Session Persistence**: Leverages your existing authenticated browser session.

## 🚀 Human-in-the-Loop Usage

### 1. Via Agent (Natural Language)
Just tell your agent:
- **Checking**: "Show me my linkedin queue"
- **Adding**: "Add a new linkedin post for Friday at 9 AM."
- **Removing**: "Remove the post about ResilienceAI from my linkedin queue."
- **Shipping**: "Ship the linkedin post for ResilienceAI."

### 2. Via CLI (For Power Users)
```bash
# See all posts
python3 queue_trigger_service.py list

# Remove a post
python3 queue_trigger_service.py remove --id [POST_ID]
```

## 🖥️ Platform Support & Notifications

### macOS (Full Support)
The proactive notification system is built for macOS using `LaunchAgents`.
1. Edit `com.agentskills.linkedin.plist` to set your absolute path.
2. Symlink and load:
```bash
ln -sf $(pwd)/com.agentskills.linkedin.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.agentskills.linkedin.plist
```

### Windows/Linux (Manual Trigger)
The browser automation works on all platforms. However, the proactive desktop notification (`queue_trigger_service.py check`) is currently tailored for macOS. 
- **Windows Users**: You can still use the queue manually. Simply ask the agent to "Check my queue" at the start of your session. 
- **Cross-Platform Note**: The core `queue_trigger_service.py check` logic works on any OS with Python, but the visual banner notification requires `osascript` (macOS).

## 🛡️ Security & macOS Fixes

### macOS Quarantine Flag
This skill automatically clears the quarantine flag when you run the `setup` command:
```bash
python3 queue_trigger_service.py setup
```
If you encounter permission issues later, you can also run:
```bash
xattr -d com.apple.quarantine ~/.claude/skills/linkedin-post-manager/*.py
```
*(Similarly for `~/.antigravity` or `~/.gemini`)*

### Browser session
This skill uses your **existing browser session**. It does not require your LinkedIn password.
