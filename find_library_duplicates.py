import os
import argparse
import re


def check_duplicates(library):
    if not os.path.exists(library):
        print(f"Library '{library}' does not exist.")
        return

    if "TV" in library:
        search_pattern = r"^.*([0-9]{4}-[0-9]{2}-[0-9]{2}|S[0-9]{2,4}E[0-9]{2,3})"
        for show in sorted(os.listdir(library)):
            show_path = os.path.join(library, show)
            if os.path.isdir(show_path):
                # print(f"Processing show: {show}")
                for season in sorted(os.listdir(show_path)):
                    season_path = os.path.join(show_path, season)
                    if os.path.isdir(season_path):
                        # print(f"  Processing season: {season}")
                        duplicates = set()
                        file_count = {}
                        for root, dirs, files in os.walk(season_path):
                            files.sort()
                            for file in files:
                                if re.match(search_pattern, file) and file.endswith(
                                    ".mkv"
                                ):
                                    filename = re.match(search_pattern, file).group(0)
                                    file_count[filename] = (
                                        file_count.get(filename, 0) + 1
                                    )
                                    if file_count[filename] >= 2:
                                        duplicates.add(filename)
                        if duplicates:
                            print(f"Duplicate episodes found in {season_path}:")
                            print("\n".join("  " + item for item in sorted(duplicates)))
    elif "Movie" in library:
        for movie in sorted(os.listdir(library)):
            movie_path = os.path.join(library, movie)
            if os.path.isdir(movie_path):
                # print(f"Processing movie: {movie}")
                duplicates = set()
                file_count = {}
                for root, dirs, files in os.walk(movie_path):
                    files.sort()
                    for file in files:
                        if file.endswith(".mkv"):
                            file_count[file] = file_count.get(file, 0) + 1
                            if file_count[file] >= 2:
                                duplicates.add(file)
                if duplicates:
                    print(f"Duplicate movies found in {library}:")
                    print("\n".join("  " + item for item in sorted(duplicates)))


def main():
    parser = argparse.ArgumentParser(
        description="Check for duplicate movies or TV episodes in libraries."
    )
    parser.add_argument(
        "libraries",
        metavar="LIBRARY",
        type=str,
        nargs="+",
        help="libraries to check for duplicates",
    )
    args = parser.parse_args()

    for library in args.libraries:
        check_duplicates(library)


if __name__ == "__main__":
    main()
