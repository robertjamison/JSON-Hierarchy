#!/bin/python3

# import the necessary modules
import json
import json4tree

# import your JSON data
infile = open("input.json", "r")
json_file = json.load(infile)
infile.close()

# create a new handler
converter = json4tree.handler(json_file)

# You can either print your results...
converter.results

# Or you can save your results
outfile = open("output.json", "w")
outfile.write(converter.results)
outfile.close()
