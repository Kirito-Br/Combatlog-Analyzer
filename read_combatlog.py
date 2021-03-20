def pre_process_file(filename):
    with open(filename) as infile:
        with open(filename + "a", "w+") as outfile:
            for zeile in infile:
                outfile.write(zeile.replace(" ", ",", 2).replace(" ", "", 1))


parameter_name_list = [
    "date",
    "time",
    "event",
    "player_id",
    "playername_server",
    "sourceflag",
    "sourceraidflag",
    "target",
    "targetname",
    "destenationflag",
    "destenationraidflag",
    "actionsparameter1",
    "spellname",
    "spellschool",
    "missType",
    "blocked",
    "absorbed",
]
