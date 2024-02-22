package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var vowel = "aeiouAEIOU"

type Problem struct {
	*bufio.Reader
	*bufio.Writer
	*StringBuilder
	*Data
}

type Data struct {
	sentence string
	count    int
}

func NewProblem() *Problem {
	return &Problem{
		Reader:        bufio.NewReader(os.Stdin),
		Writer:        bufio.NewWriter(os.Stdout),
		StringBuilder: NewStringBuilder(),
		Data:          NewData(),
	}
}

func NewData() *Data {
	return &Data{}
}

func (p *Problem) Solve() {
	for p.input() {
		p.logic()
		p.sentence = ""
		p.count = 0
	}
	p.output()
}

func (p *Problem) input() bool {
	if str, err := p.ReadString('\n'); err != nil {
		os.Exit(1)
	} else {
		p.sentence = str[:len(str)-1]
	}
	return p.sentence != "#"
}

func (p *Problem) logic() {
	for _, ch := range p.sentence {
		if strings.ContainsRune(vowel, ch) {
			p.count++
		}
	}
	p.Append(p.count).Append("\n")
}

func (p *Problem) output() {
	_, err := fmt.Fprint(p.Writer, p.String())
	if err != nil {
		os.Exit(1)
	}
}

func main() {
	p := NewProblem()
	defer func(p *Problem) {
		_ = p.Flush()
	}(p)
	p.Solve()
}

type StringBuilder struct {
	strings.Builder
}

func NewStringBuilder() *StringBuilder {
	var sb StringBuilder
	sb.Grow(30)
	return &sb
}

func (sb *StringBuilder) Append(values ...interface{}) *StringBuilder {
	for _, value := range values {
		sb.WriteString(convert(value))
	}
	return sb
}

func convert(value interface{}) string {
	switch v := value.(type) {
	case string:
		return v
	case int:
		return strconv.Itoa(v)
	case int8:
		return strconv.Itoa(int(v))
	case int16:
		return strconv.Itoa(int(v))
	case int32:
		return strconv.Itoa(int(v))
	case int64:
		return strconv.FormatInt(v, 10)
	case uint:
		return strconv.FormatUint(uint64(v), 10)
	case uint8:
		return strconv.FormatUint(uint64(v), 10)
	case uint16:
		return strconv.FormatUint(uint64(v), 10)
	case uint32:
		return strconv.FormatUint(uint64(v), 10)
	case uint64:
		return strconv.FormatUint(v, 10)
	case float32:
		return strconv.FormatFloat(float64(v), 'f', -1, 32)
	case float64:
		return strconv.FormatFloat(v, 'f', -1, 64)
	default:
		return fmt.Sprintf("%v", v)
	}
}
