Usage

Download the DEM file
Download korkeusmalliL3342CDEF.tif from the National Land Survey of Finland File Service:

https://asiointi.maanmittauslaitos.fi/karttapaikka/tiedostopalvelu/korkeusvyohykkeet?lang=fi
.

Insert the file into the input folder
Place the downloaded file into:

aineiston_kasittely/input_data/korkeusmalliL3342CDEF.tif


Run the model script
Execute the following command in the project root:

python src/gem.py

Optional: Use other locations
If you want to build a model from another location, download a TEK file from GTK soil investigation database:
https://gtkdata.gtk.fi/pohjatutkimukset/index.html
 or from your own site’s Geotechnical investigator.

Note: In this case, you may also need to download a new DEM file for the corresponding area.
