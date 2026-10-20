# Claude Limit Saver

**Stop burning your Claude limits.** One paste-in rules file and one skill that keep project memory
in a file, keep chats short, flag when you're on the wrong model, and turn a messy chat into a proper
project. Made for people running real work on a basic plan, not just developers.

Works with **Claude Projects (claude.ai)** and **Claude Code**. No coding needed for the claude.ai setup.

---

## What changes

| Without | With Limit Saver |
|---|---|
| You re-explain your project at the start of every chat | Claude reads one short `CONTEXT.md` and picks up where you left off |
| One giant chat that gets slower and more expensive every message | Unrelated requests get a 5-line brief to paste into a fresh chat |
| The heaviest model formats a list | Claude tells you in one line when the task needs a lighter (or heavier) model |
| A scheduled task quietly runs every day on the default model | Every scheduled task gets an explicit model, a written procedure and a short report |
| The same parked idea or warning comes back every chat | `PARKED`, `DELIBERATE` and `FINISHED` markers stop it |
| Claude does exactly what you typed, even when there's a better way | It says so in one line and gives you the better prompt first |
| You open a new chat every morning to ask "what's next?" | A morning task scans the project and updates one checklist; you just tick items |
| Claude struggles with a long web-research job | It hands you a ready-to-paste prompt for your other AI tool, then checks the result |

See a filled-in example: [`CONTEXT-example.md`](skills/limit-saver/examples/CONTEXT-example.md)
(a fictional one-person dog-walking business).

## Two parts

1. **Always-on rules** ([`PROJECT-INSTRUCTIONS.md`](skills/limit-saver/rules/PROJECT-INSTRUCTIONS.md),
   ~400 words). Paste into your project instructions. This is what changes Claude's behaviour in every message.
2. **The `limit-saver` skill.** Loads only when needed, for jobs with steps:
   - turn a chat into a project
   - copy working rules from one project to another
   - set up a scheduled task that doesn't drain your limit
   - a **daily task list**: a morning task scans the project and updates one checklist you tick through
   - hand a step to another AI (e.g. ChatGPT) with a strict output format, and check what comes back
   - a 5-minute audit when you keep hitting your limit

## Set up in 5 minutes

### Claude Projects (claude.ai), no code
1. Open [`PROJECT-INSTRUCTIONS.md`](skills/limit-saver/rules/PROJECT-INSTRUCTIONS.md), copy everything
   below the line, fill in the `<...>` parts, and paste it into your project's instructions.
2. Copy [`templates/CONTEXT.md`](skills/limit-saver/templates/CONTEXT.md), fill in what you know
   (or ask Claude: "fill this in from our chat"), and add it to the project's knowledge.
3. Optional, for the procedures: download `limit-saver.zip` from the
   [latest release](../../releases/latest) and upload it as a skill in Claude's settings, where your
   plan supports skills.
4. Test it: start a new chat in the project and type *"What's the next step?"* Claude should answer
   from CONTEXT.md without asking you to explain the project.

### Claude Code
```bash
git clone https://github.com/louddesigns99-ui/claude-limit-saver
cp -r claude-limit-saver/skills/limit-saver ~/.claude/skills/        # the skill, for all your projects
```
Then in your project: save the rules (below the line in `PROJECT-INSTRUCTIONS.md`) as `CLAUDE.md`, and
add a `CONTEXT.md` from the template.

### Try it on an existing chat
In a long chat, type: **"Turn this chat into a project."** Claude inventories the chat, writes
CONTEXT.md and tells you exactly what to click.

## Does it really save usage?
Honestly: it depends on how you work today. The biggest wins come from shorter chats and not
re-explaining your project. Check it yourself in one week: [`docs/measure-it.md`](docs/measure-it.md).
If it helps, open an issue with your before/after. Real numbers from users beat any claim here.

## What it won't do
- Switch models or open chats for you (Claude can't). It tells you when and what.
- Send, post or pay on your behalf. It drafts; you approve.
- Promise exact savings.

## Contributing
Ideas, fixes and before/after reports are welcome: see [CONTRIBUTING.md](CONTRIBUTING.md).

## Support
If this saves you time, you can support it here: ❤️ **Sponsor** button at the top of this page.

## License
MIT
