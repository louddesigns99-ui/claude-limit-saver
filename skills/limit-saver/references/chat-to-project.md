# Turn a chat into a project

Goal: future chats start from one short file instead of a long chat history.

## 1. Inventory (don't change anything yet)
From the chat, list in short lines:
- Goal and who it's for.
- Decisions, each with its date and a one-line reason.
- What exists: files, links, accounts (no passwords), live pages, data, scheduled tasks, other AI tools in use.
- Status: done / waiting / blocked (on whom).
- The person's stated rules and preferences.
- Next steps.
Drop the back-and-forth. Keep only what a fresh chat needs.

## 2. Decide the home
- A separate line of work → its own project and CONTEXT.md.
- Same line of work as an existing project → a section in that project's CONTEXT.md.
- Never restructure something already running to fit the new work.

## 3. Build CONTEXT.md
Fill `templates/CONTEXT.md` from the inventory. Mark PARKED, DELIBERATE and FINISHED items so they
stop being raised. Long material (research, reports) becomes separate files, linked from CONTEXT.md.

## 4. Set up the project (the person clicks; you give exact steps)
**claude.ai:**
1. Create a project named after the work.
2. Paste the filled `rules/PROJECT-INSTRUCTIONS.md` into the project instructions.
3. Upload CONTEXT.md (and any linked files) to Project knowledge.
4. First message in the new project: the next step from CONTEXT.md.

**Claude Code:**
1. Put CONTEXT.md and a CLAUDE.md (from `rules/PROJECT-INSTRUCTIONS.md`) at the repo root; commit.
2. If the person uses Claude Code projects, attach the repo and paste the same instructions.

## 5. Hand over
Three lines max: where it lives, what the person must click, the exact first message to send.

## Copying rules from another project
1. Ask the person to paste the other project's instructions (or read its CLAUDE.md if you can).
2. Merge, don't overwrite: keep this project's own rules, add the shared ones, drop duplicates.
3. Give the merged instructions to paste (or write them), and list in one line what was copied.
4. Settings you can't see or change (default model, effort): tell the person which to match.
