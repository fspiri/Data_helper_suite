# the scope
automate the process of data gathering and organization prior to Machine Learning with easy to use snippets.
***
## rename_snippet.py
this snippet renames and reformats all the files inside a folder.
### guidelines
place the snippet in the same folder as your *train* and/or *val* folders.
 ```
               ┌ rename_snippet.py
img_dataset ──┼ train ─┬ cats
               │        ├ lamas
               │        ╎
               │
               └ val ─┬ cats
                      ├ lamas
                      ╎
 ```
run with `python rename_snippet.py`   \
supported formats: `.jpg .jpeg .png` but easy to modify
### stats
Time Complexity: $`\Theta(n)`$ for $`n`$ = elements in the folder \
Space Complexity: $`\Theta(1)`$ \
Parallelism **not yet** implemented 
### possible bugs scenarios
Interrupting the process early. Partially processed files can be found in a temporary folder.

