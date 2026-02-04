# Antigravity Skills Marketplace

Welcome to the **Antigravity Skills Marketplace**. This repository contains a collection of specialized "skills" that extend the capabilities of AI agents like **Antigravity** and **Claude Code**.

## What is a Skill?
A skill is a package of logic, instructions, and tools defined in a `SKILL.md` file. It allows an agent to perform complex, domain-specific tasks by following a structured workflow.

## Available Skills

| Skill Name | Description |
| :--- | :--- |
| [**Crypto Investor L2 Scoreboard**](./crypto_investor_l2_scoreboard) | Researches and scores Layer 2 blockchains (Privacy, Gaming, etc.) using live data and an investor-focused scoring model. |

## How to Use
1.  **Clone this repository**:
    ```bash
    git clone https://github.com/your-username/antigravity-skills.git
    ```
2.  **Add to your Agent**:
    *   Copy the specific skill folder (e.g., `crypto_investor_l2_scoreboard`) into your project's `.agent/skills/` directory.
    *   Or, reference the `SKILL.md` path directly in your prompts.

## Contributing
To add a new skill:
1.  Create a new folder for your skill.
2.  Add a `SKILL.md` with your instructions.
3.  Add a `README.md` with usage examples.
4.  Submit a Pull Request.
