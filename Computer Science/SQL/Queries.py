# Each statement ends with a semicolon (;)

# CREATE is primarily used in the creation of objects (e.g., tables) within a database.
# CREATE syntax:
    # CREATE TABLE TableName(
        # Fieldname1 datatype properties,
        # Fieldname2 datatype properties,
        # Fieldname3 datatype properties,
        # Fieldname4 datatype properties);   
# for primary keys:
    # Fieldname INT IDENTITY (1,1) #auto numbering property, created automatically

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# SELECT statement
# The SELECT statement is used to select data from a database.
# The data returned is stored in a result table, called the result-set.
# Example:
    # SELECT expressions
    # FROM tables
    # [WHERE conditions]
    # [ORDER BY expression [ ASC | DESC ]];

# Simpler:
    # SELECT * from tables;

#Another example:
# Table 1:
# customer_id	last_name	first_name	favorite_website
# 4000	        Jackson	    Joe	        techonthenet.com
# 5000	        Smith	    Jane	    digminecraft.com
# 6000	        Ferguson	Samantha	bigactivities.com
# 7000	        Reynolds	Allen	    checkyourmath.com
# 8000	        Anderson	Paige	    NULL
# 9000	        Johnson	    Derek	    techonthenet.com

#Table 2:
# order_id	customer_id	order_date
# 1	        7000	    2016/04/18
# 2	        5000	    2016/04/18
# 3	        8000	    2016/04/19
# 4	        4000	    2016/04/20
# 5	        NULL	    2016/05/01

    # SELECT orders.order_id, customers.last_name
    # FROM orders
    # INNER JOIN customers
    # ON orders.customer_id = customers.customer_id
    # WHERE orders.order_id <> 1
    # ORDER BY orders.order_id;

# Result:
# order_id	last_name
# 2	Smith
# 3	Anderson
# 4	Jackson

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# An INSERT statement is used to add data into a table within a relational database.
# You do not have to include all of the columns in an INSERT statement—only those where a value should be entered.
# You also need to ensure that you are including the PRIMARY KEY and that each primary key value is unique. 
# A PRIMARY KEY can be set to auto-increment when it is a numeric value. In these cases, the PRIMARY KEY does not have to be included in the INSERT statement.
# Information can be added one row at a time using the following syntax:
    # INSERT [LOW_PRIORITY | DELAYED | HIGH_PRIORITY] [IGNORE]
    #     [INTO] tbl_name
    #     [PARTITION (partition_name,...)]
    #     [(col_name,...)]
    #     {VALUES | VALUE} ({expr | DEFAULT},...),(...),...
    #     [ ON DUPLICATE KEY UPDATE
    #        col_name=expr
    #        [, col_name=expr] ... ]

# Or simpler:
    # INSERT INTO tablename (COL1, COL2, …. ,COLn ) VALUES (value1, value2, …, valueN)

# Rows can also be added in bulk using a SELECT statement. The syntax would look like the following (MySQL, n.d.b):
    # INSERT [LOW_PRIORITY | HIGH_PRIORITY] [IGNORE]
    #     [INTO] tbl_name
    #     [PARTITION (partition_name,...)]
    #     [(col_name,...)]
    #     SELECT ...
    #     [ ON DUPLICATE KEY UPDATE
    #        col_name=expr
    #        [, col_name=expr] ... ]

# Or simpler:
    # INSERT INTO tablename (COL1, COL2, …, COLn) SELECT COLb1, COLb2, …., COLbn FROM tablename2 WHERE …
# Example: 
    # INSERT INTO TBL_Names SELECT UID, First_Name, Last_Name from tbl_OldNames where first_name = ‘Phillip';

# Example of INSERT method to 'tbl_Member2' table:
    # INSERT INTO `mydb`.`tbl_Member2` 
    # (`Member_ID`, `Last_Name`, `First_Name`, `EMail`, `Address_Line_1`, `Address_Line_2`, `City`, `State`, `Zip`, `Phone`) 
    # VALUES 
    # (12, 'Membertwo', 'Sarah', 'membertwo@email.com', '222SilverAve', '', 'Denver', '', '', '720-345-2222');

