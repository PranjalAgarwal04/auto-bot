query = input("> ")
query = query.lower()

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
         1.Source location one
         2.Source location two
         3.Source location three
         4.Refresh options""")
        query = input("> ")

        for x in query:
            if (x == "1"):
                print("Source loaction one")
                break
            elif (x == "2"):
                print("Source location two")
                break
            elif (x == "3"):
                print("Source location three")
                break
            elif (x == "4"):
                print("""
                    1-Source location four
                    2-Source location five
                    3-Source location six
               """)
            query = input("> ")
        print("Looking for the nearest auto driver...")
        print("""
                  Auto Located -
                  Driver name -
                  Auto number -
                  Contact number -
                  """)
