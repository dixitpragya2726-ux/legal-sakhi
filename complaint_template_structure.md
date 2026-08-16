# Complaint Draft — Template Structure
Legal Sakhi — Day 8 Deliverable (Person 1)

Purpose: defines the exact fields Person 2's `/draft-complaint` endpoint
needs to collect (from the conversation) and fill into a complaint letter.
This is the *structure* — Day 11 will add the exact formal wording that
goes around these fields.

---

## Core fields (every complaint type needs these)

| Field | Type | Source | Required? | Notes |
|---|---|---|---|---|
| `complainant_name` | string | User input | Yes | Full name as the survivor wants it to appear |
| `complainant_contact` | string | User input | Optional | Phone/email — some survivors may not want to share this in a draft they haven't decided to file yet |
| `incident_date` | string | User input | Yes | Exact date if known; accept "approximate" phrasing like "around mid-July" if exact date isn't remembered |
| `incident_location` | string | User input | Yes | Where it happened — workplace name, address, or general area |
| `incident_description` | string (long) | User's original conversation input | Yes | The raw description — AI should NOT heavily rewrite this, keep it close to the survivor's own words for accuracy in a legal document |
| `law_identified` | array of strings | AI-determined (from RAG retrieval) | Yes | e.g. ["POSH Act Section 3", "IPC/BNS Section 74"] — supports multiple laws per complaint (see scenario #35 from batch 2 testing) |
| `respondent_name_or_description` | string | User input | Optional | Name if known; otherwise a description ("my manager", "unknown man") — many survivors won't know full legal names |
| `authority_to_file_with` | string | Derived from `law_identified` | Yes | Auto-filled based on which law applies — see mapping below |

## Authority mapping (used to auto-fill `authority_to_file_with`)

| If `law_identified` includes... | `authority_to_file_with` becomes |
|---|---|
| POSH Act | "Internal Complaints Committee (IC)" or "Local Complaints Committee (LC), if no IC exists" |
| IT Act | "Cyber Crime Cell / nearest Police Station / cybercrime.gov.in" |
| DV Act | "Magistrate (via application under Section 12)" or "Protection Officer" |
| IPC/BNS (criminal sections) | "Nearest Police Station (for FIR)" |
| Multiple laws | List all relevant authorities, since a single incident may need parallel filings (e.g. POSH complaint to IC *and* police FIR for the same act) |

## Optional/supporting fields (nice-to-have, not blocking)

| Field | Type | Notes |
|---|---|---|
| `witnesses` | array of strings | Names/descriptions of anyone who saw or knows about the incident |
| `evidence_available` | array of strings | Cross-references the evidence checklist (Day 13) — e.g. ["screenshots", "witness statement"] |
| `prior_complaints_filed` | boolean + string | Whether this is a first complaint or a follow-up/escalation (relevant for POSH Act §18 appeals) |
| `desired_outcome` | string | What the survivor wants (e.g. "stop the harassment", "compensation", "protection order") — helps tailor the closing request paragraph |

## Design principles for Person 2 to keep in mind

1. **Never invent facts.** If a field is missing (e.g. exact date unknown),
   use a clear placeholder like `[DATE NOT SPECIFIED — PLEASE CONFIRM]`
   rather than guessing or leaving it blank silently.
2. **Preserve the survivor's own words in `incident_description`.** Heavy
   AI paraphrasing of the actual events risks changing legal meaning or
   losing detail that matters (exact words said, exact actions taken).
   Light cleanup (grammar, structure) is fine; rewriting the substance is
   not.
3. **One incident can map to multiple `law_identified` + multiple
   `authority_to_file_with` values** — don't force a single-law, single-
   authority output. Scenario #35 from the test batch (workplace touching +
   secret photos) is the test case for this.
4. **This is a draft, not a filed document.** Every generated complaint
   should carry a visible note: "This is a draft to help you organize your
   complaint. Please review it and consult a lawyer or the relevant
   authority before filing." (Ties into Day 20's disclaimer work.)

---

*Next: Day 11 will take this structure and write the exact formal wording/
paragraph templates that go around these fields, matching what a real
police station or e-FIR portal expects.*
