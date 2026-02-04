# Crypto Investor L2 Scoreboard Skill

This directory contains an agentic skill designed for **Antigravity** or **Claude Code**. 

## Overview
The **Crypto Investor L2 Scoreboard** skill helps investors research and score Layer 2 blockchains. It can:
1.  **Discover** top projects in sectors like *Privacy* and *Gaming* (if no list is provided).
2.  **Analyze** them using live web data from sources like L2BEAT and DefiLlama.
3.  **Score** them based on *Adoption*, *Value Accrual*, and *Momentum*.
4.  **Report** findings in a structured, investor-friendly Markdown format.

## Contents
*   `SKILL.md`: The core instructions file that defines the skill's logic, prompts, and output format.

## Installation / Usage
To use this skill with your AI agent:

1.  **Keep this folder**: Ensure this directory (`Crypto_Investor_L2_Scoreboard_Skill`) is accessible to your agent.
2.  **Import/Reference**:
    *   If your agent tooling supports a `skills` directory (e.g., `.agent/skills`), move this entire folder there.
    *   Otherwise, simply point the agent to the `SKILL.md` path when requesting the task.

## Example Prompts
Once the skill is available to the agent, you can use prompts like:

> "Use the L2 Scoreboard skill to analyze the top Gaming L2s."

> "Run the Investor Scoreboard for 'Aztec', 'Optimism', and 'Taiko'."
