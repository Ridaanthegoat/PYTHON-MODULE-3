def test(Ridaan):
  result={}
  for i in Ridaan:
    result[i[0]]= i[1:]
    return result


studentlist=[[1,"ridaan","8","27"],[2,"samrath","8","30"],[3,"miheet","8","21"],[4,"manan","8","21"],[5,"adin","8","1"]]
print(studentlist)
print(test(studentlist))