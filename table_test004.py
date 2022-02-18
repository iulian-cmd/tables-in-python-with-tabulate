# import the tabulate here after install with pip
from tabulate import tabulate

# basic table list
table_data = [
    ["Name", "Age", "Job", "Pay", "City"],
    ["Mr. Foo", "32", "Engineer", "$40,000", "New York"],
    ["Mrs. Bar", "24", "Doctor", "$30,000", "San Francisco"],
    ["Mr. Baz", "19", "Clerk", "$20,000", "London"],
    ["Ms. Qux", "22", "Manager", "$50,000", "Paris"],
    ["Mr. Quux", "23", "Salesman", "$30,000", "New York"],
    ["Mrs. Corge", "27", "Programmer", "$20,000", "San Francisco"],
    ["Mr. Grault", "34", "Retired", "$50,000", "London"],
    ["Mrs. Garply", "28", "Retired", "$40,000", "Paris"],
    ["Mr. Waldo", "56", "Retired", "$30,000", "New York"],
]

# display data into a html file
with open("mytable.html", "w") as f:
    f.write(
        tabulate(table_data, headers="firstrow", tablefmt="html", showindex="always")
    )
