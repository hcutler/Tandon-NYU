# Tandon-NYU

Simple scraper for Tandon School of Engineering at NYU faculty index.
The index is 27 pages long, and this scraper stores all of the contents on all 27 pages to a
local HTML file ("tandon-nyu-pagecontents.html").

The scraper parses the page contents and pulls the names of all faculty members listed in the Index.
I've run the script, and copied the list of faculty names to a text file "tandon-people.txt".

You will see from looking at the website (http://engineering.nyu.edu/people) that each faculty name is accompanied
by an image. If you click the image, it links to a homepage for that faculty member which lists their research interests,
education, etc.

This script I have written can be modified (specifically, Lines 35-42) that in addition to names of the faculty members, you can pull
the link associated with them and information listed on the homepage of a faculty member. 
