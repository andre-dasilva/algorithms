package interpreter

import "testing"

func testStack(t *testing.T) {
	stack := NewStack[int]()
	stack.Push(2)
	stack.Push(3)

	size := len(stack.store)
	if size != 2 {
		t.Errorf("Should have two elements in stack")
	}

	value := stack.Pop()
	if value != 3 {
		t.Errorf("Last value should be 3")
	}
	newSize := len(stack.store)
	if newSize != 1 {
		t.Errorf("Now there should be only one element")
	}
}
