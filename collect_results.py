"""Combine every test run in raw_outputs/ into ONE summary, and print the numbers for the solution doc.

    python collect_results.py

Takes the latest result for each case (so re-running a few failed cases with --ids just replaces those).
Writes raw_outputs/ALL_SUMMARY.md and prints the values for the yellow boxes in docs/solution_doc.html.
"""
import json
from pathlib import Path

from run_tests import write_summary

ROOT = Path(__file__).resolve().parent / "raw_outputs"


def main():
    runs = sorted(p for p in ROOT.glob("*/summary.json") if p.parent.name != "ALL")
    if not runs:
        print("No runs found in raw_outputs/. Run: python run_tests.py --ids 01 02 03")
        return
    latest, models = {}, set()
    for p in runs:                                   # folders are named by timestamp, so later runs win
        data = json.loads(p.read_text(encoding="utf-8"))
        models.add(data["model"])
        for r in data["rows"]:
            latest[r["id"]] = r
    rows = [latest[k] for k in sorted(latest)]
    out = ROOT / "ALL"
    out.mkdir(exist_ok=True)
    write_summary(out, " + ".join(sorted(models)), rows)
    (ROOT / "ALL_SUMMARY.md").write_text((out / "SUMMARY.md").read_text(encoding="utf-8"), encoding="utf-8")

    def count(key, rs=rows):
        vals = [r[key] for r in rs if key in r]
        return f"{sum(vals)} / {len(vals)}" if vals else "n/a"

    both = [r for r in rows if "no_case_law_shown" in r]
    clean = sum(r["no_case_law_shown"] and r.get("no_unflagged_repealed_law", True) for r in both)
    all_ids = [c["id"] for c in json.loads((ROOT.parent / "tests" / "cases.json").read_text(encoding="utf-8"))]
    v, a = sum(r.get("_verified", 0) for r in rows), sum(r.get("_ai_recalled", 0) for r in rows)
    print(f"\nCases found: {len(rows)} / {len(all_ids)}   (runs combined: {len(runs)})")
    missing = [i[:2] for i in all_ids if i not in latest]
    if missing:
        print(f"  Not run yet: {' '.join(missing)}   ->   python run_tests.py --ids {' '.join(missing)}")
    print("\n--- Paste into the yellow boxes of docs/solution_doc.html ---")
    print(f"Ended in the right place ............ {count('stage_ok')}")
    print(f"Asked questions before an opinion ... {count('asked_before_advising')}")
    print(f"Replied in the user's language ...... {count('language_ok')}")
    print(f"No court cases / outdated laws ...... {clean} / {len(both)}")
    print(f"Citations from the checked list ..... {100 * v // max(v + a, 1)}%  ({v} checked, {a} AI-recalled)")
    print("\n--- Candidates for 'Where it fails' (open each <case>.md to see what went wrong) ---")
    bad = [(r["id"], [k for k, x in r.items() if x is False]) for r in rows]
    bad = [(i, ks) for i, ks in bad if ks or latest[i].get("stage") == "ERROR"]
    for i, ks in bad or [("none", ["every automatic check passed - read 3-4 answers yourself and note anything weak"])]:
        print(f"  {i}: {', '.join(ks) or 'ERROR during run'}")
    print(f"\nFull table: {ROOT / 'ALL_SUMMARY.md'}")


if __name__ == "__main__":
    main()
