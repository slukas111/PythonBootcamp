#this is the homework test for tuple understanding

technological_terms = ("python","python IDE", "tuple", "collection", "string")
tt = technological_terms
print(f"""we are ninja developers. We write {tt[0]} in {tt[-4]} and now practicing
 {tt[2]} {tt[3]} topicm that contains {tt[-1]} variables""")


tt = list(tt)
print(type(tt))

tt.append("float")
tt.append("list")

print(tt)
tt = tuple(tt)

print(f"new add on with tuple work aroundL: {tt}")