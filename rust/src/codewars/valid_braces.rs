pub fn valid_braces(s: &str) -> bool {
    let mut stack = Vec::new();
    
    for c in s.chars() {
        if c == '{' || c == '(' || c == '[' {
            stack.push(c);
        } else {
            let latest = match stack.pop() {
                Some(x) => x,
                None => return false
            };
            if latest == '{' && c != '}' || latest == '(' && c != ')' || latest == '[' && c != ']' {
                return false;
            }
        }
    }
    
    if stack.is_empty() {
        return true;
    }     
    return false;
}


#[cfg(test)]
mod tests {
    use super::*; 

    #[test]
    fn basic_tests() {
        expect_true("()");
        expect_false("[(])");
    }
    
    fn expect_true(s: &str) {
        assert!(valid_braces(s), "Expected {s:?} to be valid. Got false", s=s);
    }
    
    fn expect_false(s: &str) {
        assert!(!valid_braces(s), "Expected {s:?} to be invalid. Got true", s=s);
    }
}
