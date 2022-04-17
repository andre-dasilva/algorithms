package interpreter

type Stack[T any] struct {
	store []T
}

func (s *Stack[T]) Push(i T) {
	s.store = append(s.store, i)
}

func (s *Stack[T]) Pop() T {
	length := len(s.store)

	var value T

	if length > 0 {
		value = s.store[length-1]
		s.store = s.store[:length-1]
		return value
	}
	return value
}

func NewStack[T any]() *Stack[T] {
	return &Stack[T]{
		store: nil,
	}
}
