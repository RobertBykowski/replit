def szescian(x):
  return x*x*x

def main():
  liczby = list (map(szescian, range(1,15)))
  print(liczby)
main()

  
  