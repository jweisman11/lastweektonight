# lastweektonight
Analysis of episodes from HBO's Last Week Tonight with John Oliver

### Objective
* Identify which cuss words are used in episodes of LWT
* Determine if there is a correlation between episode popularity (US views) and cuss word usage

### Approach
* Create a listing of common cuss words
* Scrape episode listing from Wikipedia - https://en.wikipedia.org/wiki/List_of_Last_Week_Tonight_with_John_Oliver_episodes
* Identify corresponding videos from LWT's YouTube channel (only focusing on "Main Segments")
* Collect URL and video info from each identified YouTube video
* Merge the Wikipedia and YouTube data
* Convert the YouTube video to text using AWS's Transcribe
* Identify cuss words used in LWT epsidoes
* Test correlation between cuss words 

### Cloud Dependencies
* Using GCP's YouTube API which requires creating key
* Using personal AWS account for transcriptions via Transcribe

### Notes
* Episode data on Wikipedia includes a count of US viewers, but I'm assuming this is for the original airing on HBO and does not include subsequent views from YouTube. Will be adding this two view counts together to get an accurate estimate of total viewership
* The first episode from LWT (Season 1, Episode 1) does not apepar on YouTube

### Comparing dates: Wikipedia vs YouTube
Episodes of HBO's LastWeekTonight air on Sundays. I confirmed all episode's air dates on Wikipedia were Sunday.

The corresponding video for the main segment on YouTube doesn't appear until Monday. LWT also publishes other content to their YouTube channel like web exclusives, special segments like "how is this still a thing" official trailers and extended interviews. I want to exclude this additional content since I'm only focused on main segments.

