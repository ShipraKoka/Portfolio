--(1)How many copies of the book titled "The Lost Tribe" are owned by the library branch whose name is "Sharpstown"?
SELECT Bk.Title, BC.No_Of_Copies, LB.BranchName
FROM Book AS Bk
INNER JOIN Book_Copies AS BC
ON Bk.BookID = BC.BookID
INNER JOIN Library_Branch AS LB
ON BC.BranchID = LB.BranchID
WHERE Bk.Title = 'The Lost Tribe'
AND LB.BranchName = 'Sharpstown'

--(2)How many copies of the book titled "The Lost Tribe" are owned by each library branch?
SELECT Bk.Title, BC.No_Of_Copies, LB.BranchName
FROM Book AS Bk 
INNER JOIN Book_Copies AS BC
ON Bk.BookID = BC.BookID
INNER JOIN Library_Branch AS LB
ON BC.BranchID = LB.BranchID
WHERE Bk.Title = 'The Lost Tribe'

--(3)Retrieve the names of all borrowers who do not have any books checked out.
SELECT DISTINCT Bor.Name, BL.BookID
FROM Borrower AS Bor
LEFT OUTER JOIN Book_Loans AS BL
ON Bor.CardNo = BL.CardNo
WHERE BL.DueDate IS NULL

--(4)For each book that is loaned out from the "Sharpstown" branch and whose DueDate is today,
--retrieve the book title, the borrower's name, and the borrower's address.
SELECT Bk.Title, Bor.Name, Bor.[Address]
FROM Library_Branch AS LB
INNER JOIN Book_Loans AS BL
ON LB.BranchID = BL.BranchID
INNER JOIN Borrower AS Bor
ON BL.CardNo = Bor.CardNo
INNER JOIN Book AS Bk
ON Bk.BookID = BL.BookID
WHERE DueDate = GETDATE()
AND LB.BranchName = 'Sharpstown'

--(5)For each library branch, retrieve the branch name and the total number of books loaned out from that branch.
SELECT DISTINCT LB.BranchName, COUNT(BL.BranchID) AS Total_Loaned
FROM Library_Branch AS LB
INNER JOIN Book_Loans AS BL
ON LB.BranchID = BL.BranchID
GROUP BY LB.BranchName

--(6)Retrieve the names, addresses, and number of books checked out for all borrowers who have more than five 
--books checked out.
SELECT Bor.Name, Bor.[Address], COUNT(BL.CardNo) AS TotalBooks
FROM Borrower AS Bor
INNER JOIN Book_Loans AS BL
ON Bor.CardNo = BL.CardNo
GROUP BY Bor.Name, Bor.[Address]
HAVING COUNT(BL.CardNo) > 5

--(7)For each book authored (or co-authored) by "Stephen King", retrieve the title and the number of copies 
--owned by the library branch whose name is "Central"
SELECT Bk.Title, BC.No_Of_Copies
FROM Book_Authors AS BA
INNER JOIN Book_Copies AS BC
ON BA.BookID = BC.BookID
INNER JOIN Book AS Bk
ON BC.BookID = Bk.BookID
INNER JOIN Library_Branch AS LB
ON BC.BranchID = LB.BranchID
WHERE LB.BranchName = 'Central'
AND BA.AuthorName LIKE '%Stephen King%'

