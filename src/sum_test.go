package sum

import "testing"

func Testsum(t *testing.T) {
	const in1, in2, out = 2, 3, 5
	if x := Sum(in1, in2); x != out {
		t.Errorf("Error!!")
	}
}