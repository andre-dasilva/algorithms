#[derive(Default)]
pub struct Stack<T> {
    elements: Vec<T>,
}

impl<T> Stack<T> {
    pub fn new() -> Self {
        Self { elements: vec![] }
    }

    pub fn pop(&mut self) -> Option<T> {
        self.elements.pop()
    }

    pub fn push(&mut self, element: T) {
        self.elements.push(element)
    }

    pub fn empty(&self) -> bool {
        self.elements.is_empty()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_push() {
        let mut stack = Stack::new();
        stack.push(1);
        stack.push(2);
        stack.push(3);

        assert_eq!(stack.elements, vec![1, 2, 3]);
    }

    #[test]
    fn test_pop() {
        let mut stack = Stack::new();
        stack.push(1);
        stack.push(2);
        stack.push(3);

        let three = stack.pop();
        assert_eq!(three, Some(3));
    }
}
