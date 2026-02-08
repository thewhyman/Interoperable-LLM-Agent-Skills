---
name: LinkedIn Post Manager
description: Manages a queue of LinkedIn posts and automates the posting process using browser automation.
---

# LinkedIn Post Manager

This skill helps the user maintain a consistent LinkedIn presence by managing a content queue and automating the posting workflow.

## Commands

- `check linkedin queue`: Checks if any LinkedIn posts are scheduled and ready.
- `add linkedin post`: Prompts for content and time. If time is omitted, recommends the next best window based on engagement data (Tue/Wed/Thu), then adds to the queue.
- `remove linkedin post <id>`: Removes a specific post from the queue.
- `ship linkedin post <id>`: Automates the posting process for a specific LinkedIn item.

## Workflow: Shipping a LinkedIn Post

When a LinkedIn post is due or requested:

1.  **Preparation**: Read from the centralized store: `~/.agentskills/linkedin_post_queue.json`.
2.  **Notification**: Inform the user: "I'm ready to ship the [Topic] post. I'll open LinkedIn and handle the typing for you."
3.  **Browser Automation**:
    - Use `browser_subagent` to navigate to `https://www.linkedin.com/feed/`.
    - Find and click the "Start a post" button/field.
    - Type the content exactly as it appears in the queue.
    - **Wait for User Confirmation**: Do NOT click the final "Post" button automatically unless explicitly told to. Ask the user: "The post is ready for your final review. Should I hit send?"
4.  **Completion**: Once posted, update the status in `~/.agentskills/linkedin_post_queue.json` to `posted`.

## Trigger Mechanism

The agent should check the `~/.agentskills/linkedin_post_queue.json` file at the start of every session. If `current_time > scheduled_at` for any `pending` post, proactively notify the user.
