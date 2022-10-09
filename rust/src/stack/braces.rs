use std::collections::HashMap;

use crate::stack::stack::Stack;

pub struct PairMatcher<T, I>
where
    T: PartialEq,
    I: Iterator<Item = T>,
{
    pairs: HashMap<T, T>,
    search_input: I,
}

impl<T, I> PairMatcher<T, I>
where
    T: PartialEq,
    I: Iterator<Item = T>,
{
    pub fn new(pairs: HashMap<T, T>, search_input: I) -> Self {
        Self {
            pairs,
            search_input,
        }
    }

    pub fn count_pairs(self) -> isize {
        let mut stack = Stack::new();
        let mut counter = 0;

        let left_elements = Vec::from_iter(self.pairs.keys());
        let right_elements = Vec::from_iter(self.pairs.values());

        for element in self.search_input {
            if left_elements.contains(&&element) {
                stack.push(element)
            } else if right_elements.contains(&&element) {
                match stack.pop() {
                    Some(_) => counter += 1,
                    None => return -1,
                }
            }        
        }

        if !stack.empty() {
            return -1;
        }
        counter
    }

    pub fn has_matching_pairs(self) -> bool {
        self.count_pairs() != -1 
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_simple_str_match() {
        let pairs = HashMap::from([('{', '}')]);
        let pair_matcher = PairMatcher::new(pairs, "{}{}".chars());
        assert_eq!(pair_matcher.count_pairs(), 2)
    }

    #[test]
    fn test_simple_int_match() {
        let pairs = HashMap::from([(1, 2)]);
        let pair_matcher = PairMatcher::new(pairs, vec![1, 2, 3, 4, 5, 1, 2, 56, 1, 2].into_iter());
        assert_eq!(pair_matcher.count_pairs(), 3)
    }

    #[test]
    fn test_failed_match() {
        let pairs = HashMap::from([(1, 2)]);
        let pair_matcher = PairMatcher::new(pairs, vec![1, 2, 3, 4, 5, 1, 2, 56, 1].into_iter());
        assert!(!pair_matcher.has_matching_pairs())
    }

    #[test]
    fn test_complex_match() {
        let pairs = HashMap::from([('{', '}')]);
        let pair_matcher = PairMatcher::new(pairs, "{{{{{{{{}{}{}{}{}{{}}}}}}}}{}{}{}}".chars());
        assert!(pair_matcher.has_matching_pairs())
    }
}

