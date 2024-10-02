# Arts

### Starting a QRNG website.
~~~
python run.py
~~~

### Getting random numbers from the website.
1. Generate a random number between 1 and 10000
2. Type: "string",
         "int",
         "binary",
         "octal",
         "hexadecimal",
   default "string"
~~~
import requests
res = requests.post('http://127.0.0.1:8080/Generate', json={"Type": "hexadecimal"})
~~~
