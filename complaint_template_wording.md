# Complaint Draft — Exact Wording Templates
Legal Sakhi — Day 11 Deliverable (Person 1)

Purpose: the actual paragraph-level wording Person 2's AI should fill in,
using the fields defined in `complaint_template_structure.md`. Three
templates are provided since different authorities expect different tone
and structure — the AI should pick the right one based on `law_identified`.

Placeholders use `{field_name}` matching the structure doc's field names
exactly, so Person 2 can do a direct find-and-replace or prompt-fill.

---

## Template A — Workplace Harassment Complaint (to Internal/Local Complaints Committee)

```
To,
The Presiding Officer,
Internal Complaints Committee,
{authority_to_file_with}

Subject: Complaint of Sexual Harassment under Section 9 of the Sexual
Harassment of Women at Workplace (Prevention, Prohibition and Redressal)
Act, 2013

Respected Madam/Sir,

I, {complainant_name}, wish to file a formal complaint regarding an
incident of sexual harassment I experienced at my workplace.

Details of the incident:
Date of incident: {incident_date}
Location: {incident_location}
Respondent: {respondent_name_or_description}

Description of the incident:
{incident_description}

This complaint is being filed under {law_identified}, which prohibits such
conduct at the workplace.

{witnesses_paragraph}
{evidence_paragraph}

I request the Committee to conduct an inquiry into this matter in
accordance with the provisions of the Act and take appropriate action.
{desired_outcome_paragraph}

I am available to provide further information or clarification as required
during the inquiry process.

Yours sincerely,
{complainant_name}
{complainant_contact}
Date: [DATE OF FILING]
```

---

## Template B — Police Complaint / FIR Draft (for criminal offences under IPC/BNS or IT Act)

```
To,
The Station House Officer,
[POLICE STATION NAME — TO BE FILLED BY COMPLAINANT],
{incident_location}

Subject: Complaint regarding {law_identified}

Respected Sir/Madam,

I, {complainant_name}, wish to lodge a complaint regarding the following
incident.

Date of incident: {incident_date}
Place of incident: {incident_location}
Person(s) involved: {respondent_name_or_description}

Description of the incident:
{incident_description}

Based on the above, I believe this incident falls under {law_identified},
and I request that an First Information Report (FIR) be registered and
appropriate investigation and action be taken.

{witnesses_paragraph}
{evidence_paragraph}

I am willing to cooperate fully with the investigation and provide any
additional information or evidence as required.

Yours sincerely,
{complainant_name}
{complainant_contact}
Date: [DATE OF FILING]

---
Note: If the police decline to register an FIR, you have the right to send
this complaint in writing to the Superintendent of Police by post, or
approach the Magistrate directly under Section 175(3), Bharatiya Nagarik
Suraksha Sanhita (equivalent to the earlier Section 156(3), CrPC).
```

---

## Template C — Domestic Violence Application (to Magistrate, under DV Act Section 12)

```
IN THE COURT OF THE MAGISTRATE AT [JURISDICTION — TO BE FILLED]

Application under Section 12 of the Protection of Women from Domestic
Violence Act, 2005

Applicant: {complainant_name}
Respondent: {respondent_name_or_description}

Details of the domestic relationship:
[Relationship to respondent — e.g. spouse, partner, family member — TO BE
CONFIRMED WITH APPLICANT]

Description of domestic violence experienced:
{incident_description}

Date(s) of incident(s): {incident_date}
Location: {incident_location}

This application is filed under {law_identified}, and the applicant seeks
the following relief(s) from this Hon'ble Court:
{desired_outcome_paragraph}
[ ] Protection Order (Section 18)
[ ] Residence Order (Section 19)
[ ] Monetary Relief (Section 20)
[ ] Other relief as the Court deems fit

{witnesses_paragraph}
{evidence_paragraph}

The applicant prays that this Hon'ble Court may be pleased to grant the
relief(s) sought above and pass any other order(s) as deemed just and
proper in the interest of justice.

Applicant's signature: {complainant_name}
Contact: {complainant_contact}
Date: [DATE OF FILING]

---
Note: A Protection Officer or the Domestic Incident Report (DIR) usually
accompanies this application. If the applicant hasn't yet contacted a
Protection Officer, direct them to the nearest DSLSA/SLSA office (see
legal_aid_centers.json) for assistance before filing.
```

---

## Shared sub-paragraph snippets (used across all 3 templates)

**`{witnesses_paragraph}`** — only include if `witnesses` field is non-empty:
```
Witnesses to this incident include: {witnesses}. They may be able to
corroborate the details described above.
```

**`{evidence_paragraph}`** — only include if `evidence_available` field is
non-empty:
```
The following evidence is available in support of this complaint:
{evidence_available}.
```

**`{desired_outcome_paragraph}`** — only include if `desired_outcome` field
is non-empty; otherwise default to a generic closing line:
```
Default (no specific outcome stated):
"I request that appropriate action be taken as per the law."

If desired_outcome is stated:
"Specifically, I am seeking: {desired_outcome}."
```

---

## Template selection logic (for Person 2)

```
if "POSH Act" in law_identified:
    use Template A
elif "DV Act" in law_identified:
    use Template C
elif any(law in law_identified for law in ["IPC", "BNS", "IT Act"]):
    use Template B
elif multiple categories present (e.g. POSH + IPC/BNS together):
    generate BOTH templates — one complaint often needs filing in two
    places simultaneously (e.g. an internal workplace complaint AND
    a police FIR for the same underlying act)
```

## Mandatory disclaimer (append to every generated draft, regardless of template)

```
⚠️ This is an AI-generated draft to help you organize your complaint. It
is not a substitute for legal advice. Please review it carefully — ideally
with a lawyer or a free legal aid center — before filing, and confirm all
placeholder fields marked in [BRACKETS] before submission.
```
