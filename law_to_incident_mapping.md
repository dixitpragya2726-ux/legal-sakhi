# Incident Type → Applicable Law Mapping
Legal Sakhi — Reference Doc (Person 1)

Purpose: A quick-reference map from *how a survivor might describe what
happened* to *which law(s) actually apply*. Useful for Person 2 when tuning
retrieval, and for anyone writing the "AI identifies the relevant law"
prompt — this is the ground truth the AI's categorization should match.

| Incident Type | Primary Law | Key Section(s) | Secondary Law (if applicable) |
|---|---|---|---|
| Unwelcome comments/remarks at work | POSH Act 2013 | §3, §2(n) | IPC/BNS §79 (if outside a formal workplace) |
| Unwanted physical contact at work | POSH Act 2013 | §3 | IPC/BNS §74 |
| Quid pro quo (job favors for sexual favors) | POSH Act 2013 | §3(2)(i)–(iii) | — |
| Hostile work environment | POSH Act 2013 | §3(2)(iv)–(v) | — |
| Filing a workplace complaint | POSH Act 2013 | §9, §4 | — |
| Workplace complaint conciliation/inquiry | POSH Act 2013 | §10, §11 | — |
| Being followed / unwanted repeated contact (in person) | IPC/BNS | §78 (stalking) | — |
| Being monitored online (social media, email) | IPC/BNS | §78(1)(ii) | IT Act §66 (if account access involved) |
| Non-consensual intimate photos/videos taken or shared | IT Act 2000 | §66E (privacy), §67 (obscene material) | IPC/BNS §74/§79 |
| Threat to leak/share private images ("revenge porn") | IT Act 2000 | §66E, §67 | — |
| Morphed / deepfake images | IT Act 2000 | §67 | IT Act §66C/§66D (if used to impersonate) |
| Fake social media account / impersonation | IT Act 2000 | §66C (identity theft), §66D (cheating by personation) | — |
| Hacking / unauthorized account access | IT Act 2000 | §66 | §66C (if credentials misused) |
| Physical abuse by spouse/partner/family (in shared household) | DV Act 2005 | §3, §12 | IPC/BNS §74/§79 (if assault also applies) |
| Emotional/verbal abuse by spouse/partner/family | DV Act 2005 | §3 (verbal & emotional abuse) | — |
| Economic abuse / financial control by spouse | DV Act 2005 | §3 (economic abuse), §20 (monetary relief) | — |
| Being denied access to the shared home | DV Act 2005 | §17 (right to reside) | — |
| Needing a legal order to stop contact/violence | DV Act 2005 | §18 (protection order) | — |
| Needing financial support after abuse | DV Act 2005 | §20 (monetary relief) | — |
| Sexual assault / rape | IPC/BNS | §63 (definition), §64 (punishment) | — |
| Rape by spouse while living separately | IPC/BNS | §67 (BNS) | DV Act §3 (sexual abuse) |
| Being disrobed / forced nakedness | IPC/BNS | §76 | — |
| Being secretly photographed/watched in private (voyeurism) | IPC/BNS | §77 | IT Act §66E (if image captured electronically) |
| Lewd gestures/comments in public (non-workplace) | IPC/BNS | §79 | — |
| General assault with intent to outrage modesty | IPC/BNS | §74 | — |

## How to use this table

1. **If the incident happened at a workplace** → check POSH Act first; only
   fall back to IPC/BNS if POSH doesn't cover the specific act (POSH doesn't
   cover, e.g., rape — that always goes to IPC/BNS regardless of location).
2. **If the incident happened at home / involves a partner or family member**
   → DV Act is primary; IPC/BNS sections apply *in addition* for criminal
   acts (DV Act relief is civil — protection/monetary orders — not a
   substitute for criminal reporting when the act is also a crime).
3. **If the incident is online/digital** → IT Act is primary; check whether
   the underlying act (e.g. stalking, modesty) also has an IPC/BNS
   equivalent that should be cited alongside it.
4. **Multiple laws often apply simultaneously** — the platform should
   surface all relevant sections, not force a single "correct" answer. A
   workplace incident involving photos, for instance, could trigger POSH +
   IT Act + IPC/BNS §74 all at once.

*Compiled by Person 1 — cross-check against actual retrieved chunks during
Day 3-5 testing, and flag any mismatch back to this table so it stays
accurate as the source of truth.*
