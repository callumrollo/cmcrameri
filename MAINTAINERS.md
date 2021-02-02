# To update the colourmaps

- Download latest version from Zenodo
https://zenodo.org/record/4491293

- From directory above the colourmaps master folder, create a new directrory called cmaps and do some Bash magic to extract colormap .txt files

`find . -name '*.txt' -exec cp {} ./cmaps \;`

- Remove the discrete colourmaps (those with numbers at the end)

- Paste colourmaps to the cmaps directory in cmcrameri

- Run the `show_cmaps`function and save the figure in teh home directory of the project
