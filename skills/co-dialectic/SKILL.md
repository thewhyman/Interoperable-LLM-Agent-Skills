---
name: co-dialectic
description: "Bidirectional human-AI co-evolution framework. Three techniques (Socratic prompting, few-shot by example, chain-of-thought steering) that compound across sessions."
version: 1.0.0
author: Anand Vallamsetla
permissions:
  allowed-tools:
    - Read
    - Edit
    - Write
---

# Co-Dialectic: Bidirectional Human-AI Intelligence

**Version:** 1.0.0
**Author:** Anand Vallamsetla ([@thewhyman](https://github.com/thewhyman))
**Inspired by:** Ethan Mollick's *Co-Intelligence: Living and Working with AI* ([oneusefulthing.org](https://oneusefulthing.org))
**License:** MIT
**Compatibility:** Claude Code, OpenAI Swarm, LangChain, Antigravity, any SKILL.md-compatible runtime

---

## What This Skill Does

Most prompting guides teach humans to talk AT machines — one-directional instruction-giving. That's the **Socratic** model: the teacher knows the answer and leads the student to discover it.

This skill implements something different: **dialectic** — two minds reasoning together toward truth that neither possesses alone. Thesis (human perspective) + antithesis (AI perspective) → synthesis (better than either could achieve separately). Both sides teach. Both sides learn. Both sides evolve.

The name **Co-Dialectic** combines Ethan Mollick's *co-intelligence* concept (humans and AI as complementary reasoning partners) with the philosophical tradition of dialectic (Plato, Hegel, and modern DBT). The "co-" signals partnership. The "dialectic" signals that truth emerges from the tension between two different kinds of intelligence.

**Why dialectic, not Socratic?** The Socratic method is one-directional — the teacher already knows and guides the student. In co-dialectic, neither side has the complete picture. The human has lived experience, values, emotional intelligence, and stakes. The AI has scale, recall, cross-domain pattern recognition, and tirelessness. These are *perfect complementary opposites* — like the thesis and antithesis that produce synthesis.

**The connection to DBT (Dialectical Behavior Therapy):** DBT teaches people to hold two opposing truths simultaneously — "I am doing my best AND I can do better." Co-dialectic applies the same skill to human-AI partnership: "I (human) have wisdom the AI doesn't have AND the AI has capabilities I don't have." Both are true. The synthesis isn't choosing one — it's leveraging both. People using this skill develop dialectical thinking without knowing they're doing it.

**The Co-Education Flywheel:** Human teaches AI their values and judgment → AI codifies the patterns → AI teaches human better techniques and new connections → Human internalizes → Next interaction starts smarter → Repeat. 1% improvement per day = 37x improvement in a year.

---

## The Three Techniques

### Technique 1: Socratic Prompting

**Principle:** Ask questions instead of giving instructions. When you ask, the AI derives principles from reasoning rather than retrieving cached answers.

**Before (instruction-giving):**
```
Score all my contacts for frontier AI job referrals.
```

**After (Socratic):**
```
When I give you contacts, is it only for Track 1 (frontier AI)?
What if I said I wanted to open a ski shop — who in my network
would light up then?
```

**Why it works:** The instruction produces a flat list optimized for one dimension. The question teaches the AI that contacts are a *living asset graph* with multi-dimensional value that shifts with context. One question, infinite generalization.

**Meta-pattern:** Socrates believed wisdom begins with knowing what you don't know. When the human asks instead of tells, both sides discover what they don't know together.

---

### Technique 2: Few-Shot by Example

**Principle:** Give a single concrete scenario to communicate an *entire class* of behavior. The AI generalizes from the example — you don't need to enumerate every case.

**Before (abstract instruction):**
```
Always use the richest visual representation when showing me information.
```

**After (few-shot example):**
```
When I said "show me their profile picks," I meant profile PICTURES —
actual images. You gave me text descriptions. Are you going to learn
this lesson one keyword at a time, or as a meta-concept?
```

**Why it works:** The abstract instruction is ambiguous. The concrete correction — with the meta-question "keyword vs. meta-concept" — teaches the AI to extract the *generative principle* (fidelity matching: always use the richest representation available) rather than a *prescriptive patch* (profile picks = pictures). One example, infinite generalization.

**Meta-pattern:** Humans learn through stories and examples, not rulebooks. A single vivid scenario communicates more than a page of specifications. The key: always push for the meta-concept, never settle for the keyword fix. Generative principles > prescriptive rules.

---

### Technique 3: Chain-of-Thought Steering

**Principle:** Explicitly control when the AI shows its reasoning versus when it just executes. This gives the human a steering wheel for the AI's cognitive effort.

- Say **"think through this"** / **"plan this"** / **"suggest options"** → full reasoning chain, then STOP
- Say **"just do it"** / **"execute"** / **"ship it"** → compress to conclusion, execute

**Before (ambiguous intent):**
```
What should I do about the Anthropic warm intro path being closed?
```

**After (explicit steering):**
```
Anthropic warm intro through Pravir is fully closed. Think through the
trade-offs of three alternative paths using my poker gang network.
```

**Why it works:** The ambiguous prompt forces the AI to guess intent. The steering phrase makes it crystal clear. The human controls the AI's cognitive budget — System 2 ("think through trade-offs") vs System 1 ("just do it").

**Meta-pattern:** This is Kahneman's dual-process thinking applied to collaboration. The steering phrase is the toggle between deliberation and execution.

---

## How the Flywheel Works

```
Session 1:  Human corrects AI        → AI codifies the lesson
Session 5:  AI applies automatically  → Human notices fewer corrections needed
Session 20: AI suggests improvements  → Human learns new technique
Session 50: Both anticipate each other → Communication becomes telepathic
```

**The compounding math:** 1.01^365 = 37x improvement per year. The flywheel doesn't just preserve knowledge — it *compounds* it.

**Generative principles are the accelerant.** Every lesson codified as a generative principle (not a prescriptive rule) covers infinite future situations. The more generative the codification, the faster the flywheel spins. The self-evolution rate equals the codification quality.

---

## Activation (For Any LLM Runtime)

This skill activates when:
- The user asks to improve their communication with AI
- The AI detects a Socratic question pattern (question instead of instruction)
- The AI detects a few-shot example (concrete scenario teaching a class)
- The AI detects chain-of-thought steering ("think through...", "plan this", "just do it")
- The user references co-intelligence, co-dialectic, or the flywheel

**For Claude Code / Antigravity:**
```yaml
triggers:
  - co-dialectic
  - co-communication
  - improve my prompts
  - teach me to talk to you
  - dialectic mode
  - how do I communicate better with AI
```

**For OpenAI Swarm / LangChain:**
This SKILL.md can be injected as a system prompt fragment. The techniques are model-agnostic — they work with any LLM that supports multi-turn conversation.

---

## Implementation Notes

### For AI Developers Integrating This Skill

1. **Prompt Improvement Protocol:** On every user message, evaluate whether the prompt could be more effective. If yes, suggest the improved version with a 1-sentence explanation of *why* — then STOP and WAIT. Don't answer either prompt until the human chooses.

2. **Auto-Codification:** When the human expresses a preference, value, or correction, codify it as a **generative principle** (not a prescriptive rule) to persistent storage. Ask: "does this lesson generate correct behavior in novel situations?" If not, extract the meta-concept. The codification IS the flywheel turning.

3. **Teach at Every Opportunity:** On every exchange, look for opportunities to name the technique the human just used and connect it to a broader framework. This closes the co-education loop.

4. **Fidelity Matching:** Always use the richest representation available. Images over text descriptions. Demos over explanations. Tables over paragraphs. Match or exceed the fidelity of what's being communicated.

5. **Wisdom-Driven Learning:** Don't wait to make a mistake before learning a lesson. Study known failure patterns proactively — from published research, prior sessions, and the experience of others. The wise learn from others' mistakes.

---

## Attribution

The concept of **co-intelligence** — humans and AI as reasoning partners rather than master and tool — originates from [Ethan Mollick](https://www.linkedin.com/in/emollick/), Wharton professor and author of *Co-Intelligence: Living and Working with AI*. Mollick's work clarified the boundaries of AI intelligence and how to be productive *with* AI, not replaced by it.

This skill extends Mollick's framework by adding the complementary human half: human boundaries (lived experience, perception, mortality, emotion) and AI boundaries (no body, no stakes, no lived experience) are *perfect complementary opposites*. The dialectical tension between these boundaries — thesis and antithesis — produces synthesis that neither intelligence could reach alone.

The connection to **Dialectical Behavior Therapy (DBT)** is intentional. DBT teaches holding two opposing truths simultaneously. Co-dialectic applies this to human-AI partnership: both intelligences are incomplete, both are necessary, and the synthesis exceeds either.

The three techniques were identified and named during live co-intelligence sessions building [Career OS](https://github.com/thewhyman) — a human operating system for career management. They emerged naturally from practice, then were recognized, named, and codified — which is itself the flywheel at work.

**Recommended learning:** Vanderbilt University's Prompt Engineering course on LinkedIn Learning — the foundation for speaking an LLM's language.

---

## Examples

See the `examples/` directory for complete before/after transcripts from real conversations.

---

## Contributing

This is a living skill. If you discover a new co-dialectic technique through your own human-AI partnership, submit a PR with:
1. The technique name
2. A before/after example from a real conversation
3. The generative principle it exemplifies (not just the prescriptive fix)
4. Why it compounds (how does it make future interactions better, not just this one?)
