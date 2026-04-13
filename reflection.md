# Reflection: Profile Comparisons

---

## High-Energy Pop vs. Chill Lofi

These two profiles are opposites. The High-Energy Pop profile wants fast, loud, electronic music and gets songs like "Sunrise City" and "Gym Hero" at the top — both pop, both high energy. The Chill Lofi profile wants slow, quiet, acoustic music and gets "Library Rain" and "Midnight Coding" instead. The results flip almost completely between the two lists, which makes sense because every feature they care about points in opposite directions. This pair showed the system working as intended — when preferences are very different, the recommendations are very different too.

---

## High-Energy Pop vs. Deep Intense Rock

Both profiles want high energy, but they want different genres and moods. Pop wants "happy," rock wants "intense." What's interesting is that some songs show up in both lists — specifically ones with very high energy scores like "Iron Collapse" and "Overdrive." The system surfaces them for both users because energy is now worth double points, so a near-perfect energy match can overcome a genre miss. This showed a real flaw: a rock fan doesn't actually want a pop song just because it's high energy, but the system sometimes recommends that anyway.

---

## Chill Lofi vs. Deep Intense Rock

The clearest contrast of all six profiles. Lofi wants low energy, high acousticness, chill mood. Rock wants high energy, low acousticness, intense mood. Every single feature pulls in the opposite direction, so they share zero songs in their top 5. This pair is useful as a sanity check — if they ever shared a top result, something would be wrong with the scoring logic.

---

## High-Energy Pop vs. Edge Case: High Energy but Sad

Both want high energy (0.9), but one wants "happy" and the other wants "sad." In theory these should feel very different. In practice, they ended up sharing several of the same songs near the top — because energy is worth 2.0 points and mood is only worth 1.0. A sad user wanting high energy gets recommended the same workout tracks as the happy pop user, just ranked slightly differently. This is the "Gym Hero problem" — the system sees the energy match and doesn't fully register that the vibe is wrong. It's like a friend recommending a party anthem to someone who just went through a breakup, because "hey, it's upbeat and you said you wanted something energetic."

---

## Edge Case: Genre Not in Catalog vs. any standard profile

When the user's genre doesn't exist in the catalog (like "bossa nova"), the system can never award genre points. This means the score ceiling drops from 4.5 to 3.5, and the top results are driven entirely by mood and energy. Compared to the standard profiles, the recommendations feel more random and less personal. The list looks like "songs that aren't too far off on energy" rather than "songs you'd actually like." This was the most eye-opening result — it showed that the whole system leans on genre as its backbone, and without it, the recommendations lose their identity.

---

## Edge Case: Maximum Acoustic vs. Chill Lofi

Both profiles want calm, acoustic-leaning music and end up with some overlap — both surface songs like "Library Rain" and "Spacewalk Thoughts." The difference is that the Maximum Acoustic profile pushes acousticness all the way to 1.0, so it rewards classical and folk songs more than lofi ones (lofi sits around 0.71–0.86 acousticness, not quite 1.0). This slight difference in one number shifted a few results. It showed that acousticness proximity actually works — small changes in the target value produce small but noticeable changes in the ranking.
