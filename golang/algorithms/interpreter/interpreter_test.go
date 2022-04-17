package interpreter

import "testing"

func TestPolishCalculation(t *testing.T) {
	testCases := []struct {
		text string
		want int
	}{
		{text: "2 3 +", want: 5},
		{text: "2 3 + 5 +", want: 10},
		{text: "2 3 + 10 *", want: 50},
	}

	for _, tc := range testCases {
		t.Run(tc.text, func(t *testing.T) {
			if got := Calculate(tc.text); got != tc.want {
				t.Errorf("got %v; want %v", got, tc.want)
			}
		})
	}
}
