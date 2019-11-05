using System;
using System.Collections.Generic;
using Algorithms.Models;

namespace Algorithms
{
    public class BinarySearch
    {
        public static bool Execute(List<Person> people, Func<Person, int> predicate, int low, int high)
        {
            if (low > high)
            {
                return false;
            }
            int middle = (low + high) / 2;
            if (predicate.Invoke(people[middle]) == 1)
            {
                return Execute(people, predicate, low, middle - 1);
            }
            else if (predicate.Invoke(people[middle]) == -1)
            {
                return Execute(people, predicate, middle + 1, high);
            }
            return true;
        }
    }
}
