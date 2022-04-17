package interpreter

import (
	"strconv"
	"strings"
)

type Interpreter interface {
	Calculate() int
}

type value int

func (v *value) Calculate() int {
	return int(*v)
}

const (
	SUM = "+"
	MUL = "*"
)

type operationSum struct {
	Left  Interpreter
	Right Interpreter
}

func (o *operationSum) Calculate() int {
	return o.Left.Calculate() + o.Right.Calculate()
}

type operationMul struct {
	Left  Interpreter
	Right Interpreter
}

func (o *operationMul) Calculate() int {
	return o.Left.Calculate() * o.Right.Calculate()
}

func operatorFactory(o string, left Interpreter, right Interpreter) Interpreter {
	switch o {
	case SUM:
		return &operationSum{
			Left:  left,
			Right: right,
		}
	case MUL:
		return &operationMul{
			Left:  left,
			Right: right,
		}
	}
	return nil
}

func Calculate(text string) int {
	stack := NewStack[Interpreter]()
	operators := strings.Split(text, " ")

	for _, operator := range operators {
		if operator == SUM || operator == MUL {
			right := stack.Pop()
			left := stack.Pop()
			operatorFunc := operatorFactory(operator, left, right)
			res := value(operatorFunc.Calculate())
			stack.Push(&res)
		} else {
			val, err := strconv.Atoi(operator)
			if err != nil {
				panic(err)
			}
			temp := value(val)
			stack.Push(&temp)
		}
	}
	return int(stack.Pop().Calculate())
}
