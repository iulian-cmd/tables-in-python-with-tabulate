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

# use tabulate to print nicer tables
print(tabulate(table_data, headers="firstrow", showindex="always"))
print(tabulate(table_data, headers="firstrow", tablefmt="psql", showindex="always"))
print(
    tabulate(table_data, headers="firstrow", tablefmt="fancy_grid", showindex="always")
)
print(tabulate(table_data, headers="firstrow", tablefmt="grid", showindex="always"))
print(tabulate(table_data, headers="firstrow", tablefmt="orgtbl", showindex="always"))
print(tabulate(table_data, headers="firstrow", tablefmt="rst", showindex="always"))
print(tabulate(table_data, headers="firstrow", tablefmt="latex", showindex="always"))
print(
    tabulate(table_data, headers="firstrow", tablefmt="latex_raw", showindex="always")
)
print(
    tabulate(
        table_data, headers="firstrow", tablefmt="latex_booktabs", showindex="always"
    )
)
print(tabulate(table_data, headers="firstrow", tablefmt="html", showindex="always"))
print(tabulate(table_data, headers="firstrow", tablefmt="html_raw", showindex="always"))
print(tabulate(table_data, headers="firstrow", tablefmt="simple", showindex="always"))
print(tabulate(table_data, headers="firstrow", tablefmt="plain", showindex="always"))
print(tabulate(table_data, headers="firstrow", tablefmt="plain", showindex="always"))
