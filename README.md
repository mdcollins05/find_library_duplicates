# find_library_duplicates

Uses standard Python libraries to find duplicate TV episodes or movie files. For whatever reason, I occasionally end up with more than one video file for a given TV show or Movie, so this helps discover those files across all of my library.

Works without any additional dependencies in Python >= 2.7 and >= 3.2. Otherwise, `argparse` is needed on the system for older Python versions.

## Usage

Simply run the script with one or more paths to your libraries. The paths need to include either "TV" or "Movie" in them for the script to operate correctly.

```
$ python ./find_library_duplicates.py "/media/TV" "/media/Movies"
```

It'll print a list of any movies or TV shows that have a duplicate mkv file. If none are found, there's no output.

