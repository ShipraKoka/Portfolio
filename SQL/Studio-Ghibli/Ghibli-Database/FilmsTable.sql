USE [StudioGhibli]
GO

/****** Object:  Table [dbo].[Films]    Script Date: 02/06/2016 14:11:27 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[Films](
	[Title] [varchar](75) NOT NULL,
	[Director] [varchar](30) NULL,
	[Rating] [varchar](10) NULL,
	[Duration] [varchar](20) NULL,
	[ReleaseDate] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[Title] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO


