##transmedia
*utilities for thumbing one's nose at intellectual property law (or not)*

___

### What is **transmedia**?

**transmedia** is a collection of utilities for converting images to audio, and vice versa. I wrote it to make light of perceived absurdities in intellectual property law. It's written to Python 3; 2.x will fail.

![Example PNG output](https://raw.githubusercontent.com/jonnystorm/transmedia/master/examples/sine.png)

At the moment, there is only one script: ```transform_png.py```. This turns files into pretty pictures (sort of) or vice versa. Of course, turning arbitrary PNG images into noise is likewise feasible, though the resulting file may not convert back to PNG the way you anticipate (yet).

    usage: transform_png.py [-h] -i INPUT -o OUTPUT

    Transform bytes into PNG or vice versa

    optional arguments:
      -h, --help            show this help message and exit
      -i INPUT, --input INPUT
                            input data file
      -o OUTPUT, --output OUTPUT
                            output PNG file


### Installation

**transmedia** is in the Cheese Shop: ```pip install transmedia```
