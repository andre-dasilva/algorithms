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
                int compare = string.Compare(p1.FirstName, p2.FirstName, System.StringComparison.CurrentCulture);
                if (compare == 0)
                {
                    return string.Compare(p1.LastName, p2.LastName, System.StringComparison.CurrentCulture);
                }
                return compare;
            });
        }

        [TestMethod]
        public void TestUserFirstNameIsInList()
        {
            bool value = BinarySearch.Execute(people, (p) => string.Compare(p.FirstName, "Patrick", System.StringComparison.CurrentCulture));
            Assert.IsTrue(value);
        }

        [TestMethod]
        public void TestUserFirstNameIsNotInList()
        {
            bool value = BinarySearch.Execute(people, (p) => string.Compare(p.FirstName, "Carl", System.StringComparison.CurrentCulture));
            Assert.IsFalse(value);
        }
    }
}
