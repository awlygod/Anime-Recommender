# Data Preparation

This project uses the Anime Dataset 2023 from Kaggle, containing around twenty five thousand anime entries with details such as title, genres, synopsis, type, episodes, score, and popularity.

## Why Preprocessing Was Necessary

The recommendation engine relies on clean, consistent text in the genres and synopsis fields to build a meaningful TF IDF model, and relies on genuinely numeric score and popularity values to rank preference based results correctly. Without handling missing values and placeholder text up front, both the similarity model and the ranking logic would either crash outright or silently produce misleading results.

## Preprocessing Steps

All of this happens inside `backend/seed.py` before any data is inserted into PostgreSQL.

### Missing Text Fields

Missing genres and synopsis values are replaced with empty strings rather than left as null. These two fields are combined and fed directly into the TF IDF vectorizer, and a null value at that stage would break the text combination step entirely.

### The UNKNOWN Placeholder Problem

The source dataset does not leave missing numeric fields blank. Instead, several columns, score, popularity, and episodes, sometimes contain the literal text `UNKNOWN` in place of a real number. A plain numeric conversion on a value like this throws a `ValueError`, which would stop the entire seeding process partway through.

A helper function, `clean_numeric`, handles this by attempting a `float()` conversion and falling back to a default value whenever that conversion fails. For the score field this default is `0.0`, and for popularity the result is wrapped in `int()` with a fallback of `0`, so both end up as zero either way, just as different numeric types matching their respective columns. This is why some anime appear in the app with a score of `N/A` rather than a number, the underlying data genuinely did not have one recorded, and the app is showing that honestly rather than inventing a value.

### Why Episodes Is Stored As Text, Not A Number

The episodes column has the same `UNKNOWN` issue, but rather than applying the same numeric fallback, it is simply cast to a string for every row. Since episode count is only ever displayed, never used in any calculation or filtering logic, there was no reason to force it into a numeric type and deal with the conversion problem at all. Keeping it as text sidesteps the issue completely.

## Inserting Into PostgreSQL

After cleaning, the dataset is inserted into a single table using SQLAlchemy's `bulk_insert_mappings`, which is significantly faster than inserting rows one at a time for a dataset this size.

Before doing any of this work, the seeding script checks whether the table already contains rows, and exits immediately if it does. This is what makes it safe for `seed.py` to run every single time the backend container starts, without ever creating duplicate rows on a restart.

## Dataset Source

Dataset used, Anime Dataset 2023.

Source, https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset