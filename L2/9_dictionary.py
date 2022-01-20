dict = {"object":"book", "stuff" : "bed", "vehicle": "bus"}
dict["object"] = "column"
# del dict["stuff"] // if key exists - otherwise an error...
dict.pop("unknown", None)
# dict.pop("stuff", None)
add_dict  = {"added":"added_val"}
dict.update(add_dict)
print(dict.keys())
print(dict.values())
