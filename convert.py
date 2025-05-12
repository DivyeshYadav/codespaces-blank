s_name =[1,"Riyaan Yadav","V"],[2,"Manyata Rai","V"],[3,"Divyesh Yadav","V"],[4,"Priyanshu Urnaw","V"],[5,"Aayan Magar","V"]
def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result

print("List: ",s_name)
print("Dictionary: ",test(s_name))