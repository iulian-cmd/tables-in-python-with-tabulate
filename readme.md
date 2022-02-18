# Pretty printing tables in Python

* install first
#### pip install virtualenv 

* go to project folder
#### cd projectfolder 

* Create a virtual environment named myenv
#### python -m venv ./myenv 

* (powershell) start the file  to start the environment
#### Activate.ps1 

* or (cmd) start the file  to start the environment
#### activate.bat 

-> if it worked you'll see a (myenv) in front of your cursor path 

* pip install the tabulate extension
#### pip install tabulate

* import the extension tabulate
#### from tabulate import tabulate

* install the black formatter
#### pip install black


==> table formats 
* tablefmt "psql"

```
+-------------+-------+------------+---------+---------------+
| Name        |   Age | Job        | Pay     | City          |
|-------------+-------+------------+---------+---------------|
| Mr. Foo     |    32 | Engineer   | $40,000 | New York      |
| Mrs. Bar    |    24 | Doctor     | $30,000 | San Francisco |
| Mr. Baz     |    19 | Clerk      | $20,000 | London        |
| Ms. Qux     |    22 | Manager    | $50,000 | Paris         |
| Mr. Quux    |    23 | Salesman   | $30,000 | New York      |
| Mrs. Corge  |    27 | Programmer | $20,000 | San Francisco |
| Mr. Grault  |    34 | Retired    | $50,000 | London        |
| Mrs. Garply |    28 | Retired    | $40,000 | Paris         |
| Mr. Waldo   |    56 | Retired    | $30,000 | New York      |
+-------------+-------+------------+---------+---------------+
```

* tablefmt="grid"

```
+-------------+-------+------------+---------+---------------+
| Name        |   Age | Job        | Pay     | City          |
+=============+=======+============+=========+===============+
| Mr. Foo     |    32 | Engineer   | $40,000 | New York      |
+-------------+-------+------------+---------+---------------+
| Mrs. Bar    |    24 | Doctor     | $30,000 | San Francisco |
+-------------+-------+------------+---------+---------------+
| Mr. Baz     |    19 | Clerk      | $20,000 | London        |
+-------------+-------+------------+---------+---------------+
| Ms. Qux     |    22 | Manager    | $50,000 | Paris         |
+-------------+-------+------------+---------+---------------+
| Mr. Quux    |    23 | Salesman   | $30,000 | New York      |
+-------------+-------+------------+---------+---------------+
| Mrs. Corge  |    27 | Programmer | $20,000 | San Francisco |
+-------------+-------+------------+---------+---------------+
| Mr. Grault  |    34 | Retired    | $50,000 | London        |
+-------------+-------+------------+---------+---------------+
| Mrs. Garply |    28 | Retired    | $40,000 | Paris         |
+-------------+-------+------------+---------+---------------+
| Mr. Waldo   |    56 | Retired    | $30,000 | New York      |
+-------------+-------+------------+---------+---------------+
```
* tablefmt="pipe"

```
| Name        |   Age | Job        | Pay     | City          |
|:------------|------:|:-----------|:--------|:--------------|
| Mr. Foo     |    32 | Engineer   | $40,000 | New York      |
| Mrs. Bar    |    24 | Doctor     | $30,000 | San Francisco |
| Mr. Baz     |    19 | Clerk      | $20,000 | London        |
| Ms. Qux     |    22 | Manager    | $50,000 | Paris         |
| Mr. Quux    |    23 | Salesman   | $30,000 | New York      |
| Mrs. Corge  |    27 | Programmer | $20,000 | San Francisco |
| Mr. Grault  |    34 | Retired    | $50,000 | London        |
| Mrs. Garply |    28 | Retired    | $40,000 | Paris         |
| Mr. Waldo   |    56 | Retired    | $30,000 | New York      |
```
* tablefmt="html"

```
<table>
<thead>
<tr><th style="text-align: right;">  </th><th>Name       </th><th style="text-align: right;">  Age</th><th>Job       </th><th>Pay    </th><th>City         </th></tr>
</thead>
<tbody>
<tr><td style="text-align: right;"> 0</td><td>Mr. Foo    </td><td style="text-align: right;">   32</td><td>Engineer  </td><td>$40,000</td><td>New York     </td></tr>
<tr><td style="text-align: right;"> 1</td><td>Mrs. Bar   </td><td style="text-align: right;">   24</td><td>Doctor    </td><td>$30,000</td><td>San Francisco</td></tr>
<tr><td style="text-align: right;"> 2</td><td>Mr. Baz    </td><td style="text-align: right;">   19</td><td>Clerk     </td><td>$20,000</td><td>London       </td></tr>
<tr><td style="text-align: right;"> 3</td><td>Ms. Qux    </td><td style="text-align: right;">   22</td><td>Manager   </td><td>$50,000</td><td>Paris        </td></tr>
<tr><td style="text-align: right;"> 4</td><td>Mr. Quux   </td><td style="text-align: right;">   23</td><td>Salesman  </td><td>$30,000</td><td>New York     </td></tr>
<tr><td style="text-align: right;"> 5</td><td>Mrs. Corge </td><td style="text-align: right;">   27</td><td>Programmer</td><td>$20,000</td><td>San Francisco</td></tr>
<tr><td style="text-align: right;"> 6</td><td>Mr. Grault </td><td style="text-align: right;">   34</td><td>Retired   </td><td>$50,000</td><td>London       </td></tr>
<tr><td style="text-align: right;"> 7</td><td>Mrs. Garply</td><td style="text-align: right;">   28</td><td>Retired   </td><td>$40,000</td><td>Paris        </td></tr>
<tr><td style="text-align: right;"> 8</td><td>Mr. Waldo  </td><td style="text-align: right;">   56</td><td>Retired   </td><td>$30,000</td><td>New York     </td></tr>
</tbody>
</table>
```

* showindex="always"  for having index 
#### showindex="always"  



