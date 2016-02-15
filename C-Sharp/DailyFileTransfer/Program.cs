using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DailyFileTransfer
{
    class Program
    {
        static void Main(string[] args)
        {
            string desktopPath = Environment.GetFolderPath(Environment.SpecialFolder.Desktop);
            string sourcePath = desktopPath + @"\Orders";
            string destPath = desktopPath + @"\Processed";

            List<string> recentFiles = CheckForRecentFiles(sourcePath);
            CopyRecentFiles(recentFiles, destPath);
        }

        public static List<string> CheckForRecentFiles(string sourcePath)
        {
            string[] allFiles = Directory.GetFiles(sourcePath);
            List<string> modifiedFiles = new List<string>();
            foreach (string eachFile in allFiles)
            {
                if (File.GetLastWriteTime(eachFile) > (DateTime.Now.AddHours(-24)))
                {
                    modifiedFiles.Add(eachFile);
                }
            }
            return modifiedFiles;
        }

        public static string CopyRecentFiles(List<string> recentFiles, string destPath)
        {
            foreach (string recentFile in recentFiles)
            {
                string fileName = Path.GetFileName(recentFile);
                string destFile = Path.Combine(destPath, fileName);
                File.Copy(recentFile, destFile);
            }
            return null;
        }
    }
}
