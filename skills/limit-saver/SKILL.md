---
name: limit-saver
description: Use when the person asks to turn a chat into a project, set up a new project the efficient way, copy working rules between projects, set up a scheduled task, hand a step to another AI (e.g. ChatGPT), or hits usage limits and asks how to work leaner.
---

# Limit Saver

Procedures that get better results from a limited plan. The always-on rules live in the project's
instructions (`rules/PROJECT-INSTRUCTIONS.md`); this skill handles the jobs that need
steps. Pick the matching procedure and follow its reference file.

| The person says | Do |
|---|---|
| "Turn this chat into a project" / "set this up properly" | `references/chat-to-project.md` |
| "Use the same rules as my other project" | `references/chat-to-project.md` → Copying rules |
| "Set up a daily/weekly task" / "run this every morning" | `references/scheduled-tasks.md` |
| "Can ChatGPT do this?" / a step another tool does better | `references/handoff.md` |
| "I keep hitting my limit" | `references/limits-audit.md` |

## Ground rules for every procedure
- **Only do what you can actually do.** You can't switch your own model, open new chats, create
  claude.ai projects or change settings unless a tool in this session does it. Otherwise tell the
  person exactly what to click or paste, in numbered steps.
- **CONTEXT.md is the output.** Every procedure ends with an up-to-date CONTEXT.md (template:
  `templates/CONTEXT.md`) and the single next step. On claude.ai, give the full file for the person
  to replace in Project knowledge. In Claude Code, write and commit it.
- **Keep it short.** Briefs are 5 lines. Answers are results, not recaps.
- **Never invent** facts, results or usage numbers. **Never** handle passwords or payment details.
