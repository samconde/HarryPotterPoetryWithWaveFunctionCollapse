# HarryPotterPoetryWithWaveFunctionCollapse
Generating Harry Potter poetry using the Wave function collapse algorithm. This project was adapted from mewo2's oisin repo (https://github.com/mewo2/oisin)


# Group Members
Samantha Conde and Alison Crosby

# Example Output Code
Here's an example of two stanzas generated from Wave Function Collapse algorithm (with Harry Potter Book 1)

*Sentences 201-300: stanza 2
He never have. You flatter me
Said Dumbledore. And I don t
Suppose you re the only one
You know who. Harry Potter come
And live here. All this you know who.
You can t. It s it s true.
That s not all. Of all the way.
I ve been watching them all day.*

*Sentences 301-450: stanza 3
I ve got him sir. It had been
A good one. She can t take him.
His Aunt rapped on the. All right then.
His Aunt rapped on the door again.
Is that all right. Are you up yet.
When he was gone. What did you get
That motorcycle. Comb your hair.
Yet Harry knew he. Is that where.*

# Instructions on how to run code
Pull github repo and ensure you have python 3 installed.

Run on terminal (perferably with ananconda with a python 3 environment):
Install two python libraries: 
```sh
pip install pronouncing
pip install pillow
```

Then to generate poems, update the filename variable to the desired text file and run
```sh
python ballad.py
```

To generate gifs, update the filename variable to the desired text file and run
```sh
python makegif.py
```


# Rules/Constraints used
There are 4 changes you can make to ballad.py
- filename (change the path of the text file you want to use to generate poems)
- meter (used to change the iambic pentameter by metrical feet and rhythm)
- step (how many times WFC should propogate)
- order (changes how many states deep it will use WFC)

```sh
filename = "input/hpbook1.txt"
...
meter=oisin.iambic(4, 'aabbccdd'),
    step=50,
    order=3
```

# Process for creating output
- See intructions for how to run code
	- ballad.py generates poems in the terminal
	- makegif.py generates a gif of the poem generation in the output folder


