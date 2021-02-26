import os
import json, operator

with open('data.json', 'r', encoding='utf-8') as f:
  result_data = json.load(f)
  print(result_data)

#############

sort_surname = sorted(result_data, key = lambda x: x['name'].split()[-1])
print(sort_surname)

#############

for record in result_data:

    dates = (''.join(record['years'].split())).split("–")

    death = int(dates[1].replace(".", "").replace("c", "").replace("BC", ""))
    death = death * -1 if dates[1].find("BC") != -1 else death

    record["death"] = death


result_data.sort(key=lambda record: record["death"])
print(result_data, sep="\n")


###############


def sort_key_by_text(result_data):
    value = result_data["text"]
    return value


def sort_key_by_len_text(result_data):
    return len(result_data["text"])


result = sorted(result_data, key=sort_key_by_len_text)
print(result)