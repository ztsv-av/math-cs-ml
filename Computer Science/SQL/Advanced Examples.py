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