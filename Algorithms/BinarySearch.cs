using System;
using System.Collections.Generic;

namespace Algorithms
{
    public static class BinarySearch
    {
        public static bool Execute<T>(List<T> list, Func<T, int> predicate)
        {
            return Execute(list, predicate, 0, list.Count - 1);
        }

        public static bool Execute<T>(List<T> list, Func<T, int> predicate, int low, int high)
        {
            if (low > high)
            {
                return false;
            }
            int middle = (low + high) / 2;
            if (predicate.Invoke(list[middle]) == 1)
            {
                return Execute(list, predicate, low, middle - 1);
            }
            else if (predicate.Invoke(list[middle]) == -1)
            {
                return Execute(list, predicate, middle + 1, high);
            }
            return true;
        }
    }
}
