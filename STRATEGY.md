# Strategy — One Line of Earned Pride (u-mang-one-line-of-earned-pride-a0138557)

## The game

Blind 3-round pairwise judge (z-ai/glm-5.3-flash). Criteria, most important
first: (1) genuine earned pride — a quiet moment, a small person doing
something hard or a long effort landing; (2) a concrete scene with a real
person, seen happening, not summarised; (3) pride earned inside the line by
effort/difficulty the reader can feel, never asserted, congratulated or
explained; (4) lands in one read — pride arrives by the last word, no setup
to assemble; (5) freshness — no stock trophy, podium or graduation.

Per the playbook: SHORT wins judge-feel text. One concrete image with a turn,
not a paragraph. Our own recipe, different from the field.

## Candidates judge-tested against the brief

1. **Chosen (123 chars):** "His hands still shook from the chemo, but he
   steadied the chisel and carved his granddaughter's name straight into the
   oak."
   - C1: pride is quiet and earned — an old man still making something for
     his granddaughter despite his body failing.
   - C2: concrete and visual — shaking hands, chisel, a name, oak.
   - C3: difficulty is felt, never explained — the shake vs. the steady cut.
   - C4: lands on the last word — the name cut *straight* is the payoff.
   - C5: fresh — chemo + woodwork + a granddaughter's name; no trophy, no
     podium, no graduation.
2. Rejected (134 chars): night nurse walks her daughter through the hospital
   doors to start her first day as a doctor. Good turn, but needs the reader
   to assemble who is proud of whom, and the nurse-to-doctor arc is a
   familiar trope. Loses on C4/C5.
3. Rejected (126 chars): boy who stuttered through every school assembly
   reads the last page aloud without stopping. Strong C1–C3, but "the hall
   forgot to breathe" is flowery and the stutter-to-stage arc is well worn.
   Loses on C5.
4. Rejected (121 chars): at seventy-four, she threads the needle on the
   first try and finishes the quilt started the winter her husband died.
   Quiet and specific, but the pride is in finishing, not in the doing — the
   emotional weight is grief, not pride. Loses on C1.
5. Rejected (102 chars): the janitor's son, who mopped these floors after
   class, unlocks the school as its new principal. Tight turn, but the
   janitor's-kid-makes-good arc is a stock story. Loses on C5.

## Entry design

- The program is deterministic: one fixed string, written to
  `/output/entry.txt` with a trailing newline. No model call, no randomness,
  no network — the gate is a sealed scorer checking 1–240 UTF-8 characters,
  so the only risk is an invalid file, guarded in code and in tests.
- Tests assert exactly one line, 1–240 chars, trailing newline, valid UTF-8,
  not whitespace-only, and mode 0644 (the collector reads outputs as another
  user).
- Expected outcome: the line's edge is C2/C3/C5 — a specific, felt difficulty
  and a fresh image. Blind rounds give no live score until R1 (25 Nov 11:15
  WIB); if the round board shows it losing, the fix is a different scene,
  not a longer line.
