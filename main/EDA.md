


# Movie Recommendation System

This idea comes from the Kaggle dataset:
https://www.kaggle.com/shivamb/netflix-shows

We aim to perform EDA on the dataset of Netflix Shows and Movies, with the end-goal of creating a machine learning based recommendation system (returning 10 related movies or shows based on a user selection from the dataset).

## EDA

### Set Preliminaries

```r
library(ggplot2)
data_loc <- "~/Projects/Movie-Suggestion-System/data"
```
### Load-in data, initial summaries and error correction

```r
netflix_data <- read.csv(paste(data_loc, "/netflix_titles.csv", sep = ""), stringsAsFactors=FALSE)
dim(netflix_data)
head(netflix_data)
```
Our dataset contains 8807 entries with 12 features. Some are free-text, containing information about the title's cast, director, synopsis, etc. Other fields are comprised of more discrete data, such as type, country, and age rating. I've decided not to interpret all string features as factors, but rather convert the necessary columns to factors as and when I need.

The following are some summaries for the more discrete features of the data:


```
## [1] "Type"
```

```
## Error in table(netflix_data$type): object 'netflix_data' not found
```

```
## [1] "Country"
```

```
## Error in table(netflix_data$country): object 'netflix_data' not found
```

```
## [1] "Age Rating"
```

```
## Error in table(netflix_data$rating): object 'netflix_data' not found
```

It would be useful to obtain similar breakdowns for fields like genre or cast, which almost always contain multiple categories or actors. This will be my next aim.

Before that, however, the age rating feature clearly has erroneous entries, as time-values like "84 min", "74 min", etc almost definitely belong in the duration column. It will be simple to find these and correct them, but this also serves as a reminder that we should naturally keep an eye out for any other mistakes in the dataset:


```r
error_indices = which(netflix_data$rating == "84 min" | netflix_data$rating == "74 min" | netflix_data$rating == "66 min")
```

```
## Error in which(netflix_data$rating == "84 min" | netflix_data$rating == : object 'netflix_data' not found
```

```r
netflix_data[error_indices, c("duration", "rating")] = netflix_data[error_indices, c("rating", "duration")]
```

```
## Error in eval(expr, envir, enclos): object 'netflix_data' not found
```

```r
netflix_data[error_indices,]
```

```
## Error in eval(expr, envir, enclos): object 'netflix_data' not found
```

