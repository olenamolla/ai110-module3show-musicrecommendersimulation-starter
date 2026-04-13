"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

import os
from recommender import load_songs, recommend_songs

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --- User Profiles ---

# Standard profiles
HIGH_ENERGY_POP = {
    "label":         "High-Energy Pop",
    "genre":         "pop",
    "mood":          "happy",
    "energy":        0.90,
    "acoustic_level": 0.05,
}

CHILL_LOFI = {
    "label":         "Chill Lofi",
    "genre":         "lofi",
    "mood":          "chill",
    "energy":        0.38,
    "acoustic_level": 0.80,
}

DEEP_INTENSE_ROCK = {
    "label":         "Deep Intense Rock",
    "genre":         "rock",
    "mood":          "intense",
    "energy":        0.92,
    "acoustic_level": 0.10,
}

# Edge case / adversarial profiles
CONFLICTING_SAD_ENERGY = {
    "label":         "Edge Case: High Energy but Sad",
    "genre":         "blues",
    "mood":          "sad",
    "energy":        0.90,   # high energy + sad mood rarely coexist in the catalog
    "acoustic_level": 0.50,
}

NONEXISTENT_GENRE = {
    "label":         "Edge Case: Genre Not in Catalog",
    "genre":         "bossa nova",  # no songs with this genre in songs.csv
    "mood":          "relaxed",
    "energy":        0.40,
    "acoustic_level": 0.70,
}

EXTREME_ACOUSTIC = {
    "label":         "Edge Case: Maximum Acoustic Preference",
    "genre":         "folk",
    "mood":          "melancholic",
    "energy":        0.50,
    "acoustic_level": 1.0,  # wants fully acoustic — tests the proximity floor
}


def print_recommendations(user_prefs: dict, recommendations: list) -> None:
    """Print a formatted block of recommendations for one user profile."""
    print("\n" + "=" * 50)
    print(f"  Profile: {user_prefs['label']}")
    print(f"  Genre: {user_prefs['genre']} | Mood: {user_prefs['mood']} | Energy: {user_prefs['energy']}")
    print("=" * 50)

    for i, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{i}  {song['title']} by {song['artist']}")
        print(f"    Genre: {song['genre']} | Mood: {song['mood']} | Energy: {song['energy']}")
        print(f"    Score: {score:.2f} / 4.50")
        print(f"    Why:")
        for reason in explanation.split(", "):
            print(f"      - {reason}")

    print("\n" + "=" * 50)


def main() -> None:
    songs = load_songs(os.path.join(BASE_DIR, "data", "songs.csv"))
    print(f"Loaded songs: {len(songs)}")

    profiles = [
        HIGH_ENERGY_POP,
        CHILL_LOFI,
        DEEP_INTENSE_ROCK,
        CONFLICTING_SAD_ENERGY,
        NONEXISTENT_GENRE,
        EXTREME_ACOUSTIC,
    ]

    for user_prefs in profiles:
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print_recommendations(user_prefs, recommendations)


if __name__ == "__main__":
    main()
