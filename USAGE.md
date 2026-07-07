# Usage Guide

This guide explains how to use the AnimeMatch UI to find anime recommendations tailored to what you already like, what you prefer, or both.

## How to Use the App

Open the application. Make sure the Docker containers are running, then navigate to http://localhost:3000 in your web browser.

Choose how you want to search. There are three ways to get recommendations, and you can use any of them depending on what you already know you want.

* Search for an anime you already enjoy using the search bar at the top. As you type, matching titles appear in a dropdown. Selecting one tells the system to find anime similar to that title.
* Set preferences using the genre chips and the type dropdown below the search bar. You can select as many genres as you like and optionally pick a type such as TV, Movie, or OVA.
* Combine both by selecting an anime and also setting preferences. The system will first find anime similar to your selected title, then narrow that list down further using your chosen genres and type.

Submit. Click the Get recommendations button to send your selection to the backend.

## Reading the Results

The system returns a ranked grid of anime cards based on whichever mode was triggered by your input.

* Poster and Title, the anime's cover image and name.
* Genres, the genre tags associated with that anime.
* Score, the anime's average rating from the dataset. Some entries show N/A where the original dataset did not have a recorded score.
* Match Percentage, shown as a rounded number derived from the similarity or ranking score behind that result. For content based results this comes from cosine similarity against your selected anime. For preference only results this is a normalized version of the anime's own score, since there is no similarity being measured in that mode.

## Worked Example

Let's assume you search for and select Naruto, and also select the Action genre with no type filter.

Expected behavior, the backend runs its combined mode. It first finds a wide pool of anime that are textually similar to Naruto based on genres and synopsis, things like Naruto: Shippuuden, Boruto, and various Naruto movies typically appear here. It then narrows that pool down to only the ones that also contain Action in their genre list, and finally ranks whatever remains by similarity score, highest first.

You will see cards for closely related titles such as Naruto: Shippuuden and Boruto: Naruto Next Generations near the top of the results, each showing a match percentage reflecting how textually similar that title is to the one you searched for, alongside its genres and score.

If instead you had only set preferences, for example Action and Comedy with no anime selected, the results would look different. That mode does not measure similarity to any single title, it simply filters the full dataset down to anime containing those genres and ranks them by their own score, so you would see a broader mix of popular Action and Comedy titles rather than anime specifically related to one show.