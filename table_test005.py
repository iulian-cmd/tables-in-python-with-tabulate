# import the tabulate here after install with pip
from tabulate import tabulate
import numpy as np
import pandas as pd

#  we have a dictionary of data
data = {
    "Name": [
        "Mr. Foo",
        "Mrs. Bar",
        "Mr. Baz",
        "Ms. Qux",
        "Mr. Quux",
        "Mrs. Corge",
        "Mr. Grault",
        "Mrs. Garply",
        "Mr. Waldo",
    ],
    "Age": ["32", "24", "19", "22", "23", "27", "34", "28", "56"],
    "Job": [
        "Engineer",
        "Doctor",
        "Clerk",
        "Manager",
        "Salesman",
        "Programmer",
        "Retired",
        "Retired",
        "Retired",
    ],
}

columns = ["COL1", "COL2", "COL3"]
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Table data with numpy: ")
print(tabulate(arr, headers=columns, tablefmt="fancy_grid", showindex="always"))


df = pd.DataFrame(data)

print("Table data with panda: ")
print(tabulate(df, headers="keys", tablefmt="fancy_grid", showindex="always"))
