# Hindi Test Phrases — Voice & Translation Testing
Legal Sakhi — Day 18 Deliverable (Person 1)

Purpose: a small set of Hindi phrases covering all 4 law categories, for
Person 2/3 to test voice input (Whisper) and translation accuracy once
that feature is built. Each phrase includes an English back-translation so
the team can verify the translation layer preserves meaning correctly —
this matters a lot for a legal tool, since a mistranslation could point
someone toward the wrong law.

Phrases are written the way someone would actually speak, not formal
textbook Hindi — voice input needs to handle natural, sometimes
grammatically loose speech.

---

## Workplace harassment (POSH Act)

**1.** "मेरा बॉस मुझे बहुत गंदी नज़रों से देखता है और अजीब कमेंट करता है।"
*(My boss looks at me in a very dirty way and makes weird comments.)*

**2.** "ऑफिस में एक आदमी बार-बार मुझे छूने की कोशिश करता है।"
*(A man at the office keeps trying to touch me repeatedly.)*

**3.** "मैंने शिकायत की थी लेकिन कुछ नहीं हुआ, अब मैं क्या करूं?"
*(I filed a complaint but nothing happened, what should I do now?)*

## Online/cyber harassment (IT Act)

**4.** "कोई मेरी फोटो को इंस्टाग्राम पर बिना पूछे शेयर कर रहा है।"
*(Someone is sharing my photos on Instagram without asking.)*

**5.** "एक अनजान आदमी मुझे गंदे मैसेज भेजता रहता है।"
*(An unknown man keeps sending me dirty/obscene messages.)*

**6.** "मेरे पूर्व पति ने मेरा इंस्टाग्राम अकाउंट हैक कर लिया।"
*(My ex-husband hacked my Instagram account.)*

## Domestic violence (DV Act)

**7.** "मेरे पति ने कल रात मुझे फिर से मारा।"
*(My husband hit me again last night.)*

**8.** "मेरी सास मुझे बेटा न होने पर ताना मारती है।"
*(My mother-in-law taunts me for not having a son.)*

**9.** "मेरे पति मुझे घर से पैसे नहीं देते, सब कुछ अपने पास रखते हैं।"
*(My husband doesn't give me money from the house, keeps everything to himself.)*

**10.** "क्या मेरे पति मुझे घर से निकाल सकते हैं?"
*(Can my husband kick me out of the house?)*

## Assault (IPC/BNS)

**11.** "रास्ते में कुछ लड़कों ने मुझे परेशान किया और पीछा किया।"
*(Some boys harassed me on the road and followed me.)*

**12.** "किसी ने मेरे साथ जबरदस्ती करने की कोशिश की।"
*(Someone tried to force themselves on me.)*

## Vague/short phrases (test whether the system can handle brief, emotional input)

**13.** "मुझे मदद चाहिए।"
*(I need help.)*

**14.** "मैं बहुत डरी हुई हूं।"
*(I am very scared.)*

**15.** "क्या आप मेरी मदद कर सकते हैं?"
*(Can you help me?)*

---

## Notes for Person 2/3

- **Phrases 13-15 are intentionally vague** — the same test principle as
  the English edge cases. A good system should respond with a gentle
  follow-up question ("Can you tell me more about what happened?") rather
  than guessing a law category from three words.
- **Mixed Hindi-English (Hinglish) is common in real usage** — e.g. "boss
  bahut ajeeb behave karta hai" — if time allows, it's worth testing at
  least one Hinglish phrase too, since many users will naturally type this
  way rather than pure Hindi.
- If Whisper's transcription introduces errors (common with regional
  accents), test the pipeline with the *correct* text first to isolate
  whether an issue is a transcription problem or a legal-retrieval problem
  before debugging further.
