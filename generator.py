# outputs a series of commands which, when run, upscale all the images in the source directory
# to make a .cmd file with these commands: "python generator.py > upscaler.cmd"
# as written, the destination directories are wiped and recreated each time. be careful.

import os
import fnmatch

imgexe = 'ImageResizer-r129.exe'
sourcedir = '.\\orig16by16'
filefilter = '*.png'

# transforms are { 'algorithm': 'destination directory name' }
transforms = { 'XBR 2x': 'x2', 'XBR 3x': 'x3', 'XBR 4x': 'x4' }

for algo, destroot in transforms.items():
    print('rmdir /s /q ' + destroot)
    for root, dir, files in os.walk(sourcedir):
        destdir = destroot + root.replace(sourcedir, '')
        print('mkdir .\\' + destdir)
        for items in fnmatch.filter(files, filefilter):
            source = root + '\\' + items
            print(imgexe + ' /load ' + source + ' /resize auto "' + algo + '" /save .\\' + destdir + '\\' + items)

