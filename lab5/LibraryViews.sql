create view "AvailableBooks" as
select "Author", "Title", "LibraryName" from "Book"
inner join "Storage" using("BookId")
inner join "Library" using("LibraryId")
where "Number" > 0;

select * from "AvailableBooks";

create view "PersonBook" as
select "FirstName", "LastName", "Author", "Title" from "Client"
inner join "Order" using("ClientId")
inner join "Book" using("BookId")
inner join "CompletedOrder" using("OrderId");

select * from "PersonBook";