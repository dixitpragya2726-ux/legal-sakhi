# Legal Data — Documentation

This covers the two datasets Person 1 built: the legal knowledge base
(`/legal-docs`) and the legal aid centers directory (`legal_aid_centers.xlsx`
/ `.json`).

---

## 1. `/legal-docs` — Legal Knowledge Base

Plain-text extracts of Indian statutes relevant to this platform, cleaned of
page numbers, footnotes, and PDF artifacts, with standardized section
headers. Intended for chunking + embedding into the RAG vector database.

| File | Act | Sections covered |
|---|---|---|
| `posh_act.txt` | Sexual Harassment of Women at Workplace Act, 2013 | 2, 3, 4, 9, 10, 11 |
| `it_act.txt` | Information Technology Act, 2000 | 66, 66C, 66D, 66E, 67 |
| `dv_act.txt` | Protection of Women from Domestic Violence Act, 2005 | 3, 12, 17, 18, 19, 20 |
| `ipc_bns_sections.txt` | Bharatiya Nyaya Sanhita, 2023 (with IPC cross-references) | 63, 64, 67, 74, 75, 76, 77, 78, 79 |

**Format:** each section is delimited by a `====` header block containing the
section number (and BNS/IPC cross-reference where applicable), followed by
plain-language-adjacent statute text. This format is deliberately consistent
across all 4 files so a single chunking script can process them the same way
— split on `SECTION` headers, one chunk per section.

**Important notes for whoever builds the chunking/ingestion script (likely
Person 2):**
- Each `====` block is one atomic legal concept — this is the natural chunk
  boundary. Don't chunk by fixed character count; chunk by section.
- BNS is the current law (post-July 2024); IPC numbers are kept alongside
  since older records, police habits, and some case law still reference
  IPC.
- These are **not exhaustive** — only sections relevant to workplace
  harassment, cyberstalking/image abuse, domestic violence, and assault/
  modesty/rape were extracted. If the RAG pipeline needs to handle a
  scenario type not covered here (e.g. dowry death, acid attacks), flag it
  and we'll extract the relevant section.
- Legal text was cross-checked against official sources (India Code, NALSA,
  and verified legal commentary) as of August 2026, but a lawyer/legal
  reviewer should ideally sanity-check before this goes anywhere near real
  users.

---

## 2. `legal_aid_centers.xlsx` / `legal_aid_centers.json` — Resource Directory

50 verified entries covering free legal aid, women's helplines, and support
NGOs across India, for the map/resource-finder feature.

**Structure (9 columns / JSON keys):**

| Column | JSON key | Description |
|---|---|---|
| City/State/Scope | `scope` | Geographic scope — a state name, "National (All India)", or a city |
| Organization Name | `name` | Full name of the organization |
| Type | `type` | Government Legal Aid / Government Commission / Police / NGO / Emergency Response / Cyber Crime Reporting |
| Phone / Helpline | `phone` | Contact number(s), as published |
| Address | `address` | Office address where available |
| Latitude / Longitude | `latitude` / `longitude` | **City-level approximate coordinates** — see caveat below |
| Notes | `notes` | What the org handles, hours, special features (e.g. WhatsApp lines) |
| Source | `source` | Where this was verified — always a government (`.gov.in`, `.nic.in`) or official org site |

**Breakdown of the 50 entries:**
- 7 national helplines (NCW, NALSA, Women Helpline 181, Police 112, Cyber
  Crime 1930, NHRC, Ministry of WCD)
- 37 State/UT Legal Services Authorities — full coverage of every state and
  union territory in India
- 6 city-specific extras (Delhi Commission for Women, Jagori, Shakti
  Shalini, Mumbai Police Women Helpline, SNEHA, Majlis Legal Centre)

**⚠️ Known limitations — read before using in the map feature:**
1. **Coordinates are city-level, not building-level.** Every organization in
   e.g. Bengaluru maps to the same point (city center). Fine for a demo pin;
   run each real address through a geocoder (Nominatim is free — see
   Day 1 notes) before any real deployment.
2. **A few NGO phone numbers are marked "see website"** (Jagori, Shakti
   Shalini, SNEHA, Majlis) — their current numbers weren't confirmed in
   research and should be verified by calling/checking their site directly
   before demo day, rather than guessed.
3. **Ladakh's SLSA has no published phone number** (email contact only) —
   correctly reflected in the data, not a bug.
4. **Government helpline numbers can change** — worth a quick re-check of
   the top 5-6 (14490, 15100, 181, 112, 1930) close to the actual demo, since
   these get occasional updates.

**How the backend should use this:** the JSON version is ready to load
directly — each object is one map pin / resource card, with `latitude`/
`longitude` as `null` for phone-only national helplines (they shouldn't get
a map pin, just a "call" button in the UI).

---

*Compiled by Person 1 (Legal Docs + Data Prep) — Day 1-2 of the hackathon.*
