# Portfolio checklist

Run through this before pinning a repo on your GitHub profile or linking it on your resume.

## Honesty
- [ ] Every number in the README comes from a file in `results/` that anyone can regenerate.
- [ ] The resume bullet for this project only claims what the repo actually shows.
- [ ] Limitations are written down, not hidden.
- [ ] Only synthetic or public data. Nothing from any employer.

## A reviewer can run it in 5 minutes
- [ ] A fresh clone passes `pip install -e ".[dev]"` and `pytest -q`.
- [ ] One command shows the main result (e.g. `<package> eval`).
- [ ] There's a free path (local model or a free tier) as well as the paid one.
- [ ] `.env.example` lists every setting, and `.env` is in `.gitignore`.

## The architect's view
- [ ] At least 3 ADRs: key choices, the alternatives and why you picked this one.
- [ ] An architecture diagram in the README.
- [ ] A "path to production" ADR covering cloud mapping, security, observability, cost and the CI quality gate.
- [ ] Cost per 1k requests and p50/p90 latency are measured.

## Presentation
- [ ] The first line of the README states problem → solution → headline result.
- [ ] A 2-3 minute demo video (Loom/YouTube) is linked at the top.
- [ ] CI badge is green.
- [ ] GitHub topics are set: `llm`, `generative-ai`, plus the project's own (`rag`, `langgraph`, `agents`, `fine-tuning`, ...).
- [ ] Added to the portfolio index on your profile README.
- [ ] One LinkedIn post: problem, what you measured, one surprising finding, link.
