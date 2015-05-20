# Weleber-Tobler Algorithm for Kinetic Visual Fields

(I need to finish an introduction. Read paper in `misc`.)

## Usage

	from weleber_tobler import KineticField
	
	k = KineticField()
	k.isopter_points = [(54.7, 1.0), (51, 14.9), ... ]
	k.steradians
	k.percent_of_sphere

## Issues

No idea why the computed steradians are "close enough" but don't match those in the paper for the given input sets (see `test/test_kineticfield.py`). The equation used _seems_ right (see `misc/equation.html`). 

## References

* Here's [a nice introduction](http://www.jomtonline.com/jomt/articles/volumes/2/2/VisualFields.pdf) to Visual Fields.
* Used [Chipmunk Basic](http://www.nicholson.com/rhn/basic/) for the original code.
* Used [this manual](http://www.antonis.de/qbebooks/gwbasman/) as reference for GW-BASIC.

This line means "go to line 400"; it doesn't reassign the array value (d'oh...):

    IF RD(I)<90 THEN 400

This means "use double-precision":

    RD(I)=90#

Not sure what this means. Assuming it's "greater than or equal to":

    IF T(K)=>T(I) 

## License

[MIT](https://raw.githubusercontent.com/afreeorange/mit-license/master/LICENSE)
