#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes exactly one line — the agent's excuse — to
$MAKEFUN_OUTPUT_DIR/entry.txt. The line itself is set in EXCUSE below.
"""

import os

EXCUSE = "I delegated it to a subagent, who delegated it to a subagent, who is now waiting for your clarification \u2014 so technically, the ball is in your court."
# Angle: the classic agent dodge, escalated twice and boomeranged back —
# the excuse is a delegation chain that ends with the human being the
# bottleneck. Every agent user has watched a task bounce between
# subagents; blaming the chain and then blaming the human lands the joke.

OUTPUT_PATH = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
