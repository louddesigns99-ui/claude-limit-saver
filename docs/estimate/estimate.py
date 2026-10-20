"""Modelled token estimate for Claude Limit Saver.

This is arithmetic on stated assumptions, not a measurement. Change the numbers below to match
how you work and re-run:  python3 docs/estimate/estimate.py

Model: every message in a chat re-sends the chat so far, so the tokens processed for exchange i
are roughly  start_tokens + exchange_tokens * i.  A long chat therefore grows quadratically;
splitting the same work into short chats that start from a small CONTEXT.md keeps it linear.
"""

EXCHANGE = 800        # tokens per exchange (your message + Claude's reply), average
REEXPLAIN = 2500      # tokens to re-explain the project at the start of a chat (without the skill)
RULES = 550           # always-on rules, loaded in every chat (with the skill)
CONTEXT = 700         # CONTEXT.md, loaded in every chat (with the skill)
CHAT_LEN_WITH = 10    # exchanges per chat when you keep one task per chat
DAILY_RUN = 3400      # one morning daily-list run (reads ~3,000, writes ~400)


def chat_tokens(turns, start):
    return sum(start + EXCHANGE * i for i in range(1, turns + 1))


def without(turns):
    return chat_tokens(turns, REEXPLAIN)


def with_skill(turns, include_daily=True):
    full, rest = divmod(turns, CHAT_LEN_WITH)
    t = full * chat_tokens(CHAT_LEN_WITH, RULES + CONTEXT) + (chat_tokens(rest, RULES + CONTEXT) if rest else 0)
    return t + (DAILY_RUN if include_daily else 0)


def saving(turns):
    a, b = without(turns), with_skill(turns)
    return a, b, 1 - b / a


if __name__ == "__main__":
    print(f"{'exchanges of work':>18} {'one long chat':>15} {'with skill':>12} {'saving':>8}")
    for n in (20, 40, 80, 200):
        a, b, s = saving(n)
        print(f"{n:>18} {a:>15,} {b:>12,} {s:>8.0%}")
