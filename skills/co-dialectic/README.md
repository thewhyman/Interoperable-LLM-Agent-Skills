# Co-Dialectic

> **Stop talking AT your AI. Start thinking WITH it.**

A model-agnostic skill that implements bidirectional co-evolution between humans and AI — where both sides get sharper together over time.

## Why "Dialectic"?

**Socratic** = one-directional. The teacher already knows the answer.
**Dialectic** = bidirectional. Neither side has the complete answer. Truth emerges from the tension between two different kinds of intelligence.

This connects to **DBT (Dialectical Behavior Therapy)**: holding two opposing truths simultaneously. In co-dialectic: "I (human) have wisdom AI doesn't" AND "AI has capabilities I don't." Both true. The synthesis exceeds either.

## Three Techniques

| Technique | What You Do | What Changes |
|-----------|------------|--------------|
| **Socratic Prompting** | Ask questions instead of giving instructions | AI derives generative principles, not cached answers |
| **Few-Shot by Example** | Give one concrete scenario | AI generalizes to an entire class of behavior |
| **Chain-of-Thought Steering** | Say "think through this" or "just do it" | You control the AI's cognitive budget |

---

## Installation

### Claude Code

Copy the skill directory into your Claude Code skills folder:

```bash
# Option 1: Use the repo's install script (installs ALL skills)
cd /path/to/llm-agent-skills
python3 agent_skills_install.py --claude-code

# Option 2: Copy just co-dialectic manually
cp -r skills/co-dialectic ~/.claude/skills/co-dialectic
```

Restart Claude Code after installing. The skill activates automatically when triggered.

### Antigravity

```bash
# Option 1: Install script
python3 agent_skills_install.py --antigravity

# Option 2: Manual copy
cp -r skills/co-dialectic ~/.antigravity/skills/co-dialectic
```

Restart your agent session. Verify with: *"What skills do you have available?"*

### OpenAI (ChatGPT, Swarm, Assistants API)

Inject the contents of `SKILL.md` as a system prompt fragment:

```python
import openai

# Read the skill definition
with open("skills/co-dialectic/SKILL.md") as f:
    co_dialectic_prompt = f.read()

client = openai.OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": co_dialectic_prompt},
        {"role": "user", "content": "Help me communicate better with AI"}
    ]
)
```

### LangChain / LangGraph

Add the skill as a system message in your agent's prompt:

```python
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI  # or ChatAnthropic

with open("skills/co-dialectic/SKILL.md") as f:
    co_dialectic_prompt = f.read()

llm = ChatOpenAI(model="gpt-4o")  # works with any LLM
messages = [
    SystemMessage(content=co_dialectic_prompt),
    HumanMessage(content="I want to improve how I work with AI")
]
response = llm.invoke(messages)
```

### Plain Conversation (No Code Required)

Just read `SKILL.md` and start using the three techniques in your next AI conversation — ChatGPT, Claude, Gemini, anything. The flywheel starts turning immediately. No installation needed.

---

## Usage & Trigger Phrases

The skill activates when you use any of these patterns:

| Trigger | What It Does |
|---------|-------------|
| `co-dialectic` / `dialectic mode` | Activates the full skill |
| `improve my prompts` | Starts prompt improvement protocol |
| `teach me to talk to you` | Engages the co-education flywheel |
| Asking a question instead of giving an instruction | Triggers Socratic prompting recognition |
| Giving a concrete scenario to teach a class of behavior | Triggers few-shot recognition |
| `think through this` / `just do it` | Chain-of-thought steering |

---

## Before/After Examples

### Example 1: Socratic Prompting — The Ski Shop Question

**The problem:** A flat instruction produces a flat result — contacts scored on one dimension only.

**Before (instruction-giving):**
```
Score all my contacts for frontier AI job referrals.
```
*Result: A one-dimensional ranked list. Contacts that aren't useful for AI jobs score zero — even though they might be invaluable for other goals.*

**After (Socratic prompting):**
```
When I give you contacts, is it only for Track 1 (frontier AI)?
What if I said I wanted to open a ski shop — who in my network
would light up then?
```
*Result: The AI derived the principle of a "living asset graph" — contacts scored across ALL life dimensions (career, ventures, hobbies, mentorship, personal growth), dynamically re-weighted when context shifts. One question taught infinite generalization.*

**Why it works:** The question forced the AI to reason from first principles rather than retrieve a cached response. The deliberately absurd scenario (ski shop) communicated that the principle must generalize to ANY context, not just the current one.

> *From a real session — see [examples/session-18-real-examples.md](examples/session-18-real-examples.md) for the full transcript.*

---

### Example 2: Few-Shot by Example — Keywords vs. Meta-Concepts

**The problem:** AI learns corrections one keyword at a time instead of extracting the underlying principle.

**Before (abstract instruction):**
```
Always use the richest visual representation when showing me information.
```
*Result: The AI sort-of follows this, but inconsistently — because "richest visual representation" is ambiguous.*

**After (few-shot with meta-question):**
```
When I said "show me their profile picks," I meant profile PICTURES —
actual images. You gave me text descriptions.

Are you going to learn this lesson one keyword at a time,
or as a meta-concept?
```
*Result: The AI extracted the generative principle of "fidelity matching" — always use the richest representation available (images over descriptions, demos over explanations, rendered charts over raw numbers). One correction, applied to everything forever.*

**Why it works:** The concrete error (text instead of images) was the few-shot example. The meta-question ("keyword or meta-concept?") was the forcing function that pushed the AI from a prescriptive patch (`profile picks = pictures`) to a generative principle (`always match or exceed the fidelity of what's being discussed`).

> *From a real session — see [examples/session-18-real-examples.md](examples/session-18-real-examples.md) for the full transcript.*

---

## The Flywheel

```
You correct the AI → AI codifies the lesson as a generative principle
     ↑                                              ↓
You learn a new     ← AI suggests a better  ← AI teaches you back
prompting pattern      prompt for your intent
```

```
Session 1:  Human corrects AI        → AI codifies the lesson
Session 5:  AI applies automatically  → Human notices fewer corrections needed
Session 20: AI suggests improvements  → Human learns new technique
Session 50: Both anticipate each other → Communication becomes telepathic
```

**1% better per day = 37x better per year.**

---

## Attribution

Inspired by Ethan Mollick's [Co-Intelligence](https://oneusefulthing.org). Extended with the human boundaries half (complementary opposites) and operationalized into a repeatable system. DBT connection: dialectical thinking applied to human-AI partnership.

**Recommended learning:** [Vanderbilt University's Prompt Engineering course on LinkedIn Learning](https://www.linkedin.com/learning/) — the foundation for speaking an LLM's language.

## License

MIT
