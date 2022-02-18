# import the tabulate here after install with pip
from tabulate import tabulate
from bs4 import BeautifulSoup
from html.parser import HTMLParser

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)


parser = MyHTMLParser()


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

# try to insert the output html format into an html file with Beautiful Soup
soup = BeautifulSoup(
    open("index.html"),
    "html.parser",  # html parser
    from_encoding=("utf-8", "iso-8859-1"),  # encoding
    # from_encoding="utf-8"  # encoding
    # from_encoding="iso-8859-1",  # encoding
)

# from bs4.diagnose import diagnose

# with open("bad.html") as fp:
#     data = fp.read()
# diagnose(data)


def display_content():
    return parser.feed(tabulate(
        table_data,
        headers="firstrow",
        tablefmt="html",
        showindex="always",
        numalign="left",
        stralign="left",)
    )


new_div = soup.new_tag("div")
new_div["class"] = "table-responsive container"
# new_div.append(display_content())
# soup.new_div.append(display_content())

with open("index.html", "w") as file:
    file.write(str(soup.append(parser)))
