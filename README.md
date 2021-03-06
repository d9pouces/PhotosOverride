PhotosOverride
==============

Analyse Apple's Photos database and add keywords to some pictures: 
- pictures that are larger than a threshold,
- pictures that are smaller than a threshold,
- pictures that have been added multiple times,
- pictures of which the original is missing from disk.

You must create the used keywords in Apple Photos and create smart folders to display pictures these keywords.


```bash
poetry run python -m photosoverride examine --library ~/Pictures//Photos\ Library.photoslibrary/ 
  --original-keyword "original"  # Keyword to add to the first of duplicate pictures.
  --duplicate-keyword "duplicates"  # Keyword to add to duplicate pictures.
  --missing-keyword "missing"  # Keyword to add to missing pictures.
  --clean-keywords  # Remove all used keywords from pictures 
  --small-size 100000  # Max size of small pictures (in bytes).
  --large-size 50000000  # Min size of large pictures (in bytes).
  --small-keyword "small"  # Keyword to add to small pictures.
  --large-keyword "large"  # Keyword to add to large pictures.
``` 

Examples
--------

Remove the "Large" from all pictures, and add it to all pictures of at least 100 MB:
```bash
poetry run python -m photosoverride examine --clean-keywords --large-size 100000000 --large-keyword "Large"
``` 

Find all duplicate pictures, add the "Original" keyword to the first copy and the "Duplicate" keyword to other copies: 
```bash
poetry run python -m photosoverride examine --original-keyword "Original" --duplicate-keyword "Duplicate"
``` 
