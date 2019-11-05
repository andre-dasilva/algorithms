namespace Algorithms
{
    public static class Palindrome
    {
        public static bool Execute(string word)
        {
            string lowerCaseWord = word.ToLower();
            for (int index = 0; index < lowerCaseWord.Length; index++)
            {
                int reverseIndex = (lowerCaseWord.Length - 1) - index;
                if (reverseIndex <= index)
                {
                    break;
                }
                if (lowerCaseWord[index] != lowerCaseWord[reverseIndex])
                {
                    return false;
                }
            }
            return true;
        }
    }
}