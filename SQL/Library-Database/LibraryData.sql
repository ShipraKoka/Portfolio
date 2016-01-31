INSERT INTO Publisher
VALUES('CreateSpace', NULL, NULL),
('Simon & Schuster', NULL, NULL),
('Anchor', NULL, NULL),
('Hogarth Press', NULL, NULL),
('St. Martin''s Griffin', NULL, NULL),
('Harper Perennial', NULL, NULL),
('Penguin Books', NULL, NULL),
('Puffin Books', NULL, NULL),
('Gallery Books', NULL, NULL),
('HarperCollins', NULL, NULL),
('Kodansha', NULL, NULL),
('Vintage', NULL, NULL),
('Little, Brown Books for Young Readers', NULL, NULL),
('Farrar, Straus and Giroux', NULL, NULL),
('Harper Perennial Modern Classics', NULL, NULL),
('Penguin Classics', NULL, NULL)
SELECT * FROM Publisher
ORDER BY Name ASC

INSERT INTO Book
VALUES (1, 'The Lost Tribe', 'CreateSpace'),
(2, 'Way Up High in a Tall Green Tree', 'Simon & Schuster'),
(3, 'The Shining', 'Anchor'),
(4, 'Mrs. Dalloway', 'Hogarth Press'),
(5, 'The Wright Brothers', 'Simon & Schuster'),
(6, 'Smart Talk', 'St. Martin''s Griffin'),
(7, 'Brain Lock: Free Yourself from Obsessive-Compulsive Behavior', 'Harper Perennial'),
(8, 'The Joy Luck Club', 'Penguin Books'),
(9, 'Matilda', 'Puffin Books'),
(10, 'The Raven', 'Gallery Books'),
(11, 'Where the Sidewalk Ends', 'HarperCollins'),
(12, 'Akira', 'Kodansha'),
(13, 'The Big Sleep', 'Vintage'),
(14, 'The Thing About Jellyfish', 'Little, Brown Books for Young Readers'),
(15, 'Thinking, Fast and Slow', 'Farrar, Straus and Giroux' ),
(16, 'A People''s History of the United States', 'Harper Perennial Modern Classics'),
(17, 'Jane Eyre', 'Penguin Classics'),
(18, 'Frankenstein', 'CreateSpace'),
(19, 'Tales of the City: A Novel', 'Harper Perennial'),
(20, 'The Lady in the Lake', 'Vintage')
SELECT * FROM Book

INSERT INTO Book_Authors
VALUES (1, 'Matthew Caldwell'),
(2, 'Jan Peck'),
(3, 'Stephen King'),
(4, 'Virginia Woolf'),
(5, 'David McCullough'),
(6, 'Lisa B. Marshall'),
(7, 'Jeffrey M. Schwartz'),
(8, 'Amy Tan'),
(9, 'Roald Dahl'),
(10, 'Edgar Allan Poe'),
(11, 'Shel Silverstein'),
(12, 'Katsuhiro Otomo'),
(13, 'Raymond Chandler'),
(14, 'Ali Benjamin'),
(15, 'Daniel Kahneman'),
(16, 'Howard Zinn'),
(17, 'Charlotte Bronte'),
(18, 'Mary Shelley'),
(19, 'Armistead Maupin'),
(20, 'Raymond Chandler')
SELECT * FROM Book_Authors


INSERT INTO Library_Branch
VALUES (1, 'Sharpstown', NULL),
(2, 'Central', NULL),
(3, 'Union', NULL),
(4, ' Crossroads', NULL)
SELECT * FROM Library_Branch

INSERT INTO Book_Copies
VALUES 
(3, 1, 3), (4, 1, 2), (5, 1, 2), (7, 1, 2), (8, 1, 3), (9, 1, 5), (10, 1, 2), (13, 1, 3), (14, 1, 4), (15, 1, 3),
(1, 2, 2), (2, 2, 2), (4, 2, 4), (5, 2, 3), (6, 2, 4), (7, 2, 2), (9, 2, 3), (11, 2, 2), (16, 2, 2), (17, 2, 2),
(1, 3, 2), (3, 3, 2), (5, 3, 4), (6, 3, 2), (15, 3, 2), (16, 3, 2), (17, 3, 2), (18, 3, 3), (19, 3, 4), (20, 3, 4),
(2, 4, 2), (3, 4, 3), (4, 4, 2), (5, 4, 5), (7, 4, 5), (9, 4, 2), (12, 4, 2), (13, 4, 5), (14, 4, 2), (19, 4, 2)
SELECT * FROM Book_Copies
ORDER BY BookID ASC

