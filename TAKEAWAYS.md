# Takeaways

Running notes of ideas worth applying — especially to Slate.

---

## 1. The Semi-Async Valley of Death (Ara / @arafatkatze)

Source: https://x.com/arafatkatze/status/1986131437331140665/photo/1

Sync vs async is the wrong lens for coding agents. Plot **observed productivity (Y)**
against **agent autonomy / latency (X)** and you get a U-shaped curve:

- **Left — interactive flow (~5 sec → 2-4 min):** fast, cheap models keep you in the
  deep-work / flow state. High felt productivity. (e.g. GLM 4.6 on Cerebras ~2000 tok/s,
  Gemini Flash → Sonnet 4.5, Minimax M2 → GPT-5 Codex, climbing in intelligence but also
  latency.) Even for *hard* problems you still want fast models to stay in the flow window.
- **Middle — the valley of death (~6+ min):** "Not enough to delegate, not fun to wait."
  Too slow to feel interactive, too quick/uncertain to walk away from. Almost nothing in
  this region produces genuinely useful results — it's dead time.
- **Right — parallel / background / commodified (~10+ min, hours):** for *super-hard*
  problems it's fine for the agent to grind in the background. You fully delegate and
  trade time for intelligence. Frontier labs are flexing multi-day problem solving here.

Key insight: match the model/latency to the problem so you live on either *side* of the
valley — interactive flow or true fire-and-forget background — and avoid the dead middle.

**Why it matters for Slate:** Design agent UX so tasks land on one side of the valley.
Either keep responses fast enough to hold the user in flow (interactive work), or make
them genuinely async/backgroundable (fire-and-forget, notify-on-done) — never strand the
user in the 6-min "watch a spinner" middle. Latency budget should be a deliberate product
decision per task type, not an afterthought.

---

## 2. Evals should be on the task, not the call (from Notion)

Evaluate the **whole task end-to-end**, not individual model calls in isolation. The unit
of evaluation should be a complete outcome — a full app, a full set of document
extractions, etc. — rather than the quality of any single LLM call along the way.

**Why it matters for Slate:** A single call can look "correct" while the overall task
still fails (or vice versa). Measuring at the task level is what actually reflects user
value and catches failures that only emerge across a multi-step pipeline.

---

## 3. Charge for outcome, not seat (Geoff Huntley + Notion)

Both Geoff Huntley and Notion landed on the same pricing thesis: in an agentic world,
per-seat pricing breaks down. When agents do the work, value isn't tied to how many
humans have logins — it's tied to outcomes/tasks completed. Price for the outcome
delivered rather than the number of seats.

**Why it matters for Slate:** Slate is already planning this — outcome-based pricing.
Good external validation that the direction matches where the market is heading. The
[[#2]] task-level eval mindset is the natural pair: if you bill per outcome, you need to
measure success at the outcome/task level too.

---

## 4. A dumber, fast model can beat a smarter, slow one

Iteration-loop speed often matters more than raw model intelligence. A weaker model that
responds fast lets you run many more correction/refinement cycles per unit time, and the
tight feedback loop converges on a good result faster than a smarter model that's slow
enough to stall the loop. Throughput of attempts > quality of a single attempt.

**Why it matters for Slate:** Pairs directly with [[#1]] — staying in the fast,
interactive side of the valley isn't just nicer UX, it's often *more capable* in
practice because of loop speed. When choosing models per task, weigh latency-enabled
iteration, not just benchmark scores.

---

## 5. Fail Fast, Fix Faster — the validation harness is the moat (aj fisher)

Source: https://ajfisher.me/aieng26 ("Fail Fast, Fix Faster", AI Engineer 2026)

Once a model clears a baseline of competence, raw intelligence becomes secondary. What
compounds advantage is **iteration speed × validation quality**: a fast model with a tight
validation harness runs many correction loops cheaply and converges faster than a smarter,
slower model.

- **Evidence:** Mercury 2 (diffusion-based) hit perfect scores in ~6s median, vs GPT-5.4
  at 88s and Qwen3 Coder 480B at 611s — winning on loop speed, not reasoning.
- **The Ralph Loop:** persistent agent loops with targeted feedback are the core
  operational model; repeated tight cycles beat brute-force intelligence.
- Measure **loop efficiency** (turn counts, time-to-completion), not just accuracy.
- Invest in **validation harnesses** and metric-driven workflows (DSPy, Inspect) over
  endless prompt tweaking.

**Why it matters for Slate:** This is the rigorous version of [[#4]]. The defensible asset
isn't the model — it's the validation harness wrapped around it. Combined with [[#2]]
(task-level evals), the play is: build tight, automated, task-level validation so cheaper
fast models can loop to a correct outcome. Speed + validation first, intelligence second.
