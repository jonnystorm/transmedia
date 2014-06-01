##transmedia
*utilities for thumbing one's nose at intellectual property law (or not)*

___

### What is **transmedia**?

**transmedia** is a collection of utilities for converting images to audio, and vice versa. I wrote it to make light of perceived absurdities in intellectual property law. It's written to Python 3; 2.x will fail.

![Example PNG output](https://raw.githubusercontent.com/jonnystorm/transmedia/master/examples/sine.png)

At the moment, there are only two real scripts: ```pcm2png.py``` and ```png2pcm.py```. The first turns PCM audio files (raw, signed 16-bit, little-endian) into pretty pictures (sort of). The second turns those same pictures back into the original PCM audio. Of course, turning arbitrary PNG images into audio is likewise feasible, though the resulting audio may not convert back to PNG the way you anticipate (yet).

    usage: pcm2png.py [-h] -i INPUT -o OUTPUT [-d BYTE_DEPTH]

    Transform PCM to PNG

    optional arguments:
      -h, --help            show this help message and exit
      -i INPUT, --input INPUT
                            input PCM file
      -o OUTPUT, --output OUTPUT
                            output PNG file
      -d BYTE_DEPTH, --byte-depth BYTE_DEPTH
                            bytes per sample (default: 2)

    
    usage: png2pcm.py [-h] -i INPUT -o OUTPUT

    Transform PNG to PCM

    optional arguments:
      -h, --help            show this help message and exit
      -i INPUT, --input INPUT
                            input PNG file
      -o OUTPUT, --output OUTPUT
                            output PCM file

### Installation

**transmedia** is in the Cheese Shop: ```pip install transmedia```