INSERT INTO Borrower
VALUES (1, 'Andrea Smith', '123 Third St, Los Angeles, CA 92475', '310-555-1234'),
(2, 'Bob Griffin', '411 Garrison Ave, Ventura, CA 92658', '818-421-8367'),
(3, 'Janet Stevens', '81930 Eton Dr, Van Nuys, CA 92758', '818 -284-2857'),
(4, 'Sandy Johnson', '39578 Hanson St, Los Angeles, CA 92849', '310-498-2948'),
(5, 'Carl Sanders', '2953 Marlon Pl, Los Angeles, CA 94847', '310-489-2948'),
(6, 'Sam Levinson', '29437 Maple Dr, Corona, CA 92874', '951-398-2938'),
(7, 'Melody Harper', '2938 Balboa Blvd, Van Nuys, CA 92758', '818-555-2540'),
(8, 'Christopher Mann', '297 First St, Sherman Oaks, CA 91837', '818-293-0284'),
(9, 'David Anderson', '19345 Sepulveda Blvd, Los Angeles, CA 90024', '310-249-3290'),
(10, 'Jill Higgins', '2948 Market Ave, Santa Monica, CA 90064', '310-329-2395')
SELECT * FROM Borrower

INSERT INTO Book_Loans(BookID, BranchID, CardNo, DateOut)
VALUES (1, 2, 5, '5/2/2014'),
(6, 2, 5, '5/2/2014'),
(4, 2, 5, '10/1/2015'),
(7, 2, 5, '11/13/2015'),
(11, 2, 5, '7/11/2015'),
(17, 2, 5, '7/11/2015'),
(5, 3, 7, '2/4/2015'),
(16, 3, 7, '2/4/2015'),
(17, 3, 7, '11/1/2015'),
(3, 3, 7, '6/4/2013'),
(6, 3, 7, '5/18/2015'),
(18, 3, 7, '5/18/2015'),
(20, 3, 7, '5/18/2015'),
(1, 2, 1, '8/9/2014'),
(6, 2, 1, '8/9/2104'),
(11, 2, 1, '8/9/2104'),
(2, 4, 2, '5/9/2015'),
(4, 4, 2, '6/5/2015'),
(7, 4, 2, '7/1/2015'),
(9, 4, 2, '7/15/2015'),
(13, 4, 2, '8/1/2015'),
(8, 1, 3, '11/14/2015'),
(9, 1, 3, '11/14/2015'),
(3, 1, 4, '10/4/2013'),
(8, 1, 4, '1/29/2012'),
(10, 1, 4, '9/3/2014'),
(13, 1, 4, '3/17/2015'),
(3, 1, 8, '4/27/2015'),
(4, 1, 8, '4/27/2015'),
(7, 1, 8, '4/27/2015'),
(9, 1, 8, '4/27/2015'),
(10, 1, 8, '10/30/2015'),
(13, 1, 8, '10/30/2015'),
(15, 1, 8, '10/30/2015'),
(1, 3, 6, '8/4/2014'),
(3, 3, 6, '7/3/2015'),
(5, 3, 6, '8/15/2015'),
(15, 3, 6, '8/4/2014'),
(17, 3, 6, '8/4/2014'),
(19, 3, 6, '8/15/2015'),
(4, 4, 9, '11/8/2015'),
(5, 4, 9, '11/8/2015'),
(12, 4, 9, '11/8/2015'),
(14, 4, 9, '11/8/2015'),
(19, 4, 9, '11/8/2015'),
(4, 2, 10, '4/25/2015'),
(5, 2, 10, '9/30/2015'),
(6, 2, 10, '11/2/2015'),
(9, 2, 10, '4/25/2015'),
(16, 2, 10, '5/3/2013')
GO
EXEC CalcDueDate --Calculates and inputs the due date for each record in the Book_Loans table
SELECT * FROM Book_Loans
ORDER BY DateOut



