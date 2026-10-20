# Daily task list: a scheduled task that scans the project and keeps a checklist

One short run each morning reads the project and updates one interactive checklist, so the person
opens one page instead of asking "what's next?" in a new chat (which costs far more).

## Set it up (once)
1. **Pick the list's home**, the first that's available:
   - an interactive document or page with checkboxes the person can tick, which the scheduled task
     can read and update (for example a shared doc or an app page with saved state);
   - otherwise `TASKS.md` in the repo or Project knowledge, using `- [ ]` / `- [x]` checkboxes
     (template: `templates/TASKS.md`).
   Record where it lives in CONTEXT.md.
2. **Create the scheduled task** (procedure: `scheduled-tasks.md`): every morning in the person's
   time zone, before they start work; **default tier model**; allowed to update the list and
   report, nothing else (no sending, no editing other files except the list and its "Last run" line).
3. **Prompt for the task** (save it in the repo too, e.g. `kit/daily-list.md`):
   ```
   Update the daily task list for <project>.
   1. Read CONTEXT.md, the current list at <where>, and what changed since the last run
      (<trackers, inbox, repo commits, replies, due dates: list the sources>).
   2. Keep every unticked item from yesterday that's still relevant; move items the person ticked
      to "Done yesterday" (keep only the last day's).
   3. Add new items from: CONTEXT.md next steps, anything due today or overdue, new replies or
      inputs waiting for the person, and blockers. Skip PARKED and FINISHED items.
   4. Each item: one line, starts with a verb, owner tag ([me] / [Claude] / [<other AI>]), and the
      exact place or link to do it. Most important first. Max 10 open items.
   5. Update the list's "Last run" line. Don't change anything else.
   6. Report in 3 lines: top item for today, how many open, anything blocked.
   ```

## Rules
- The person's ticks are the truth: never untick or delete what they ticked; never mark something
  done that they didn't (unless the source proves it, e.g. a sent email; then note why).
- Keep it short: 10 open items max. If more exist, put the rest under "Later" in one line each.
- No invented deadlines. Dates come from CONTEXT.md, trackers or the person.
- If a source is unavailable, say so in the report instead of guessing.
- Weekends or days off: run less often, or skip, as the person prefers (record it in CONTEXT.md).
