# LLM Skill Standard Specification

The **LLM Skill Standard** defines a portable, tool-agnostic format for defining capabilities ("skills") that Large Language Models (LLMs) and AI agents can utilize.

## Philosophy

Skills should be:
1.  **Universal**: Writeable in standard Markdown and readable by any LLM.
2.  **Self-Contained**: All instructions, context, and prompts required for the skill reside in a single `SKILL.md` file (or a folder containing it).
3.  **Composable**: Agents can load multiple skills as needed.

## File Structure

A compliant skill resides in its own directory and MUST contain a `SKILL.md` file:

```text
skills/
  ├── my_awesome_skill/
  │   ├── SKILL.md       # Required: The core definition
  │   ├── README.md      # Optional: Human-readable documentation
  │   └── assets/        # Optional: Helper files, images, or schemas
```

## The `SKILL.md` Format

The `SKILL.md` file combines structured metadata (YAML Frontmatter) with natural language instructions.

### 1. YAML Frontmatter
Used by the agent framework to index and select skills. **Compatible with Claude Code.**

```yaml
---
name: skill-name        # Required: Kebab-case name (e.g., 'code-reviewer'). Acts as slash command.
description: string     # Required: Single-sentence summary for semantic routing.
version: 1.0.0          # Optional: Semantic versioning.
author: string          # Optional: Author name or contact.
dependencies:           # Optional: List of required system packages.
  - python3
permissions:            # Optional: Requested permissions/tools.
  allowed-tools:        # Claude Code specific tool allowlist.
    - Bash
    - Read
---
```

## Skill Collections & Installation

To standardized distribution, repositories can define a **Skill Collection** manifest.

### `skills.yaml` Format
Root-level file declaring which skills this repository exports or depends on.

```yaml
skills:
  - name: crypto-investor
    path: skills/crypto_investor_l2_scoreboard
    description: "Analyzes L2 blockchains."
  - name: code-reviewer
    url: "https://github.com/my-org/skills/releases/download/v1.0/code-reviewer.zip"
```

### Installation Standard
Tools should install skills into a standard user directory to ensure cross-tool availability.

*   **Standard Path**: `~/.antigravity/skills` or `~/.claude/skills`
*   **Project Path**: `.agent/skills` (Recommended for project-specific skills)


### 2. Instructions (The Body)
The rest of the file is standard Markdown. It serves as the system prompt or context injection for the agent.

#### Best Practices for Instructions:
*   **Role Definition**: Clearly state what role the agent adopts (e.g., "You are an expert Data Analyst").
*   **Input Format**: Describe what the user will provide.
*   **Step-by-Step Workflow**: Break complex tasks into numbered phases.
*   **Output Format**: Explicitly define how the result should look (Markdown tables, JSON, etc.).
*   **Examples**: Provide few-shot examples if complex reasoning is required.

## Example `SKILL.md`

```markdown
---
name: Code Reviewer
description: Reviews code for security vulnerabilities and style violations.
---

# Code Review Protocol

As an expert Security Auditor, your goal is to review the provided code.

## Steps
1.  **Analyze** the code for common CVEs (SQLi, XSS).
2.  **Check** for stylistic consistency (PEP8 for Python).
3.  **Report** findings in a standardized table.

## Output Format
| Severity | File | Issue | Recommendation |
| :--- | :--- | :--- | :--- |
| High | main.py | SQL Injection | Use parameterized queries |
```