# 'mydb' is a database where table 'tbl_Member2' is located
# 'tbl_Member2' column datatypes:
# (`Member_ID`, `Last_Name`, `First_Name`, `EMail`, `Address_Line_1`, `Address_Line_2`, `City`, `State`, `Zip`, `Phone`)
# INT, VARCHAR(45), VARCHAR(45), VARCHAR(45), VARCHAR(45), VARCHAR(45), VARCHAR(45), VARCHAR(45), VARCHAR(45) 

#The following example shows how to do a multitable insert through an INSERT ALL statement, which is not supported by all databases but is supported by ORACLE 9i databases and higher (Gennick, 2005):
    #  INSERT ALL
    #        INTO table1 (column1, column2, …, columnN) VALUES (value1, value2, …., valueN)
    #        INTO table2 (column1, column2, …, columnN) VALUES (value1, value2, …., valueN)
    #        ….
    #        INTO tableN(column1, column2, …, columnN) VALUES (value1, value2, …., valueN)
    #  SELECT * from dual;
# The SELECT * from dual part of the statement allows you to enter your own values. 
# If you wanted to use a SELECT statement, the value1 to valueN for each area would be the column names from the SELECT statement at the bottom of the INSERT ALL statement. 
# Because a SELECT statement can come from one or more tables, the columns can use any of the specified columns' names across each table that is specified in the SELECT statement.

# An INSERT ALL can also be performed conditionally. 
# The example above is an unconditional INSERT ALL wherein all of the INSERT statements are performed without any conditions.
#  For a conditional INSERT ALL, the syntax would look mostly the same; however, it would contain a WHEN statement. The syntax would be as follows:
    # INSERT ALL|FIRST
    #      [WHEN condition THEN] INTO target [VALUES]
    #      [WHEN condition THEN] INTO target [VALUES]
    #      ...
    #      [ELSE] INTO target [VALUES]
    # SELECT ...
    # FROM source_query;
# Using the FIRST statement will allow the row to fall into the FIRST condition that was met vice all of the conditions that might be met with the row value being tested.

# Copy data from one table to another:
    # INSERT INTO table2
    # SELECT * FROM table1;
# or specific columns:
    # INSERT INTO table2
    # (column_name(s))
    # SELECT column_name(s)
    # FROM table1;
# or create new table with columns:
    # SELECT * INTO SupplierUSA
    # FROM Supplier
    # WHERE Country = 'USA'
# This will create a SupplierUSA table that has the same columns as the Supplier table.

# If the database that you are using does not support INSERT ALL, the recommended way to add rows to multiple tables is to use transactions. 
# A transaction will ensure that all of the statements included within will be completed or ignored together. Consider the following example:
    # START TRANSACTION
    #      [transaction_characteristic [, transaction_characteristic] ...]
    # transaction_characteristic:
    #      WITH CONSISTENT SNAPSHOT
    #      | READ WRITE
    #      | READ ONLY
# Once a transaction is started, it must be ended with either a COMMIT or a ROLLBACK. 
# A COMMIT processes the statements within the transaction to make the changes permanent. 
# A ROLLBACK cancels all of the changes made within the transaction.
# The following is a quick example:
    # START TRANSACTION;
    # SELECT @A:=SUM(salary) FROM table1 WHERE type=1;
    # UPDATE table2 SET summary=@A WHERE type=1;
    # COMMIT;
# Transactions can be short, such as the example above, or long, with the transaction containing multiple statements. 
# It is important to be aware that not all statements can be rolled back. 
# The statements that are done within a transaction that impact the database structure, such as a CREATE table, an ALTER table, or a DROP table, cannot be rolled back.

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Several common conversions might be converting a TYPE1 value to a TYPE2 or the other way around.
# Often, a CAST function will work to accomplish this goal, as shown in the following:
    # CAST(datetime_col AS DATE)    (This will take a DATETIME value and convert it to a DATE value.)

# CONVERT is also another function:
    # CONVERT(expr USING transcoding_name)


