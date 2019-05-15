CREATE TABLE "Location" (
    "LocationId" SERIAL PRIMARY KEY,
    "City"       VARCHAR(100) NOT NULL,
    "Street"     VARCHAR(100) NOT NULL,
    "House"      INT CHECK ( "House" >= 1)
);

CREATE TABLE "Library" (
    "LibraryId"   SERIAL PRIMARY KEY,
    "LocationId"  INT REFERENCES "Location"("LocationId"),
    "LibraryName" VARCHAR(100) NOT NULL
);


CREATE TABLE "Book" (
    "BookId"  SERIAL PRIMARY KEY,
    "Author"  VARCHAR(60) NOT NULL,
    "Title"   VARCHAR(60) NOT NULL
);

CREATE TABLE "Storage" (
    "BookId"    INT REFERENCES "Book"("BookId"),
    "Number"    INT CHECK ("Number" >= 0),
    "LibraryId" INT REFERENCES "Library"("LibraryId")
);

CREATE TABLE "EmployeeType" (
    "EmployeeTypeId"  SERIAL PRIMARY KEY,
    "StaffTypeName"   VARCHAR(100) NOT NULL
);

CREATE TABLE "Employee" (
    "EmployeeId"    SERIAL PRIMARY KEY,
    "EmployeeType"  INT REFERENCES "EmployeeType"("EmployeeTypeId"),
    "FirstName"     VARCHAR(60) NOT NULL,
    "LastName"      VARCHAR(60) NOT NULL,
    "BirthDate"     DATE NOT NULL,
    "StartedToWork" DATE NOT NULL
);

CREATE TABLE "Client" (
    "ClientId"  SERIAL PRIMARY KEY,
    "FirstName" VARCHAR(60) NOT NULL,
    "LastName"  VARCHAR(60) NOT NULL,
    "Phone"     VARCHAR(20) NOT NULL
);


CREATE TABLE "Order" (
    "OrderId"    SERIAL PRIMARY KEY,
    "ClientId"   INT REFERENCES "Client"("ClientId"),
    "BookId"     INT REFERENCES "Book"("BookId"),
    "Date"       DATE NOT NULL ,
    "EmployeeId" INT REFERENCES "Employee"("EmployeeId")
);

CREATE TABLE "CompletedOrder" (
    "CompletedOrderId"  SERIAL PRIMARY KEY,
    "OrderId"           INT REFERENCES "Order"("OrderId"),
    "DateGiving"        DATE NOT NULL ,
    "DateBack"          DATE NOT NULL
);
