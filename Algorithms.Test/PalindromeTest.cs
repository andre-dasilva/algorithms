using Microsoft.VisualStudio.TestTools.UnitTesting;
using System.Collections.Generic;
using Algorithms.Models;

namespace Algorithms.Test
{
    [TestClass]
    public class PalindromeTest
    {
        [TestMethod]
        public void TestPalindromeTrue()
        {
            string palindrome = "anna";
            Assert.IsTrue(Palindrome.Execute(palindrome));
        }

        [TestMethod]
        public void TestPalindromeFalse()
        {
            string palindrome = "hans";
            Assert.IsFalse(Palindrome.Execute(palindrome));
        }

        [TestMethod]
        public void TestListOfPalidroms()
        {
            List<string> testWords = new List<string>()
            {
                "civic",
                "deified",
                "deleveled",
                "devoved",
                "dewed",
                "Hannah",
                "kayak",
                "level",
                "madam",
                "racecar",
                "radar",
                "redder",
                "refer",
                "repaper",
                "reviver",
                "rotator",
                "rotor",
                "sagas",
                "solos",
                "sexes",
                "stats",
                "tenet",
            };

            foreach (string word in testWords)
            {
                Assert.IsTrue(Palindrome.Execute(word));
            }
        }
    }
}
