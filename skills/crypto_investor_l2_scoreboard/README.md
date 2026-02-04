# Crypto Investor L2 Scoreboard Skill

This directory contains an agentic skill describing how to research and score Layer 2 blockchains, adhering to the [LLM Skill Standard](../../SPEC.md).

## Overview
The **Crypto Investor L2 Scoreboard** skill helps investors research and score Layer 2 blockchains. It can:
1.  **Discover** top projects in sectors like *Privacy* and *Gaming* (if no list is provided).
2.  **Analyze** them using live web data from sources like L2BEAT and DefiLlama.
3.  **Score** them based on *Adoption*, *Value Accrual*, and *Momentum*.
4.  **Report** findings in a structured, investor-friendly Markdown format.

## Contents
*   `SKILL.md`: The core instructions file that defines the skill's logic, prompts, and output format.

## Usage
To use this skill with your AI agent:

1.  **Ensure Access**: Make sure this directory is accessible to your agent.
2.  **Reference**: Provide the agent with the path to `SKILL.md` (e.g., via a `view_file` tool or by placing it in the agent's skills directory).

## Example Prompts
Once the skill is available to the agent, you can use prompts like:

> "Use the L2 Scoreboard skill to analyze the top Gaming L2s."

> "Run the Investor Scoreboard for 'Aztec', 'Optimism', and 'Taiko'."
