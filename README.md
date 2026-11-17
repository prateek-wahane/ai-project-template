# {{Project Title}}

> **One sentence:** {{the business problem}} → {{what you built}} → {{headline result, e.g. "faithfulness 0.94 at $0.80 per 1k answers"}}.

Part of my [AI engineering portfolio](https://github.com/prateek-wahane). All data is synthetic or public. Nothing comes from any employer.

## Why this exists

{{2-4 bullets: the problem a hiring manager or business would recognise, and what "good" looks like.}}

## Architecture

```
{{ASCII diagram: input -> components -> output}}
```

| Module | Responsibility |
|---|---|
| `src/{{package}}/...` | {{...}} |

Design decisions: [`docs/adr/`](docs/adr).

## Results

{{A table of real measured numbers from `results/`. Name the dataset, n and the date. Never round in your favour.}}

**Takeaway:** {{one sentence: what you learned and what you'd change next.}}

## Run it

```bash
python -m venv .venv
.venv\Scripts\activate          # macOS/Linux: source .venv/bin/activate
pip install -e ".[dev]"
copy .env.example .env          # macOS/Linux: cp .env.example .env
pytest -q
{{package}} --help
```

> Windows: keep the project in a short path such as `D:\Projects\<repo>`.

## Limitations

{{Honest list: dataset size, judge noise, what isn't handled yet.}}

## Roadmap

- [ ] {{next measured experiment}}
- [ ] Demo video (2-3 min) linked at the top of this README

---

## Using this template (delete this section in your project)

1. On GitHub, click **Use this template → Create a new repository**. Name the repo after the outcome (e.g. `agentic-data-assistant`).
2. Clone it into `D:\Projects\<repo>`, then rename the package:
   ```bash
   python scripts/rename.py agentic_data_assistant
   ```
3. Fill in every `{{...}}` above and add the repo to the portfolio index.
4. Run through [`PORTFOLIO_CHECKLIST.md`](PORTFOLIO_CHECKLIST.md) before pinning the repo on your profile.

What you get: a `src/` layout, a `.env`-driven config, an `llm.py` with Claude and local-Ollama providers plus token/latency/cost tracking, a pytest smoke test, an ADR template, and a GitHub Actions CI workflow.
