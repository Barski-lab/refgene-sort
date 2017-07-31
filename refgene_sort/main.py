import sys
import sqlite3
import tempfile
import argparse
import os


CREATE_REFGENE_TABLE_SCRIPT=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'create_refgene_table.sql'), 'r').read()


def arg_parser():
    """Returns argument parser"""
    parser = argparse.ArgumentParser(description='refGene annotation sorter')
    parser.add_argument ("-t", "--tmp", help="Temp folder to store sqlite db file", default=None)
    parser.add_argument ("-q", "--querry", help="Custom select querry. Table name should be refGene", default="SELECT * FROM refGene")
    parser.add_argument("-s", "--order", help="Ordering option", default='')
    parser.add_argument("-i", "--input", help="Input file to location", required=True)
    parser.add_argument("-o", "--output", help="Output file to location", required=True)
    return parser


def get_tmp_file (args):
    return tempfile.mkstemp(dir=args.tmp)


def run_sql_script(connection, script):
    connection.cursor().executescript(script)
    connection.commit()


def load_from_file(connection, filename):
    header=''
    with open(filename, 'r') as data_file:
        for line in data_file.readlines():
            if "bin" in line and "name" in line and 'exonCount' in line:
                header=line.strip()
                continue
            line_splitted=line.strip().split()
            sql_insert = "INSERT INTO refGene VALUES (" \
                         "{},'{}','{}','{}',{},{},{}," \
                         "{},{},'{}','{}',{},'{}'," \
                         "'{}','{}','{}')".format(*line_splitted)
            """
                `bin` smallint(5) NOT NULL,
                `name` varchar(255) NOT NULL,
                `chrom` varchar(255) NOT NULL,
                `strand` char(1) NOT NULL,
                `txStart` int(10) NOT NULL,
                `txEnd` int(10) NOT NULL,
                `cdsStart` int(10) NOT NULL,
                `cdsEnd` int(10) NOT NULL,
                `exonCount` int(10) NOT NULL,
                `exonStarts` longblob NOT NULL,
                `exonEnds` longblob NOT NULL,
                `score` int(11) DEFAULT NULL,
                `name2` varchar(255) NOT NULL,
                `cdsStartStat` varchar(255) NOT NULL,
                `cdsEndStat` varchar(255) NOT NULL,
                `exonFrames` longblob NOT NULL
            """
            connection.cursor().execute(sql_insert)
    connection.commit()
    return header


def select_from_db(connection, querry, order):
    c=connection.cursor()
    cmd=querry+' '+order
    print cmd
    c.execute(cmd)
    return c.fetchall()


def export_to_file(header, rows, outputfile):
    outputfile=os.path.join(os.getcwd(),outputfile) if not os.path.isabs(outputfile) else outputfile
    with open(outputfile, 'w') as output_stream:
        output_stream.write(header+'\n')
        for row in rows:
            output_stream.write('\t'.join(map(str,row))+'\n')


def main(argsl=None):
    if argsl is None:
        argsl = sys.argv[1:]
    args, _ = arg_parser().parse_known_args(argsl)
    sql_temp_file=get_tmp_file(args)[1]
    try:
        connection = sqlite3.connect(sql_temp_file)
        run_sql_script(connection, CREATE_REFGENE_TABLE_SCRIPT)
        header = load_from_file(connection, args.input)
        export_to_file (header, select_from_db(connection, args.querry, args.order), args.output)
        connection.close()
    except Exception as ex:
        print str(ex)
    finally:
        os.remove(sql_temp_file)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
