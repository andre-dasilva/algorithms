pub fn insertion_sort(elements: &mut [i32]) {
    for i in 1..elements.len() {
        let mut j = i;
        while j > 0 && elements[j - 1] > elements[j] {
            elements.swap(j - 1, j);
            j -= 1;
        }
    } 
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_insertion_sort() {
        let mut actual = vec![5, 2, 4, 6, 1, 3];
        insertion_sort(&mut actual);

        let expect = vec![1, 2, 3, 4, 5, 6];
        assert_eq!(actual, expect);
    }
}
