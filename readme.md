# the Scope
automate the process of data gathering and organization prior to Machine Learning with easy to use snippets.
***
<details markdown="1">
<summary><h2> rename_snippet.py</h2></summary>
<br>
 <h3>guidelines</h3>
 
 place the snippet in the same folder as your *train* AND/OR *val* folders.
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
<details>
 <summary><h3> stats </h3></summary>
 
**Time Complexity**: $`\Theta(n)`$ for $`n =`$  elements in the folder \
**Space Complexity**: $`\Theta(1)`$ \
Parallelism **not yet** implemented 

</details>
<details>
 <summary><h3>possible bugs scenarios</h3></summary>
 
 Interrupting the process early. Partially processed files can be found in a temporary folder.

</details>
<br>
<br>

</details>

