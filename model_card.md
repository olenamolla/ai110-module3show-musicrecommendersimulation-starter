# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

**MoodMatch 1.0**

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

Suggests songs that match a user's current mood and taste. Built for classroom exploration, not for real users or production apps. Assumes the user knows their favorite genre, mood, and energy level.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

Every song gets a score out of 4.5. Genre match gives +1.0, mood match gives +1.0, energy closeness gives up to +2.0, and acousticness closeness gives up to +0.5. Songs are ranked from highest to lowest and the top 5 are returned with a reason explaining why each was picked.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

20 songs total — 10 original, 10 added. Features include genre, mood, energy, tempo, acousticness, valence, and danceability. 17 genres and 12 moods are covered. Most genres have only 1–2 songs, so the catalog is small and uneven. Lyrics, language, and listening history are not included at all.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

Works well for users whose genre exists in the catalog. Transparent, you always see why a song was picked. Still returns useful results even when the genre is missing. Easy to tune by adjusting the weights.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The biggest weakness is that most genres in the catalog have only one or two songs. This means users who prefer a common genre like pop always get a strong genre match, while users who prefer something like blues or folk might get zero genre points because there are so few songs for them. The system ends up working much better for some users than others, not because their taste is harder to match, but simply because the dataset is unbalanced. Another issue is that mood matching is all-or-nothing — "chill" and "relaxed" feel like the same vibe to most people, but the system treats them as completely different and gives zero credit. This can make the results feel off even when the recommended song is genuinely close to what the user wants.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I tested six profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and three edge cases — a user with conflicting preferences (sad mood but high energy), a user whose favorite genre doesn't exist in the catalog, and a user who wants fully acoustic music.

The results mostly made sense. The Chill Lofi profile correctly surfaced the two lofi songs at the top, and the Rock profile ranked the most intense songs first. What surprised me was the Happy Pop profile — "Gym Hero" kept showing up near the top even though it has an intense mood, not a happy one. The reason is that Gym Hero is tagged as pop, so it earns the full genre bonus, and its energy (0.93) is close enough to the user's target (0.9) to score well on energy too. The system doesn't notice that "intense" and "happy" feel completely different to a real listener — it just sees that genre and energy both match and ranks it high. It's like recommending a loud workout track to someone who just wants something upbeat and fun. The numbers check out, but the vibe is wrong.

The most surprising result came from the edge case profile whose genre wasn't in the catalog at all. Instead of returning nothing useful, the system just ranked songs by energy and acousticness alone — which actually produced a reasonable-sounding list. It showed that the scoring still works even when the strongest signal (genre) is missing.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

* Group similar moods so "chill" and "relaxed" count as a partial match
* Add more songs per genre so niche users get fair results
* Add a diversity rule so the top 5 doesn't always come from the same genre

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

Building this showed how much the results depend on the data, not just the logic. The scoring rules were simple, but the recommendations were only as good as what was in the catalog. A song kept showing up in the wrong place not because the code was broken, but because the labels didn't capture the full picture. Real apps like Spotify have millions of songs — that scale is what makes their recommendations feel personal.

---

## 10. Intended Use and Non-Intended Use

**Intended:** classroom project to learn how content-based recommenders work.

**Not intended for:** real users, production apps, or making decisions about what music people should like.




