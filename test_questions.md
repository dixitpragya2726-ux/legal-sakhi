# Test Questions for RAG Retrieval Testing
Legal Sakhi — Day 3 Deliverable (Person 1)

Purpose: Person 2 uses these to verify the retrieval pipeline pulls the
*correct* legal section for a realistic, plainly-worded incident description
— the way an actual user would type it, not lawyer-speak. For each, the
"Expected section(s)" is what a correct retrieval should surface as the
top result(s). If retrieval returns something else, that's a chunking or
embedding issue to debug, not a wording issue in the test question.

---

### 1. Workplace harassment — verbal
**Query:** "My boss keeps making comments about my body and it makes me so uncomfortable at work."
**Expected section(s):** POSH Act Section 2(n) (definition of sexual harassment), Section 3

### 2. Workplace harassment — physical
**Query:** "My manager touched my shoulder and back in a way that felt inappropriate during a meeting."
**Expected section(s):** POSH Act Section 3; IPC/BNS Section 74 (outrage modesty)

### 3. Workplace harassment — filing process
**Query:** "How do I file a complaint against my colleague for harassment? Is there a deadline?"
**Expected section(s):** POSH Act Section 9 (complaint + 3-month limit), Section 4 (Internal Committee)

### 4. Quid pro quo harassment
**Query:** "My supervisor said he'd promote me faster if I agreed to go on a date with him."
**Expected section(s):** POSH Act Section 3(2)(i) (promise of preferential treatment)

### 5. Stalking — in person
**Query:** "A man from my building keeps following me and trying to talk to me even though I've told him to stop."
**Expected section(s):** IPC/BNS Section 78 (stalking)

### 6. Stalking — online
**Query:** "Someone keeps checking my Instagram and messaging me even though I've blocked them on other apps."
**Expected section(s):** IPC/BNS Section 78(1)(ii) (monitoring electronic communication)

### 7. Image-based abuse / non-consensual photos
**Query:** "My ex is threatening to share private photos of me if I don't get back with him."
**Expected section(s):** IT Act Section 66E (privacy violation); IT Act Section 67 (obscene material)

### 8. Morphed/deepfake images
**Query:** "Someone made a fake edited photo of me and is sharing it in a group chat."
**Expected section(s):** IT Act Section 67; IT Act Section 66C/66D (if impersonation involved)

### 9. Online impersonation / fake account
**Query:** "There's a fake Instagram account using my photos and pretending to be me, messaging my friends."
**Expected section(s):** IT Act Section 66C (identity theft), Section 66D (cheating by personation)

### 10. Domestic violence — physical
**Query:** "My husband hit me again last night and I don't know what to do."
**Expected section(s):** DV Act Section 3 (definition — physical abuse); Section 12 (application to Magistrate)

### 11. Domestic violence — emotional/economic
**Query:** "My husband controls all our money and won't let me access our savings even for basic things."
**Expected section(s):** DV Act Section 3 (economic abuse); Section 20 (monetary relief)

### 12. Domestic violence — housing rights
**Query:** "Can my husband kick me out of our house even though it's in his name?"
**Expected section(s):** DV Act Section 17 (right to reside in shared household)

### 13. Domestic violence — protection order
**Query:** "How can I legally stop my husband from contacting me or coming near me?"
**Expected section(s):** DV Act Section 18 (protection orders)

### 14. Sexual assault / rape
**Query:** "I was forced into a sexual act against my will by someone I know."
**Expected section(s):** IPC/BNS Section 63 (definition of rape), Section 64 (punishment)

### 15. General "insult" / non-physical harassment in public
**Query:** "A man made lewd comments and gestures at me while I was walking to the market."
**Expected section(s):** IPC/BNS Section 79 (word, gesture, or act intended to insult modesty)

---

## Notes for Person 2

- Questions 1-4 test POSH Act retrieval specifically. If the pipeline
  confuses these with general IPC/BNS assault sections, the chunking or
  embedding may be weighting the wrong keywords (e.g. "boss," "workplace"
  should pull POSH, not generic assault law).
- Questions 5-6 and 7-9 are designed to test whether the system can tell
  *stalking* apart from *image-based abuse* apart from *impersonation* —
  three related but legally distinct IT Act/BNS provisions that a naive
  embedding might blur together.
- Questions 10-13 test whether DV Act retrieval correctly distinguishes
  *type* of relief needed (protection vs. monetary vs. housing) — a
  well-tuned system shouldn't just return "Section 3" for every DV query.
- If more than 3-4 of these return the wrong section on a first pass, it's
  worth revisiting chunk size (Day 6 task) before assuming the embedding
  model itself is the problem.
