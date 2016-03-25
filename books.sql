
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
INSERT INTO "books_author" VALUES(1,'Mr.','Bart Baesens');
INSERT INTO "books_author" VALUES(2,'Mr.','Aimee Backiel');
INSERT INTO "books_author" VALUES(3,'Mr.','Seppe vanden Broucke');
INSERT INTO "books_author" VALUES(4,'Mr.','Jay McGavren');
INSERT INTO "books_author" VALUES(5,'Mr.','Ian F. Darwin');
INSERT INTO "books_publisher" VALUES(1,'Wroxx Press','10475 Crosspoint Blvd.','Indianapolis','IN 46256');
INSERT INTO "books_publisher" VALUES(2,'O''Reilly Media','1005 Gravenstein Hwy N','Sebastopol','CA 95472');
INSERT INTO "books_book" VALUES(1,'Beginning Java Programming: The Object-Oriented Approach','2015-04-01',1);
INSERT INTO "books_book" VALUES(2,'Head First Ruby: A learner''s companion to Ruby','2015-08-01',2);
INSERT INTO "books_book" VALUES(3,'Java Cookbook, 3rd Edition','2014-05-01',2);
INSERT INTO "books_book_authors" VALUES(1,1,1);
INSERT INTO "books_book_authors" VALUES(2,1,2);
INSERT INTO "books_book_authors" VALUES(3,1,3);
INSERT INTO "books_book_authors" VALUES(4,2,4);
INSERT INTO "books_book_authors" VALUES(5,3,5);
COMMIT;
