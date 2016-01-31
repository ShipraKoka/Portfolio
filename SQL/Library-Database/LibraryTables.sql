USE master
GO

CREATE DATABASE dbLibrary

USE dbLibrary
GO

CREATE TABLE Publisher
(
Name nvarchar(50) PRIMARY KEY,
[Address] nvarchar(75) NULL,
Phone varchar(25) NULL
)

CREATE TABLE Book
(
BookID int PRIMARY KEY,
Title nvarchar(75) NOT NULL,
PublisherName nvarchar(50) FOREIGN KEY REFERENCES Publisher(Name) NULL
)

CREATE TABLE Book_Authors
(
BookID int FOREIGN KEY REFERENCES Book(BookID),
AuthorName nvarchar(50)
)

CREATE TABLE Library_Branch
(
BranchID int PRIMARY KEY,
BranchName varchar(30) NOT NULL,
[Address] varchar(75) NULL
)

CREATE TABLE Borrower
(
CardNo int PRIMARY KEY,
Name varchar(50) NOT NULL,
[Address] varchar(75) NOT NULL,
Phone varchar(25) NOT NULL
)

CREATE TABLE Book_Copies
(
BookID int FOREIGN KEY REFERENCES Book(BookID),
BranchID int FOREIGN KEY REFERENCES Library_Branch(BranchID),
No_Of_Copies int NOT NULL
)

CREATE TABLE Book_Loans
(
BookID int FOREIGN KEY REFERENCES Book(BookID),
BranchID int FOREIGN KEY REFERENCES Library_Branch(BranchID),
CardNo int FOREIGN KEY REFERENCES Borrower(CardNo),
DateOut DATE NOT NULL,
DueDate DATE NULL
)
