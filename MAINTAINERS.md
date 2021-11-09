# To update the colormaps

- Download latest version from Zenodo
https://zenodo.org/record/4491293

- From directory above the colormaps master folder, create a new directrory called cmaps and do some Bash magic to extract colormap .txt files

`find . -name '*.txt' -exec cp {} ./cmaps \;`

- Remove the discrete colormaps (those with numbers at the end)

- Paste colormaps to the cmaps directory in cmcrameri

- Run the `show_cmaps`function and save the figure in the home directory of the project
