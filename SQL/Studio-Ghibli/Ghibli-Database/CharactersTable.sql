USE [StudioGhibli]
GO

/****** Object:  Table [dbo].[Characters]    Script Date: 02/06/2016 14:11:13 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[Characters](
	[Title] [varchar](75) NULL,
	[_Character] [varchar](30) NOT NULL
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO

ALTER TABLE [dbo].[Characters]  WITH CHECK ADD FOREIGN KEY([Title])
REFERENCES [dbo].[Films] ([Title])
GO


