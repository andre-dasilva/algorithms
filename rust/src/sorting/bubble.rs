pub fn bubble_sort(elements: &mut [i32]) {
    for i in 0..elements.len() {
        for j in 0..elements.len() - i - 1 {
            if elements[j] > elements[j + 1] {
                elements.swap(j, j + 1)
            }
        }
    } 
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_bubble_sort() {
        let mut actual = vec![5, 2, 4, 6, 1, 3];
        bubble_sort(&mut actual);

        let expect = vec![1, 2, 3, 4, 5, 6];
        assert_eq!(actual, expect);
    }
}
