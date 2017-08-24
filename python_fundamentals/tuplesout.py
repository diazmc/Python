my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def tup(a):

    b = [(k,v) for k,v in a.items()] 

    return b

print tup(my_dict)