# Project Rationale

## Why I Chose This Project

Finding a good anime to watch can be difficult because thousands of titles exist across many genres, formats, and eras. Most recommendation systems take one of two approaches. Either they suggest titles similar to something you already like, or they let you filter by genre and type without considering similarity at all.

I wanted to build something that does both at once. A user can pick an anime they already enjoy, set genre and type preferences, or combine the two together. Building this also gave me hands on experience with recommendation logic, REST API design, containerization with Docker, and connecting a real database to a full stack application.

## What Makes This Project Special

Instead of relying on a single matching method, this application supports three modes of recommendation depending on what the user provides.

If a user selects only an anime, the system finds other anime with similar genres and synopsis using text similarity.

If a user selects only preferences such as genre or type, the system filters and ranks anime according to those choices.

If both are provided, the application first finds anime similar to the selected title and then narrows that list down using the chosen preferences, producing results that are both similar and relevant to what the user actually wants.

This matters because most recommendation demos only implement one strategy. Supporting all three, and having the backend decide which one to run based on what the frontend actually sends, was the main technical challenge of this project, and the part I can speak to in the most depth if asked.