// Join written out :-). I know slices have a .join method
fn join(arr: &[&str]) -> String {
    let mut joined = String::new();

    let mut delimiter = "";
    for a in arr {
        joined.push_str(delimiter);
        joined.push_str(a);
        delimiter = " ";
    }
    joined
}

pub fn part_list(arr: Vec<&str>) -> String {
    let mut result = String::new();

    for i in 0..arr.len() - 1 {
        let start = &arr[..i + 1];
        let end = &arr[i + 1..];

        let line = format!("({}, {})", join(start), join(end));
        result.push_str(&line);
    }
    result
}

#[cfg(test)]
mod tests {
    use super::*;

    fn dotest(arr: Vec<&str>, exp: &str) {
        println!("arr: {:?}", arr);
        let ans = part_list(arr);
        println!("actual:\n{}", ans);
        println!("expect:\n{}", exp);
        println!("{}", ans == exp);
        assert_eq!(ans, exp);
        println!("-");
    }

    #[test]
    fn basis_tests() {
        dotest(vec!["I", "wish", "I", "hadn't", "come"],
                "(I, wish I hadn't come)(I wish, I hadn't come)(I wish I, hadn't come)(I wish I hadn't, come)");
        dotest(
            vec!["cdIw", "tzIy", "xDu", "rThG"],
            "(cdIw, tzIy xDu rThG)(cdIw tzIy, xDu rThG)(cdIw tzIy xDu, rThG)",
        );
    }
}
