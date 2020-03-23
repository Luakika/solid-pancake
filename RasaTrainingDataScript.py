# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 10:03:03 2019

@author: candice.l.penelton
"""

from RasaCSVtoJSON import RasaCsvToJson
from RasaJSONtoCSV import RasaJsonToCsv
import sys

# Select input and output directories
input_dir = sys.argv[1]
output_dir = sys.argv[2]

bot_name = sys.argv[3]

# Generate json data
trainingjson = RasaCsvToJson(input_dir)
training_data = trainingjson.get_common_examples()

# Save data    
trainingjson.save_json(training_data,output_dir)

# Save case sensitive training data for reference if included
if len(sys.argv) == 5:
    bot_name = sys.argv[3]
    csv_dir = sys.argv[4]
    csv_saver = RasaJsonToCsv(output_dir)
    json_data = csv_saver.get_json_data()
    intents, entities = csv_saver.get_common_examples(json_data)
    csv_name = bot_name + "_lowercase_training_data"
    csv_saver.save_intents_csv(intents, csv_name, csv_dir)
    if len(entities) > 0:
        csv_saver.save_entities_csv(entities, csv_name, csv_dir)