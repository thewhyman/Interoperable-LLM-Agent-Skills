---
name: Crypto Investor L2 Scoreboard
description: An agentic skill that researches Layer 2 blockchains and generates an investment-focused scoreboard. Provide a list of L2s or sectors or autonomously discovers top projects in **Privacy** and **Gaming**.
---

# Crypto Investor L2 Scoreboard Skill

This skill analyzes Layer 2 (L2) blockchains using live web data to generate a scored report from a crypto investor's perspective. It either accepts a list of L2s or sectors or autonomously discovers top projects in **Privacy** and **Gaming**.

## Input Format

The user may provide:
1.  **A specific JSON list**.
2.  **A broad request** (e.g., "Find and score the top Privacy and Gaming L2s").

## Instructions for the Agent

### Phase 1: Discovery (Constructing the List)
**If the user DID NOT provide a specific list of L2s:**
1.  **Sectors**: Use sector provided by the user or default to "Privacy", "Gaming".
2.  **Search for Leaders**: Perform web searches to identify the top 3-5 active projects in each sector.
    *   *Queries*: "top privacy layer 2 coins 2024", "best crypto gaming L2s by active users", "upcoming privacy L2 mainnets".
3.  **Filter**: Prioritize projects that are active (Mainnet) or high-profile upcoming (Testnet/Hype).
4.  **Construct Scope**: Create the `l2_list` from these findings. Use standard "Blue Chip" L2s (Arbitrum One, Base, Optimism) as **Baselines** for comparison.

### Phase 2: Detailed Analysis (Data Collection)
**For each L2 in the constructed scope:**
1.  **Execute Web Searches** (Focus on "Investor Lens" - last 30 days).
2.  **Extract Key Metrics** for the 3 Scoring Pillars:
    *   **Adoption**: user counts, transaction volume, active games/apps.
    *   **Value Accrual**: revenue (fees), token utility, TVL quality (stablecoins vs. native tokens).
    *   **Momentum**: growth rate of metrics, social sentiment/hype, recent partnerships, shipping cadence.

### Phase 3: Scoring & Reporting
1.  **Calculate Component Scores** (🟢 Bullish, 🟡 Neutral, 🔴 Bearish, ⚪ Unknown):
    *   **Adoption Score**: Is it being used? (Comparatively).
    *   **Value Accrual Score**: Is it sustainable/profitable?
    *   **Momentum Score**: Is it accelerating right now?S

2.  **Categorize Leaders**:
    *   Identify projects fitting specific archetypes: *Asymmetric Upside*, *Real Usage Today*, *Capital Durability*, *Highest Tech Risk/Reward*, *Needs Proof Soon*.

3.  **Generate Output**:
    The final report MUST be a clear, investor-readable Markdown document structured exactly as follows:

    #### 1. Scoreboard Table
    | L2 | Category | Adoption | Value | Momentum | The "One Sentence Read" |
    | :--- | :--- | :---: | :---: | :---: | :--- |
    | [Name] | [Sector] | [Score] | [Score] | [Score] | [Concise investor thesis] |

    #### 2. Leaders by Thesis
    *   **Asymmetric Upside**: [List L2s with high potential return vs risk]
    *   **Real Usage Today**: [List L2s with actual current traction]
    *   **Capital Durability**: [List L2s safe for parking capital]
    *   **Highest Tech Risk/Reward**: [List L2s with unproven but revolutionary tech]
    *   **Needs Proof Soon**: [List L2s that are lagging or over-promised]

    #### 3. Watchlist Questions
    *   "Is momentum improving without incentives?"
    *   "Is adoption diversifying across apps?"
    *   "Is value accrual rising per user (not just TVL spikes)?"
    *   *(Add any specific project-related questions here)*

    #### 4. Notes & Caveats
    *   "Privacy L2s: adoption/retention may be structurally under-visible; weight dev/roadmap more."
    *   "Gaming L2s: expect bursty tx patterns; retention + launch cadence matter more than fees."
    *   *(Add any additional observations)*
