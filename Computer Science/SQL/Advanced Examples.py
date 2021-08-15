# Task: convert rows of a table into columns
# Table:
#   Country     City
#   USA         New York
#   USA         Houston
#   USA         Dallas
#   India       Hybera
#   India       Banga
#   India       New Delhi
#   UK          London
#   UK          Bermington
#   UK          Manchester
# Result:
#   Country     City1       City2       City3
#   India       Hybera      Banga       New Delhi
#   UK          London      Bermington  Manchester
#   USA         Mew York    Houston     Dallas
# Code:
    # SELECT * FROM countries
    #
    # SELECT Country, City1, City2, City3
    # FROM (
    #   SELECT Country, City
    #       'City' + CAST(ROW_NUMBER() OVER (PARTITION BY Country ORDER BY Country) AS Varchar(10)) AS ColumnSequence
    #   FROM Countries
    #  ) Temp # name of table = 'Temp'
    #
    # PIVOT (
    #   MAX(City)
    #   FOR ColumnSequence IN (City1, City2, City3)
    # ) Piv

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Write a query to pull all of the members who have a primary home address and show the results. 
# Fields must include: FULL NAME, Address_Line_1, City, State, Zip_Code. 
# A value of 1 in the Primary_Address field indicates that the address is the primary one.
# Tables: 
    # Tbl_Members
    # id_members       First_Name      Last_Name
    # 151                     John            Smith
    # 152                     Karen           Williams
    # 153                     Lee             Johnson

    # Tbl_Address
    # id_address    address_type      primary_address     address_line_1      city    state   zip_code    Tbl_Members_id
    # 1             Home              1                   3321 Green St       Denver  CO      80124       151
    # 2             Work              0                   556 White Drive     Boulder CO      80224       152
    # 3             Home              1                   1246 Greenvile St   Denver  CO      81234       153
# Query:
    # SELECT
    #     CONCAT(First_Name, ' ', Last_Name) AS FULL_NAME,
    #     Address_Line_1 AS Address,
    #     City,
    #     State,
    #     Zip_Code AS Zip
    # FROM
    #     tbl_Members INNER JOIN tbl_address ON 
    #       tbl_Members.id_members = tbl_address.id_address
    # WHERE
    #     primary_address = 1 AND address_type = 'Home'              
# Result:
    # FULL_NAME     Address             City    State   Zip
    # John Smith    3321 Green St       Denver  CO      80124
    # Lee Johnson   1246 Greenvile St   Denver  CO      81234