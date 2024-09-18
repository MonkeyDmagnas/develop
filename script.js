const display = document.getElementById('display');
const buttons = document.querySelectorAll('button');

let currentNumber = '';
let previousNumber = '';
let operator = '';

buttons.forEach(button => {
  button.addEventListener('click', () => {
    const value = button.value;

    if (value === 'C') {
      currentNumber = '';
      previousNumber = '';
      operator = '';
      display.value = '';
    } else if (value === '=') {
      const result = eval(`${previousNumber} ${operator} ${currentNumber}`);
      display.value = result;
      currentNumber = result.toString();
      previousNumber = '';
      operator = '';
    } else if (['+', '-', '*', '/'].includes(value)) {
      previousNumber = currentNumber;
      currentNumber = '';
      operator = value;
    } else {
      currentNumber += value;
      display.value = currentNumber;
    }
  });
});