# DELETE statement
# It is important to remember that DELETE only works on data and not on any type of database component, 
# such as a field, table, index, or view. 
# In these cases, a DROP or ALTER command would be used. DELETE is solely used on data, specifically entire rows of data, stored within the database.
#Again, if you just want to delete the value for a specific field of data, an UPDATE command would be used to set the value to null, zero, or empty. 
# DELETE is used only for the removal of an entire row or rows of data at one time.

# Single Table
    # DELETE [LOW_PRIORITY] [QUICK] [IGNORE] FROM tbl_name
    #  [PARTITION (partition_name,...)]
    #  [WHERE where_condition]
    #  [ORDER BY ...]
    #  [LIMIT row_count]                         

# Multiple Tables
    # DELETE [LOW_PRIORITY] [QUICK] [IGNORE]
    #  tbl_name[.*] [, tbl_name[.*]] ...
    #  FROM table_references
    #  [WHERE where_condition]                       

# Or
    # DELETE [LOW_PRIORITY] [QUICK] [IGNORE]
    #  FROM tbl_name[.*] [, tbl_name[.*]] ...
    #  USING table_references
    #  [WHERE where_condition]

# Simpler
    # DELETE FROM tbl_Player WHERE UID = 10;

# Delete all data from table (if you need to delete table, use DROP):
    # DELETE from table

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# TRUNCATE statement.
# TRUNCATE is another statement which is used to delete ALL data from a table, but not the table itself.
# The DELETE statement removes rows one at a time and records an entry in the transaction log for each deleted row. 
# TRUNCATE TABLE removes the data by deallocating the data pages used to store the table data and records only the page deallocations in the transaction log. 
# DELETE command is slower than TRUNCATE command.
# Example of TRUNCATE:
    # TRUNCATE TABLE TableName; 

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# UPDATE statement.
# When using UPDATE to a single row, the WHERE clause becomes very important to single out the row that you want to update.
# Example:
    # UPDATE tbl_Player set Team_ID = 1 where Lastname like ‘J*’
    # UPDATE tbl_Player set TeamID = 3 where ISNULL(TeamID)     (ISNULL function tests to see whether the value specified in the column is set to NULL.
    #                                                            If expr is NULL, ISNULL() returns 1, otherwise it returns 0.)

# The following is a single-table syntax update:
    # UPDATE [LOW_PRIORITY] [IGNORE] table_reference
    #     SET col_name1={expr1|DEFAULT} [, col_name2={expr2|DEFAULT}] ...
    #     [WHERE where_condition]
    #     [ORDER BY ...]
    #     [LIMIT row_count]

# The following is a multiple-table syntax update:
    # UPDATE [LOW_PRIORITY] [IGNORE] table_references
    #     SET col_name1={expr1|DEFAULT} [, col_name2={expr2|DEFAULT}] ...
    #     [WHERE where_condition]

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Locking tables helps keep other sessions from interfering with the data within the specified tables. See the following example:
    # LOCK TABLES
    #      tbl_name [[AS] alias] lock_type
    #      [, tbl_name [[AS] alias] lock_type] ...
    # lock_type:
    #      READ [LOCAL]
    #      | [LOW_PRIORITY] WRITE
    # UNLOCK TABLES
# Using locks on tables can also contribute to sessions working together. The interaction or non-interaction between sessions depends on how the tables are locked.
# The following sections describe the different types of locks.
# The READ [LOCAL] lock has the following characteristics (MySQL, n.d.f):
    # The session that holds the lock can read from a table but cannot write to it.
    # Multiple sessions can acquire a READ lock for a table at the same time.
    # Other sessions can read a table without explicitly acquiring a READ lock.
    # The LOCAL modifier allows nonconflicting INSERT statements (concurrent inserts) by other sessions to execute while the lock is held. 
        # However, READ LOCAL cannot be used if you are going to manipulate a database using processes that are external to the server while you hold the lock.
# The WRITE lock has the following characteristics (MySQL, n.d.f):
    # The session that holds the lock can read from and write to a table.
    # Only the session that holds the lock can access a table. No other session can access the table until the lock is released.
    # Lock requests for a table from other sessions are blocked while the WRITE lock is held.

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
