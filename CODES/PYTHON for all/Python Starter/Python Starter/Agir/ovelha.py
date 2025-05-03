ovelha=[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

def count_sheeps():
    ove=[i for i in ovelha if i==True]
    return print(len(ove))
count_sheeps()