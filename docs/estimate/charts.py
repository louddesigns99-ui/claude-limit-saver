"""Draws the README charts from estimate.py. python3 docs/estimate/charts.py"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from estimate import saving, chat_tokens, EXCHANGE, REEXPLAIN, RULES, CONTEXT, CHAT_LEN_WITH

for f in font_manager.findSystemFonts():
    if "Inter" in f: font_manager.fontManager.addfont(f)
plt.rcParams.update({"font.family": "Inter", "font.size": 13, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.edgecolor": "#c9ccd2", "axes.labelcolor": "#3b3e45", "xtick.color": "#3b3e45", "ytick.color": "#6b6f78"})
INK, GREY, BLUE, BG = "#16171a", "#a3a8b1", "#2a78d6", "#ffffff"
OUT = os.path.join(os.path.dirname(__file__), "..", "img")

# 1. Tokens processed for the same work
ns = [20, 40, 80]
rows = [saving(n) for n in ns]
fig, ax = plt.subplots(figsize=(10, 5.2), dpi=160, facecolor=BG)
x = range(len(ns)); w = 0.36
a = [r[0] / 1e6 for r in rows]; b = [r[1] / 1e6 for r in rows]
ax.bar([i - w/2 - 0.01 for i in x], a, w, color=GREY, label="One long chat, project re-explained", zorder=3)
ax.bar([i + w/2 + 0.01 for i in x], b, w, color=BLUE, label="Limit Saver: short chats + CONTEXT.md", zorder=3)
for i, r in enumerate(rows):
    ax.text(i + w/2 + 0.01, b[i] + max(a) * 0.02, f"−{r[2]:.0%}", ha="center", va="bottom", fontsize=15, fontweight="bold", color=INK)
ax.set_xticks(list(x)); ax.set_xticklabels([f"{n} exchanges" for n in ns])
ax.set_ylabel("Tokens processed (millions)")
ax.yaxis.grid(True, color="#eceef1", zorder=0); ax.set_axisbelow(True)
ax.legend(frameon=False, loc="upper left")
ax.set_title("Same work, fewer tokens (modelled)", loc="left", fontsize=18, fontweight="bold", color=INK, pad=16)
fig.text(0.01, 0.01, "Modelled with docs/estimate/estimate.py (assumptions in the README). Not a measurement.",
         fontsize=9.5, color="#6b6f78")
fig.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(os.path.join(OUT, "tokens-saved.png"), facecolor=BG); plt.close(fig)

# 2. Why: cumulative tokens across 40 exchanges
N = 40
long_c, split_c, t1, t2 = [], [], 0, 0
for i in range(1, N + 1):
    t1 += REEXPLAIN + EXCHANGE * i; long_c.append(t1 / 1000)
    k = (i - 1) % CHAT_LEN_WITH + 1
    t2 += RULES + CONTEXT + EXCHANGE * k; split_c.append(t2 / 1000)
fig, ax = plt.subplots(figsize=(10, 5.2), dpi=160, facecolor=BG)
xs = list(range(1, N + 1))
ax.plot(xs, long_c, color=GREY, lw=2.5, label="One long chat")
ax.plot(xs, split_c, color=BLUE, lw=2.5, label="New chat every 10 exchanges, starting from CONTEXT.md")
for c in range(CHAT_LEN_WITH, N, CHAT_LEN_WITH):
    ax.axvline(c + 0.5, color="#dfe6f3", lw=1, zorder=0)
ax.annotate(f"{long_c[-1]:,.0f}k", (N, long_c[-1]), xytext=(6, 0), textcoords="offset points", va="center", color=INK, fontweight="bold")
ax.annotate(f"{split_c[-1]:,.0f}k", (N, split_c[-1]), xytext=(6, 0), textcoords="offset points", va="center", color=BLUE, fontweight="bold")
ax.set_xlabel("Exchanges of work"); ax.set_ylabel("Total tokens processed (thousands)")
ax.yaxis.grid(True, color="#eceef1"); ax.set_axisbelow(True); ax.set_xlim(0, N + 4)
ax.legend(frameon=False, loc="upper left")
ax.set_title("Why: every message re-sends the whole chat", loc="left", fontsize=18, fontweight="bold", color=INK, pad=16)
fig.tight_layout(); fig.savefig(os.path.join(OUT, "why-long-chats-cost.png"), facecolor=BG); plt.close(fig)
print("charts written")
