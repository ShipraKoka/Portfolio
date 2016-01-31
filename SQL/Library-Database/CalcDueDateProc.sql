USE [dbLibrary]
GO

/****** Object:  StoredProcedure [dbo].[CalcDueDate]    Script Date: 11/16/2015 14:30:17 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE PROC [dbo].[CalcDueDate]
AS
DECLARE @RN INT
DECLARE Record CURSOR
FOR
SELECT BookID FROM Book_Loans
OPEN Record
FETCH NEXT FROM Record INTO @RN
WHILE @@FETCH_STATUS = 0
BEGIN
UPDATE Book_Loans
SET DueDate = DATEADD(MONTH, 1, DateOut)
WHERE CURRENT OF Record
FETCH NEXT FROM Record INTO @RN
END
CLOSE Record
DEALLOCATE Record

GO


