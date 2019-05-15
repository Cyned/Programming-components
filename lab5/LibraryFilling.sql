INSERT INTO "Location" VALUES
(1, 'Kiev', 'Yangela', 20),
(2, 'Kiev', 'Saksaganskogo', 29);


INSERT INTO "Library" VALUES
(1, 1, 'Taras Schevchenko Library');

INSERT INTO "Book" VALUES
(1, 'P.S. Scott', 'Angel Land: A Teen/YA Fantasy Light Novel'),
(2, 'Alan Hurst', 'The Onyx Crown: Part I of a Trilogy '),
(3, 'G. Willow Wilson', 'The Bird King '),
(4, 'y R.F. Kuang', 'The Dragon Republic');


INSERT INTO "Storage" VALUES
(1, 2, 1),
(2, 2, 1),
(3, 0, 1);

INSERT INTO "EmployeeType" VALUES
(1, 'Security guard'),
(2, 'Administrator'),
(3, 'Librarian'),
(4, 'Cleaner');

INSERT INTO "Employee" VALUES
(1, 1, 'Sergey',  'Sydoryuk',  '1997-01-27', '2019-01-10'),
(2, 2, 'Aleksey', 'Semenov',   '1980-05-04', '2018-04-11'),
(3, 3, 'Alina',   'Puschkina', '1975-11-15', '2017-10-01'),
(4, 4, 'Sergey',  'Smirnov',   '2000-02-28', '2019-03-26');


INSERT INTO "Client" VALUES
(1, 'Sasha', 'Alekseeva', '0502346536'),
(2, 'Denis', 'Sidorov',   '0960349586');

INSERT INTO "Order" VALUES
(1, 1, 1, '2019-04-01', 3);

INSERT INTO "CompletedOrder" VALUES
(1, 1, '2019-04-03', '2019-04-17');
