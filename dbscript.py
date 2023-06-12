import logging
import psycopg2

logging.basicConfig(format='%(name)s:[%(levelname)s] %(message)s',  level=logging.DEBUG)
log = logging.getLogger(__name__)
DATAPATH = "./studentDetails.txt"

conn = psycopg2.connect(
    host="db",
    database="postgres",
    user="postgres",
    password="postgres",
    port=5432
)

cursor = conn.cursor()
log.info(f"Connected to database: {cursor}")

def initialize_tables():
    """
    Creates tables if they do not exist.
    Returns true if the tables were create from this call, 
    and false if they alreadt existed.
    """
    query = """
    CREATE TABLE IF NOT EXISTS studentdetails (
            rollno INTEGER PRIMARY KEY,
            name VARCHAR(50),
            hostel VARCHAR(15),
            room INTEGER,
            mess INTEGER,
            messpref CHAR(3),
            dept VARCHAR(10),
            year INTEGER
    );
    """
    cursor.execute(query)
    conn.commit()
    log.info("Created table studentdetails.")

def dept(rollno):
    first4 = rollno[:4]
    if first4 == "1061": return "CSE"
    elif first4 == "1031": return "Civil"
    elif first4 == "1021": return "Chem"
    elif first4 == "1071": return "EEE"
    elif first4 == "1081": return "ECE"
    elif first4 == "1101": return "ICE"
    elif first4 == "1111": return "Mech"
    elif first4 == "1121": return "MME"
    elif first4 == "1141": return "Arch"
    elif first4 == "1011": return "Prod"
    else: return "NA"

def insert_data():
    with open(DATAPATH) as f:
        # Skip the first line since it contains the column names
        _ = f.readline()

        for line in f:
            l = line.split()
            cursor.execute(
                "INSERT INTO studentdetails VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING",
                (l[1], l[0], l[2], l[3], l[4], l[5], dept(l[1]), '2022')
            )
            conn.commit()
        
        log.info("Inserted data into table studentdetails.")
        
def view_data():
    cursor.execute("SELECT * FROM studentdetails")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    

def main():
    initialize_tables()
    insert_data()
    view_data()

main()