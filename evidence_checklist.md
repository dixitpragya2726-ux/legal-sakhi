# Evidence Preservation Checklist — Content
Legal Sakhi — Day 13 Deliverable (Person 1)

Purpose: rule-based content (no AI needed, per the roadmap) mapping
incident type → what evidence to preserve. Person 2 can implement this as
a simple lookup: incident category in, checklist array out. Categories
match the `law_identified` categories already used in the complaint
template work, so the same classification logic can drive both features.

---

## Category 1: Workplace Harassment (POSH Act)

- [ ] Save any messages, emails, or chat logs from the person involved — take screenshots with visible timestamps and sender names, and also export/back up the original chat where possible.
- [ ] Write down the date, time, and exact location of each incident as soon as possible, including what was said or done, while your memory is fresh.
- [ ] Note the names of anyone who witnessed the incident or who you told about it afterward (even informally, like a friend or family member) — later witness statements can matter.
- [ ] Check if the location has CCTV coverage; if so, request preservation of footage promptly, since it's often overwritten within days to weeks.
- [ ] Keep a copy of your employment contract, offer letter, or ID card showing you work at that workplace, in case employment relationship needs to be established.
- [ ] If you've already reported this informally (to a friend, HR, or manager) and got a response, save that too — it can show a pattern or a lack of action.

## Category 2: Online / Cyber Harassment (IT Act)

- [ ] Take screenshots of every message, post, or comment — make sure the screenshot shows the sender's username/profile, the full message, and the timestamp.
- [ ] Do NOT delete the harasser's messages or block them until you've saved everything — blocking can sometimes hide message history depending on the app.
- [ ] Save the profile URL/link of the account involved, not just their display name (usernames can be changed later).
- [ ] If images or videos were shared without consent, save the original file if you have access to it (not just a screenshot), since original files preserve metadata that can help verify authenticity.
- [ ] Use your device or a screen-recording app to capture how the content appears live (especially for disappearing content like Stories, which vanish after 24 hours).
- [ ] Report the content on the platform itself (most apps have a "report" function) — this creates a timestamped record on the platform's side too, separate from your own.
- [ ] Note down the exact date/time you first saw the content and any dates it reappeared or was reshared.

## Category 3: Domestic Violence (DV Act)

- [ ] If there is a physical injury, take clear photos as soon as possible, and consider a medical examination within 24-48 hours — hospitals can create a Medico-Legal Certificate (MLC), which is strong evidence.
- [ ] Keep a private, dated log of incidents, even ones that felt "minor" — a documented pattern over time is often more persuasive than a single incident.
- [ ] Save any threatening messages, call recordings, or voicemails, the same way as the cyber harassment category above.
- [ ] If financial abuse is involved, keep copies of bank statements, salary slips, or property documents that show what's being withheld or controlled.
- [ ] Identify anyone who may have witnessed the abuse or its aftermath (neighbors, domestic help, family members) and note their contact details.
- [ ] If you've already contacted a Protection Officer, NGO, or helpline, keep any reference/complaint numbers they gave you.
- [ ] If safe to do so, keep a small "go-bag" with copies of ID documents, this evidence log, and emergency contacts, in case you need to leave quickly.

## Category 4: Physical Assault / Sexual Assault (IPC/BNS)

- [ ] Try not to shower, change clothes, or clean up before a medical examination if the assault was very recent — this can preserve forensic evidence, even though it's an extremely difficult thing to ask of someone in this situation.
- [ ] Go to a hospital or health center as soon as possible; government hospitals are required to provide free treatment and documentation for medico-legal cases.
- [ ] If you do change clothes, keep the clothes worn during the incident in a paper bag (not plastic, which can degrade evidence), without washing them.
- [ ] Write down everything you remember as soon as you're able to — exact words said, sequence of events, physical description of the person if unknown to you.
- [ ] Note any witnesses, including anyone who saw you immediately before or after the incident, even if they didn't witness the act itself.
- [ ] If the assault happened in a place with cameras (street, building, transport), note the exact location and time so footage can be requested quickly.

## General principles (apply across all categories)

- [ ] When in doubt, save it — it's easier to decide something isn't needed later than to recover something already deleted.
- [ ] Back up evidence in at least two places (e.g. phone + email to yourself, or phone + cloud storage) in case a device is lost, damaged, or taken.
- [ ] Evidence collection should never put you in danger — if preserving something (like confronting someone for a screenshot) would escalate risk, prioritize your safety first and document what you can safely gather later.

---

## Implementation note for Person 2

Simple mapping structure for the backend:

```python
EVIDENCE_CHECKLISTS = {
    "posh_act": [...],       # Category 1 items
    "it_act": [...],         # Category 2 items
    "dv_act": [...],         # Category 3 items
    "ipc_bns_assault": [...] # Category 4 items
}

def get_checklist(law_identified: list[str]) -> list[str]:
    # Return combined, de-duplicated checklist if multiple laws apply
    # (matches the multi-law handling already used in the complaint draft feature)
    ...
```

If an incident spans multiple categories (e.g. workplace + cyber, per test
scenario #35), combine the relevant checklists rather than picking just
one — the "General principles" section should always be appended last,
regardless of category.
