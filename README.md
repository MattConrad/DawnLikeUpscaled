There is an amazing tileset for roguelikes/fantasy RPGs called DawnLike, by the famous Dragon De Platino:

[https://opengameart.org/content/dawnlike-16x16-universal-rogue-like-tileset-v181]

The tiles are only 16x16 though, and that's pretty small for a lot of games.

This repo is the DawnLike tileset, upscaled to x2, x3, and x4 sizes. If you need one of these sizes, clone the repo and have fun. (Do remember to accredit DawnBringer as discussed in the link above, and include Platino somewhere in your project as an attribution, see link above and  \orig16by16\Characters\Reptile0.png).



More details for the curious, or if you want to make your own variations.

I poked at this a little, a long time ago, with ImageMagick, but the results were blurry and didn't look good. (ImageMagick may have gotten better at pixel art since then.)

At some point I found an obscure image resizer called ImageResizer by Hawkynt (Windows only, but see below) that supports lots of different algorithms for resizing images. Some of these work very nicely with pixel art:

[https://code.google.com/archive/p/2dimagefilter/wikis/ImageResizer.wiki]

The images here came from running the XBR algorithm over all of the original DawnLike pngs, using the included upscaler.cmd.

upscaler.cmd was created using generator.py. If you want to use a different algorithm, or adapt this for a different tileset, or whatever, you can use generator.py to make your own upscaler command list. (Running ImageResizer from the command line is kind of involved and fiddly, be warned.)

If you are Unixy and not Windowsy, you can check out:

[https://github.com/icebreaker/2dimagefilter]

which is a port of (some of) ImageResizer to Mono.



There's a neat /Examples folder in the original DawnLike set that shows a lot of animated gifs showing DawnLike in action. The example .gifs are not upscaled and won't be in the output directories. If you're new to DawnLike you should check out the originals, though!



Thanks to Dawnbringer, Dragon De Platino, and Hawkynt for making these excellent resources available freely.
