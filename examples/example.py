#!/bin/python3

# import the necessary modules
import json
import json4tree from json4tree

# import your JSON data
infile = open("input.json", "r")
json_file = json.load(infile)
infile.close()

# create a new handler
handler = json4tree(json_file)

# You can either print your results...
handler.results

# Or you can save your results
outfile = open("output.json", "w")
outfile.write(handler.results)
outfile.close()
