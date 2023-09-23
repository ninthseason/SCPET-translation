import json


filename = "SChinese_trans.json"
savename = "SChinese_trans_utf8.json"

with open(filename, "r", encoding="utf-8") as f:
    jsontype = json.load(f)
    with open(savename, "w", encoding="utf-8") as sf:
        json.dump(jsontype, sf, ensure_ascii=False)

