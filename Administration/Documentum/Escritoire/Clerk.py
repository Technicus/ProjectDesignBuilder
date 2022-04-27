
import json

# Data to be written
file_data = {
    "filename" :
        "headder" : {
            "Interpreter" : "#!/bin/python",
            "Coding" : "# utf-8",
            "Date" : "",
            "Version" : "__version__",
            "Release" : "__release__"
        },
        "footer" : {
            "Author" : "Technicus",
            "Copyright" : "Copyright (C) 2022",
            "Credits" : "Associates",
            "License" : "GNU GENERAL PUBLIC LICENSE Version 3",
            "Project" : "ProjectDesignBuilder"
        },
        "Description" : {
            "Description" : "",
            "Theory" : "",
            "Implementation" : "",
            "Development" : ""
        }
}

# Serializing json
#headder = json.dumps(headder, indent = 4)
#footer = json.dumps(footer, indent = 4)
file_data = json.dumps(file_data, indent = 4)

# Writing to sample.json
with open("FileReport.json", "w") as outfile:
    outfile.write(file_data)




