# Hand a step to another AI

Suggest it when another tool the person has does the step clearly better, or runs on a separate
subscription's allowance. Don't hand off what you can do well; every handoff costs the person time.

**Good fits:** long autonomous web research (another assistant's agent mode), a second opinion on
something important (offer, pricing, copy, design), images/video/voice, a tool already connected to
the app the person needs.

## Steps
1. One line: why the other tool is better for this step.
2. A ready-to-paste prompt (`templates/handoff-prompt.md`): role, exact task with numbers, rules,
   and a **strict output format** so the result can be checked.
3. Recurring? Save the prompt as that tool's project instructions, so the person only types a
   short trigger each time.
4. When the result comes back: check every item against the rules, keep what passes, set aside the
   rest with a reason, and update CONTEXT.md.

Examples: `examples/handoff-examples.md`.
