# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Real-world recommenders like Spotify or Youtube use massive amounts of data and they track every song users skip, replay, add to playlist. Then, they find other users who behave like you and suggest what they listened to next. That's called collaborative filtering. My version is simpler and does not need any listening history. Instead it uses content-based filtering. It looks directly at the attributes of each song and compares them to what the user says they want. For each song, it computes a score using a weighted formula: genre match counts the most because genre is hard preference that rarely changes, mood comes second because it reflects the user's current vibe, and energy and acousticness fill the rest with proximity math (songs with the user's target values score higher). Then it sorts all the scores and returns the top K results. 

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo

  * genre — matched against user's favorite genre (worth 35% of score)
  * mood — matched against user's favorite mood (worth 25% of score)
  * energy — proximity to user's target energy (worth 25% of score)
  * acousticness — proximity to user's acoustic preference (worth 15% of score)
  * tempo_bpm — used as tie-breaker only
  * id, title, artist — display only, not scored
  * valence, danceability — loaded but unused in scoring


- What information does your `UserProfile` store

  * favorite_genre — binary match against song.genre
  * favorite_mood — binary match against song.mood
  * target_energy — numeric target (0.0–1.0) for energy proximity
  * likes_acoustic — converted to 1.0 (acoustic) or 0.0 (electronic) for proximity scoring

- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

---

### Algorithm Recipe

Every song is scored out of 4.5 points:

* `+2.0` — genre matches the user's favorite genre
* `+1.0` — mood matches the user's mood
* `+0 to 1.0` — energy is close to the user's target (`1.0 - difference`)
* `+0 to 0.5` — acousticness is close to the user's preference

Songs are then sorted highest to lowest and the top K are returned with a short reason explaining why each was picked.

### Potential Biases

* Genre carries the most weight, so a perfect mood and energy match in a different genre can still lose to a weaker same-genre song
* Mood is all-or-nothing — "intense" and "energetic" feel similar but the system treats them as completely different
* Results can lack variety — the system always picks the closest matches with no built-in diversity

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

### Tests Performed (5 total — all passing)

* `test_recommend_returns_songs_sorted_by_score` — pop/happy user gets the pop song ranked first
* `test_explain_recommendation_returns_non_empty_string` — explanation is a non-empty string
* `test_no_genre_match_scores_lower` — a non-matching genre always ranks below a matching one
* `test_recommend_returns_k_results` — `recommend(k=1)` returns 1 song, `recommend(k=2)` returns 2
* `test_perfect_match_scores_higher_than_partial` — full genre+mood+energy match outscores a partial match

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

The biggest learning moment was realizing that the scoring logic wasn't the hard part but the data was. Once I built the scoring function, it worked exactly as written. But the results didn't always feel right, and that had nothing to do with the code. It was because the labels in the CSV didn't capture the full picture of a song. "Gym Hero" is tagged as pop and intense, so it scores well for a happy pop user on paper, but nobody would actually recommend it for that mood. That gap between what the numbers say and what a human would feel was the most surprising thing about this project.

Using AI tools helped a lot with the structural parts: setting up the scoring formula, understanding proximity math, and thinking through edge cases. But I had to double-check anything involving weights and expected outputs, because the AI would sometimes suggest a formula that looked right but didn't match what I actually wanted to test. Running the code myself and checking whether "Gym Hero" or "Moonlit Sonata" showed up where I expected was more useful than trusting any explanation alone.

What surprised me most was how quickly a simple four-feature formula started to feel like a real recommender. It's just math, but when you run it against real song names and see "Midnight Coding" rise to the top for a chill user, it feels intelligent. That illusion breaks fast once you look at the edge cases — but it helped me understand why people trust these systems more than they probably should.

If I extended this project, I'd try grouping similar moods together so "chill" and "relaxed" score as partial matches, and I'd add a diversity penalty so the top 5 doesn't always pull from the same genre. I'd also want to test what happens with a much larger catalog — most of the weaknesses here came from having only 1–2 songs per genre, not from the algorithm itself.


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

