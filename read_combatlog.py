def pre_process_file(filename):
    with open(filename) as infile:
        with open(filename + "a", "w+") as outfile:
            for zeile in infile:
                outfile.write(zeile.replace(" ", ",", 2).replace(" ", "", 1))
