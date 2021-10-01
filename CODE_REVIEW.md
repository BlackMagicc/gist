# CODE REVIEW

## Which coding challenge did you review

Python

## Feedback
ln 8: 'from db import Pool' -> Not sure which library this is, couldn't find in db
ln 41: 'max_lifespan = 60 * 60 * 4' -> This variable isn't used
ln 44: query_contains function ->
    Could be more verbose/worded better,
    Not sure if function intends to return true if query contains every letter or word in words
    NOTE: If words only contains one word then this function just checks for every letter
ln 58: kill_query_on function ->
    'expirey' parameter not used
lns 64: 'cleaned = clean_query(query)'
lns 65: 'if query_contains(clean_query(query)' -> Repetitive, should use cleaned variable here 
ln 79: 'Thread.__init__(self)' -> Repetitive - adds nothing to the code
ln 82: 'while loop' -> There doesn't seem to be a breaking condition for this while loop
ln 103: guard function -> Same name as class and variable, could use different variable names for easier readability

In the future, I would like for this person to be more verbose and clear
on their intentions in the code