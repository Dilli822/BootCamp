

  #identifiers in python
  -name which is used to give to variables,function,classes , modules, objects in python
  -they case Sensitive
  -for example
  a = 5
  A = 10
  print(a + A) //15
  both a and A are different variables

  Rules of identifiers:
  --cannot start with number
  --can be declared with letters & digits
  --specail characters cannnot be used as identifiers like @,$

  #Check identifier
   >>import keyword
  >>> keyword.iskeyword("name")

  import.keyword
  >>>keyword.iskeyword("def")

  >>> "name".isidentifier()
  true
