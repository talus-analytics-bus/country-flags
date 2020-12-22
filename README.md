# country-flags 🇩🇪

This is an internal Talus repository of country flags. Adapted from Hampus Nilsson's svg-country-flags package: https://github.com/hjnilsson/country-flags.

## Using the flags

To access the flag images that are hosted by Talus on AWS, use this form of URL:

`https://flags.talusanalytics.com/{STYLE}{SIZE}/{ISO}.png`

### Options

Available sizes are:

- 32px
- 64px
- 100px
- 300px
- 1000px

Available styles are flat (normal) or shiny (gives flags a more distinctive border, helpful sometimes in preventing flags blending into the background).

- flat: simply ignore `{STYLE}` paramter — flat is default. For example: `https://flags.talusanalytics.com/64px/us.png`
- shiny: add `shiny_` prefix for the `{STYLE}` parameter. For example: `https://flags.talusanalytics.com/shiny_64px/us.png`

### Examples:

- Shiny France (FR) flag at 300px resolution: `https://flags.talusanalytics.com/shiny_300px/fr.png`
- Flat Australia (AU) flag at 100px resolution: `https://flags.talusanalytics.com/100px/au.png`

## Advanced: Generating flag images

By running `resize.py` from the `scripts` directory, you can generate a set of square image flags at any resolution at or below 1000px. The flags will maintain their aspect ratio, but the images themselves will be square at a consistent size for easier implementation.

Note: The `resize.py` script will automatically use the 1000px source image pngs (located in `png1000px` directory) to generate the resized flag images, but this can be changed manually where `sourceDir` is defined in the script.

### Instructions:

- Navigate to `scripts` in this repo
- Install Pillow with `python3 -m pip install --upgrade Pillow`
- Run the script from `scripts` directory: `python resize.py {desired image dimension, in pixels}`. For example: `python resize.py 64` will resize into 64px by 64px squares
- Generated images can be found in `scripts/exports/{pixels}px`, where `{pixels}` was the number of pixels you used to run the command

### Notes & Troubleshooting:

#### Switch between shiny and flat flag generation
By default, the script will generate flat (normal) flag images. To switch between generating shiny and flat flags, change the source image folder in line 46 of `resize.py` to be either `png1000px` (flat) or `shiny1000px` (shiny). Then, change the export folder prefix appropriately in lines 52, 53, and 60 (either add or remove `shiny_` in the export folder name).

#### Troubleshooting
If you receive the "ModuleNotFoundError: No module named 'PIL'" error after installing pillow, you may have multiple python versions competing. Try `python3 resize.py 64` instead of `python resize.py 64`, for example.

#### Other Useful Info
- The ImageMagick commands used to create the shiny pngs from the flat pngs can be found in `png1000px` dir. `bevel.sh` bevels the images, and `shiny/shadow.sh` is used to give the beveled images a shadow.
- If generating new shiny images, it's a good idea to check the generated `np.png` image for Nepal, since Nepal's flag has a unique shape. Minimal editing may be required to eliminate any artifacts from the beveling/shadowing process.
