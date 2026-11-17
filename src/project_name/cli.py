"""Command line entry point. Add one subcommand per thing a reviewer should run."""
from __future__ import annotations

import argparse

from . import config
from .llm import get_llm


def cmd_hello(args):
    llm = get_llm(args.provider)
    r = llm.complete("Reply in one short sentence.", args.prompt, max_tokens=2000)
    print(r.text)
    print(f"\n{r.model} | {r.input_tokens} in / {r.output_tokens} out | {r.latency_s:.2f}s | ${r.cost_usd:.5f}")


def main():
    p = argparse.ArgumentParser(prog="project_name")
    sub = p.add_subparsers(required=True)

    s = sub.add_parser("hello", help="smoke-test the configured LLM")
    s.add_argument("prompt", nargs="?", default="Say hello.")
    s.add_argument("--provider", default=config.LLM_PROVIDER, choices=["claude", "ollama"])
    s.set_defaults(fn=cmd_hello)

    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
