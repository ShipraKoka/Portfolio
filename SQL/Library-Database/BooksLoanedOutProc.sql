USE [dbLibrary]
GO

/****** Object:  StoredProcedure [dbo].[GetBooksLoanedOut]    Script Date: 02/01/2016 18:41:02 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE PROC [dbo].[GetBooksLoanedOut]
AS
SELECT DISTINCT LB.BranchName, COUNT(BL.BranchID) AS Total_Loaned
FROM Library_Branch AS LB
INNER JOIN Book_Loans AS BL
ON LB.BranchID = BL.BranchID
GROUP BY LB.BranchName
GO


