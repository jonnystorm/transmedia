##transmedia
*utilities for thumbing one's nose at intellectual property law (or not)*

___

**transmedia** is a collection of utilities for converting images to audio, and vice versa. I wrote it to make light of perceived absurdities in intellectual property law.

![Example PNG output](http://github.com/jonnystorm/transmedia/sine.png)

At the moment, there are only two real scripts: ```pcm2png.py``` and ```png2pcm.py```. The first turns PCM audio files (raw, signed 16-bit, little-endian) into pretty pictures (sort of). The second turns those same pictures back into the original PCM audio. Of course, turning arbitrary PNG images into audio is likewise feasible, though the resulting audio may not convert back to PNG the way you anticipate (yet).

```usage: pcm2png.py [-h] -i INPUT -o OUTPUT [-d BYTE_DEPTH]

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
```
