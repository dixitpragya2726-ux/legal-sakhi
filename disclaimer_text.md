# Disclaimer Text & Placement
Legal Sakhi — Day 20 Deliverable (Person 1)

Purpose: exact wording for the "not a substitute for a lawyer" disclaimer,
plus where it needs to appear across the app. This matters both ethically
(survivors need to understand this is guidance, not legal representation)
and practically (protects the team from claims of unauthorized legal
practice).

---

## Primary disclaimer (long form)

Used on: first chat interaction, complaint draft screen

```
This tool provides general legal information to help you understand your
rights and options — it is not a substitute for advice from a qualified
lawyer. Laws and procedures can vary based on your specific situation, and
this information may not cover every detail relevant to your case. For
advice specific to you, please consult a lawyer or a free legal aid center
— you can find nearby options using the "Find Help" feature in this app.
```

## Short form (persistent banner)

Used on: every screen, as a small persistent footer/banner — should not be
intrusive but should always be visible

```
⚠️ This is legal information, not legal advice. Not a substitute for a lawyer.
```

## Complaint draft-specific disclaimer

Used on: appended to the bottom of every generated complaint draft
(already included in `complaint_template_wording.md`, repeated here for
consistency)

```
⚠️ This is an AI-generated draft to help you organize your complaint. It
is not a substitute for legal advice. Please review it carefully — ideally
with a lawyer or a free legal aid center — before filing, and confirm all
placeholder fields marked in [BRACKETS] before submission.
```

## Evidence checklist-specific note

Used on: evidence checklist screen, as a brief intro line before the
checklist itself

```
This checklist covers common types of evidence that can support your case.
It's a general guide, not a complete or guaranteed list — a lawyer or legal
aid center can advise on what's most relevant to your specific situation.
```

## Crisis/safety note (separate from legal disclaimer, but related)

Used on: chat screen, shown contextually if the conversation suggests
immediate danger (this is a product/safety decision, not just legal
boilerplate — flagging for team discussion on whether/how to detect this)

```
If you are in immediate danger, please call 112 (Police Emergency) right
away. This tool is not designed for emergency response.
```

---

## Placement summary (for Person 3)

| Screen | Disclaimer version | Position |
|---|---|---|
| Chat screen (first message) | Primary (long form) | Shown once, as the AI's first message before any legal explanation |
| Chat screen (ongoing) | Short form | Persistent small banner, bottom of screen |
| Complaint draft screen | Complaint-specific | Bottom of the generated draft, before any download/copy button |
| Evidence checklist screen | Evidence-specific | Top of the checklist, before the items |
| Any screen (contextual) | Crisis/safety note | Only if danger-related keywords are detected in conversation — flag to Person 2 for keyword logic if pursued |

## Tone principles

- **Never sound legalistic or cold** — this app is for someone possibly in
  distress. "This is legal information, not legal advice" should feel like
  a caring clarification, not corporate fine print.
- **Never repeat the disclaimer so often it becomes noise** — the short
  form banner should be persistent but visually quiet (small text, muted
  color), not a repeated pop-up that interrupts the conversation.
- **Always pair the disclaimer with a next step** — don't just say "consult
  a lawyer," point to the "Find Help" feature so the disclaimer itself is
  useful, not just a liability shield.
