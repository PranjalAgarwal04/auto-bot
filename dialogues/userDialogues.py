query = input("> ")
query = query.lower()
print(query)

if (query == "hello" or query == "hi" or query == "hey"):
    print("""Hello, do you want to book an auto?
      1.Book an auto
      2.Report
      3.Help""")
    query = input("> ")

    if (query == "1"):
        print("""Enter your current location.""")
        query = input("> ")

        print("""
         1.Source loaction one
         2.Source location two
         3.Source location two
         4.Refresh options""")
        query = input("> ")

        if (query == "1"):
            print()
