**refGene-sort**

Utility to sort refGene tab-delimited annotation files from Genome Browser (DB dumps)
```bash
usage: refgene-sort [-h] [-t TMP] [-q QUERRY] [-s ORDER] -i INPUT -o OUTPUT

refGene annotation sorter

optional arguments:
  -h, --help            show this help message and exit
  -t TMP, --tmp TMP     Temp folder to store sqlite db file
  -q QUERRY, --querry QUERRY
                        Custom select querry. Table name should be refGene
  -s ORDER, --order ORDER
                        Ordering option
  -i INPUT, --input INPUT
                        Input file to location
  -o OUTPUT, --output OUTPUT
                        Output file to location
```