# librum-apertum
The goal of this is to host a static API on GitHub pages by storing endpoints in files. Here each possible valid GET request is stored in some HTML file. The static API is demonstrated using verses from the KJV Bible (plus deuterocanonical books) as responses. What makes this work neatly is the fact that you can omit the `.html` extension on GitHub Pages and still reach the same pages, giving the illusion of a normal API. To maintain this illusion while returning JSON objects, I imagine you'd just need to put only the raw JSON in the `.html` file rather than use a `.json` 

Here's an example of a request and the response it gives:
```bash
$ curl https://jackdonofrio.github.io/librum-apertum/kjv/John/3/16
"For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life."
```


Todo:
- fix deuterocanonical book titles in kjv
- add rest of deuterocanon to vulgate

(Note: this was originally uploaded on my other account, pyr0m4nc3r.)
