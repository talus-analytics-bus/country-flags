for f in *.png
do convert $f \( +clone -background black -shadow 80x20+0+15 \) +swap -background transparent -layers merge +repage shadow/$f
done