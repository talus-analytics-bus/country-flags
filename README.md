# country-flags

This is an internal Talus repository of country flags. Adapted from Hampus Nilsson's svg-country-flags package: https://github.com/hjnilsson/country-flags.

## Generating square flag images

By running `resize.py` from the `scripts` directory, you can generate a set of square image flags at any resolution at or below 1000px. The flags will maintain their aspect ratio, but the images themselves will be square at a consistent size for easier implementation.

Note: The `resize.py` script will automatically use the 1000px source image pngs (located in `png1000px` directory) to generate the resized flag images, but this can be changed manually where `sourceDir` is defined in the script.

_Instructions:_

- Navigate to `scripts` in this repo
- Install Pillow with `python3 -m pip install --upgrade Pillow`
- Run the script from `scripts` directory: `python resize.py {desired image dimension, in pixels}`. For example: `python resize.py 64` will resize into 64px by 64px squares
- Generated images can be found in `scripts/exports/{pixels}px`, where `{pixels}` was the number of pixels you used to run the command
