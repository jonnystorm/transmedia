##transmedia
*utilities for thumbing one's nose at intellectual property law (or not)*

___

### What is **transmedia**?

**transmedia** is a collection of utilities for converting images to audio, and vice versa. I wrote it to make light of perceived absurdities in intellectual property law. It's written to Python 3; 2.x will fail.

![Example PNG output](https://raw.githubusercontent.com/jonnystorm/transmedia/master/examples/sine.png)

At the moment, there are only two real scripts: ```bytes2png.py``` and ```png2bytes.py```. The first turns any file into a pretty picture (sort of). The second turns those same pictures back into the original file. Of course, turning arbitrary PNG images into noise is likewise feasible, though the resulting file may not convert back to PNG the way you anticipate (yet).

    usage: bytes2png.py [-h] -i INPUT -o OUTPUT [-d BYTE_DEPTH]

    Transform bytes into PNG

    optional arguments:
      -h, --help            show this help message and exit
      -i INPUT, --input INPUT
                            input data file
      -o OUTPUT, --output OUTPUT
                            output PNG file
      -d BYTE_DEPTH, --byte-depth BYTE_DEPTH
                            bytes per pixel (default: 2)

    
    usage: png2bytes.py [-h] -i INPUT -o OUTPUT

    Transform PNG into bytes

    optional arguments:
      -h, --help            show this help message and exit
      -i INPUT, --input INPUT
                            input PNG file
      -o OUTPUT, --output OUTPUT
                            output data file

### Installation

**transmedia** is in the Cheese Shop: ```pip install transmedia```
