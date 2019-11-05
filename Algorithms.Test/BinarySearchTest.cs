using Microsoft.VisualStudio.TestTools.UnitTesting;
using System.Collections.Generic;
using Algorithms.Models;

namespace Algorithms.Test
{
    [TestClass]
    public class BinarySearchTest
    {
        private List<Person> people = new List<Person>();

        [TestInitialize]
        public void Setup()
        {
            people = new List<Person>()
            {
                new Person() { FirstName = "Hans", LastName = "Müller" },
                new Person() { FirstName = "André", LastName = "da Silva" },
                new Person() { FirstName = "Patrick", LastName = "Rossi" },
                new Person() { FirstName = "Philipp", LastName = "Schneider" },
                new Person() { FirstName = "Gert", LastName = "Richard" },
                new Person() { FirstName = "Patrick", LastName = "Gubler" },
                new Person() { FirstName = "Biance", LastName = "Huber" },
                new Person() { FirstName = "Carlos", LastName = "Vega" }
            };

            people.Sort((p1, p2) =>
            {
                int compare = p1.FirstName.CompareTo(p2.FirstName);
                if (compare == 0)
                {
                    return p1.LastName.CompareTo(p2.LastName);
                }
                return compare;
            });
        }

        [TestMethod]
        public void TestUserFirstNameIsInList()
        {
            bool value = BinarySearch.Execute(people, (p) => p.FirstName.CompareTo("Patrick"), 0, people.Count - 1);
            Assert.IsTrue(value);
        }

        [TestMethod]
        public void TestUserFirstNameIsNotInList()
        {
            bool value = BinarySearch.Execute(people, (p) => p.FirstName.CompareTo("Thomas"), 0, people.Count - 1);
            Assert.IsFalse(value);
        }
    }
}
