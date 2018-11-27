# Some hints to make your life easier
## Quirks in PsychoPy
PsychoPy is wonderful in some ways, but has some real weird quirks that aren't well documented.
### Capturing and playing sounds in PsychoPy
`psychopy.sound` is the sound module within PsychoPy. I find it buggy and hard to use, so I just use sounddevice and soundfile like we did in Session 5. Making this work with PsychoPy requires a specific set of import statements though, which I'll provide here so you don't have to waste time figuring it out yourself by trial and error:  
```
import sounddevice as sd
import soundfile as sf
from psychopy import prefs
prefs.general['audioLib'] = ['pygame']
from psychopy import core, visual, event  # and any other parts of psychopy you want to use
```
## Working with csv files
### csv or tsv?
Comma-separated values (or csv) files are a convenient way to store data. The data is stored as follows:
```
column name 1,column name 2,column name 3
row 1 value 1,row 1 value 2,row 1 value 3
row 2 value 1,row 2 value 2,row 2 value 3
row 3 value 1,row 3 value 3,row 3 value 3
```
The commas being used as delimiters makes it a compact file format (doesn't use a lot of disk space) and very easy to read. Quickly editing a column in a csv, however, can be a bit of a hassle. One convenient way to work on them is to open them in Excel, which should recognize the file format and open it as a spreadsheet. I say _should_ because Excel has the quirk that it uses a different csv file standard depending on your geographical location settings. This is terribly inconvenient, because it means that on my Dutch (or German) computer it will try to use semicolons (;) as delimiters for csv, while on an American collaborator's computer it would use commas. The files are then no longer readable once we send them to each other.  
Luckily, there is an easy solution: use tab-separated values instead of comma-separated values, because Excel handles tabs the same everywhere. Excel likes to store tab-separated values as `.txt` files (when saving a spreadsheet, select "tab-delimited text" as the format) but that's confusing because lots of files that are _not_ tab-separated values also use `.txt`. The better option is to use `.tsv`. This requires some small adaptations (Excel may not recognize the file extension, so you need to manually select Excel as the program to use when opening) but at least it's safe to send tsv files to the other side of the world!
### pandas or the csv module
When reading or writing tsv data in Python, you have two main options: the pandas module and the csv module. One is not necessarily better than the other, but depending on the situation you might prefer one to the other.
I myself like to use the csv module to write data when I collect it during an experiment, but prefer to use pandas for loading it when I'm going to analyze it. The tsv files they generate are exactly the same, so just use what happens to be convenient and don't worry about it.  
One thing you __do__ need to keep in mind is to specify `delimiter='\t'` when opening tsv files for reading or writing in both pandas and the csv module.
## Modular code
Please don't write your whole project in a single file. Instead, break the code up into functions that you can reuse or call in a loop, and store related functions in separate files that you can import as modules into your main project.  
It will be much easier to structure and understand your own code this way.
## Comments
__Use them!__  
(For our sake and yours.)
