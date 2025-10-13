What is Data Type?

Data types are used to represent the nature of the data that can be stored in the database table. For example, in a particular column of a table, if we want to store a string type of data then we will have to declare a string data type of this column.

Data types mainly classified into three categories for every database.

1.String Data Types-1.varchar(n) 2.char(n) 3.text

2.Numeric Data Types 1.integer 2.smallint 3.bigint 

 FLOAT VALUE 4.numeric(p,s) 5.real 6.double precision

3.Date and Time Data Types 1.date 2.time 3.timestamp 4.timestamptz 5.interval

4.boolean Data Types 1.true/false 2.null





PostgreSQL offers a comprehensive set of data types for various data storage needs. These types are broadly categorized as follows:
1. Numeric Types:
Integers: smallint, integer, bigint (for different ranges of whole numbers), serial, smallserial, bigserial (auto-incrementing integers).

Floating-Point Numbers: real, double precision (for approximate numeric values), numeric, decimal (for exact numeric values with specified precision and scale).

Monetary: money (for currency values).

🧠 Explanation
Data Type	  Precision	                 Description
REAL	~6 decimal digits	Rounded to 12345.679 (loss of precision)
DOUBLE PRECISION	~15 decimal digits	Keeps most digits accurately
NUMERIC(20,10)	Exact (10 digits after decimal)	Fully precise, no rounding errors

💡 When to Use
Scenario	 Recommended     Type
Temperature,  measurements	REAL
Scientific    calculations	DOUBLE PRECISION
Currency, prices, totals	NUMERIC(p, s)



2. Character Types:
char(n): Fixed-length string, padded with spaces if shorter than n.
varchar(n): Variable-length string with a maximum length of n.
text: Variable-length string with virtually unlimited length.

3. Temporal Types:
date: Stores dates (year, month, day).
time: Stores time of day (hour, minute, second).
timestamp, timestamptz: Stores date and time, with timestamptz including time zone information.
interval: Stores time periods.

4. Boolean Type:
boolean: Stores logical true, false, or NULL.

5. Binary Types: bytea: Stores binary strings (byte arrays).

6. Network Address Types: inet: Stores IPv4 and IPv6 hosts and networks, cidr: Stores IPv4 and IPv6 networks, and macaddr: Stores MAC addresses.

7. Bit String Types:
bit(n): Fixed-length bit string.
bit varying(n): Variable-length bit string.

8. Geometric Types:
point, line, lseg, box, path, polygon, circle: For representing geometric objects.

9. Other Specialized Types:
uuid: For storing Universally Unique Identifiers.
json, jsonb: For storing JSON data, with jsonb offering more efficient storage and indexing.
xml: For storing XML data.
enum: For creating custom enumerated types with a predefined set of values.
array: For storing arrays of other data types.
tsvector, tsquery: For full-text search capabilities.