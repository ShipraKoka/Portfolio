USE [dbLibrary]
GO

/****** Object:  StoredProcedure [dbo].[GetBranchDueToday]    Script Date: 02/01/2016 18:42:48 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE PROC [dbo].[GetBranchDueToday]
AS
SELECT Bk.Title, Bor.Name, Bor.[Address]
FROM Library_Branch AS LB
INNER JOIN Book_Loans AS BL
ON LB.BranchID = BL.BranchID
INNER JOIN Borrower AS Bor
ON BL.CardNo = Bor.CardNo
INNER JOIN Book AS Bk
ON Bk.BookID = BL.BookID
WHERE DueDate = GETDATE()
GO


