import json
import time

from Baidu_Text_transAPI import callapi

filename = "SChinese.json"
f = open(filename, "r")
data = json.load(f)
f.close()

category = ["menu", "item", "npc", "effects", "hints", "misc"]

for cate in category:
    for key in data[cate]:
        value = data[cate][key]
        if '%' in value:
            continue
        trans_value = callapi(value)["trans_result"]
        time.sleep(1)
        src = ""
        dst = ""
        for next, i in enumerate(trans_value):
            if next != 0:
                src += "\n"
                dst += "\n"
            src += i["src"]
            dst += i["dst"]
        print(src, ":", dst)
        data[cate][key] = dst


filename = "SChinese_trans.json"
f = open(filename, "w")
json.dump(data, f)
f.close()
