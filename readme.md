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
<details markdown="1">
<summary><h2> image_scraper_snippet.py</h2></summary>
<br>
 <h3>guidelines</h3>
 
 place the snippet in the folder above your *train* AND/OR *val* folders.
 ```
                 ┌ image_scraper_snippet.py
──img_dataset ──┼ train ─┬ cats
                 │        ├ lamas
                 │        ╎
                 │
                 └ val ─┬ cats
                        ├ lamas
                        ╎
 ```
- **requirements**:
    - have Chrome installed on your system. Will be used as guest, no log-in needed.
    - have selenium installed. If not just run `pip install selenium`
- run with `python rename_snippet.py`.
- the snippet will create a `downloads` folder in which all the queries will be downloaded.  
- the downloaded images are small, adapt for machine learning.  
- don't forget to turn on variable size analysis in your model, as the images come in a range of sizes.  

<details>
 <summary><h3> stats </h3></summary>
 
**Time Complexity**: $<= 0.10 sec$ for $`image`$  - after the browser has been opened \
**Parallelism** implemented - Concurrent downloads

</details>
<details>
 <summary><h3>possible bugs scenarios</h3></summary>
 
 Most common bug: Chrome doesn't load properly / Loads with different settings. 
 - **implemented solution**: the program will try to re-open the browser for a max of 3 times. This solution doesn't always work.  
 - **user solution**: Be stubborn. Re-run the program until it works. Usually 2 re-run at max will do it.

</details>
<br>
<br>

</details>
