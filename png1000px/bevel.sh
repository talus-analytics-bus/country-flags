for f in *.png
do convert $f -raise 30 shiny/$f
done
