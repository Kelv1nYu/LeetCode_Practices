SELECT FirstName, LastName, City, State
FROM Person
LEFT JOIN Address
ON Person.PersonId = Address.PersonId;



SELECT FirstName, LastName, City, State
FROM Person
LEFT JOIN Address
USING(PersonId);
