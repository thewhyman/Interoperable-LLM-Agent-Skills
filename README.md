# LLM Skills Marketplace

Welcome to the **LLM Skills Marketplace**. This repository contains a collection of specialized "skills" compliant with the **[LLM Skill Standard](SPEC.md)**.

## Universal Compatibility
These skills are designed to be **tool-agnostic**. They are defined using standard Markdown and can be used by any AI agent or LLM workflow, including:
*   **Antigravity**
*   **Claude Code**
*   **OpenAI Swarm**
*   **LangChain / LangGraph** agents
*   Custom in-house agent frameworks

## What is a Skill?
A skill is a self-contained package of instructions and logic defined in a `SKILL.md` file. By adhering to the [standard](SPEC.md), these skills allow any compatible agent to perform specialized, complex tasks without vendor lock-in.

## Available Skills

| Skill Name | Description |
| :--- | :--- |
| [Crypto Investor L2 Scoreboard](skills/crypto_investor_l2_scoreboard) | Researches and scores L2 blockchains based on adoption and momentum. |

## Usage
1.  **Clone** this repository.
2.  **Point** your agent to the specific `SKILL.md` file you wish to use.

```bash
git clone https://github.com/your-username/llm-skills.git
```

## Contributing
We welcome contributions! Please ensure your skills follow the [Specification](SPEC.md).

1.  Create a new folder in `skills/`.
2.  Create a `SKILL.md` with YAML frontmatter + instructions.
3.  (Optional) Add a `README.md` for human readers.
4.  Submit a Pull Request.
