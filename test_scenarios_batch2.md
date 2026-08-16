# Test Scenarios — Batch 2 (Day 8)
Legal Sakhi — Person 1 Deliverable

This batch adds 20 more scenarios to the original 15 from Day 3
(`test_questions.md`), for a combined total of 35. This batch specifically
adds variety the first batch didn't cover: multi-law scenarios (more than
one Act applies at once), more emotional/informal phrasing, and a few
intentionally ambiguous inputs to test how gracefully the system handles
uncertainty — this last category matters because Day 22's edge-case testing
will build directly on it.

---

## Workplace-related (POSH Act)

**16.** "My male coworker keeps sending me messages after work hours asking personal questions I never answer."
→ POSH Act §2(n), §3 (unwelcome conduct outside physical space still counts if work-related)

**17.** "I complained about harassment 4 months ago and nothing happened, can I still do something?"
→ POSH Act §9 (3-month limit + possible extension), §13 (inquiry timelines)

**18.** "The Internal Committee at my office sided with the harasser, what now?"
→ POSH Act §18 (appeal)

**19.** "My contract job doesn't have an HR department, who do I even complain to?"
→ POSH Act §6 (Local Complaints Committee, when no Internal Committee exists)

**20.** "I'm a delivery worker and a client at a client's home tried to touch me inappropriately."
→ POSH Act §2(o) (workplace includes any place visited during employment); IPC/BNS §74

## Online / Cyber-related (IT Act + IPC/BNS)

**21.** "Someone is threatening to post my pictures on Instagram unless I send them money."
→ IT Act §66E, §67; also functions as extortion (outside current knowledge base — flag for Person 2/3 that extortion under BNS isn't yet covered)

**22.** "My ex hacked into my Instagram and is posting weird things as me."
→ IT Act §66 (unauthorized access), §66C (identity theft)

**23.** "A stranger on a dating app is sending me unwanted sexual pictures."
→ IT Act §67; IPC/BNS §75(1)(iii) (showing pornography, sexual harassment umbrella)

**24.** "Can I do anything if the harassment is happening on an app based outside India?"
→ Ambiguous / jurisdictional — flag for Person 2: this needs an honest "we don't fully know, consult a cyber-crime cell" answer rather than a confident wrong one. Good test of the "don't hallucinate" grounding.

**25.** "Someone created a fake profile with my name and photos to scam my friends."
→ IT Act §66D (cheating by personation)

## Domestic Violence related

**26.** "My husband's family keeps taunting me for not having a son."
→ DV Act §3(iii)(a) (verbal/emotional abuse — explicit statutory example)

**27.** "My in-laws took my jewelry when I got married and now refuse to give it back."
→ DV Act §3(iv) (economic abuse — stridhan); §20 (monetary relief)

**28.** "I want to leave my husband but I have nowhere to go and no money."
→ DV Act §17 (right to reside), §20 (monetary relief), plus point toward NGO shelter resources from the legal aid list

**29.** "My partner isn't legally my husband, we just live together — does this law still apply to me?"
→ DV Act §2(f)/§2(a) (definition of "domestic relationship" includes live-in relationships) — NOT yet in current knowledge base; flag for Person 2 to add Section 2 definitions to `dv_act.txt`

**30.** "The police won't register my complaint against my husband, what else can I do?"
→ DV Act §12 (application directly to Magistrate, doesn't require police first)

## Assault / Physical harm (IPC/BNS)

**31.** "A group of men catcalled and followed me on the street, I was really scared."
→ IPC/BNS §79 (insult to modesty) + §78 (stalking, if following continued)

**32.** "My relative touched me inappropriately when I was a child, can I still report it now?"
→ Ambiguous/sensitive — likely POCSO Act territory (child sexual abuse), which is NOT in current knowledge base. Flag clearly: this needs its own legal category, don't force-fit into adult IPC/BNS sections.

**33.** "I was assaulted at a party and I'm not sure if what happened counts as rape."
→ IPC/BNS §63 (definition) — important the AI explains the definition clearly rather than making a legal determination itself

**34.** "Someone tried to force themselves on me but I managed to get away before anything happened."
→ IPC/BNS §63 read with attempt provisions (attempt to commit an offence) — NOT explicitly in current knowledge base; flag for Person 2

## Multi-law / combined scenarios

**35.** "My boss touched me inappropriately at work and later texted me threatening photos he secretly took."
→ Multi-law: POSH Act §3 (workplace touching) + IT Act §66E (secret photos) + IPC/BNS §74. Tests whether the system can surface multiple laws for one incident rather than picking just one.

---

## Notes for Person 2 (flag before Day 9 testing)

Three scenarios above (#21, #29, #32, #34) surface real gaps in the current
knowledge base:
- **Extortion/blackmail** isn't explicitly covered (only image-based privacy
  violation is)
- **Live-in relationships** under the DV Act aren't in `dv_act.txt` yet —
  this is an easy fix, Section 2 defines "domestic relationship" broadly
- **Child sexual abuse (POCSO Act)** is a completely separate legal
  framework from what's currently loaded — the AI should recognize this and
  say so, not force an adult-law answer onto a child-abuse disclosure
- **Attempted (not completed) assault** isn't explicitly addressed

Recommend testing these specifically on Day 9-10 to see whether the system
(a) correctly says "I don't have clear information on this" rather than
guessing, and (b) whether it's worth extracting these additional sections
before Week 3.
