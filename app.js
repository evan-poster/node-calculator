const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());

app.get('/', (req, res) => {
	res.json({ message: 'Hello from the backend!' });
});

// Adds two numbers and returns the result
app.get('/add', (req, res) => {
	const { n1, n2 } = req.query;
	const num1 = Number(n1);
	const num2 = Number(n2);
	if (isNaN(num1) || isNaN(num2)) {
		res.status(400).json({
			error: 'Both n1 and n2 must be numbers.'
		});
		return;
	}
	const result = num1 + num2;
	res.json({ result });
});

// Subtracts two numbers and returns the result
app.get('/subtract', (req, res) => {
	const { n1, n2 } = req.query;
	const num1 = Number(n1);
	const num2 = Number(n2);
	if (isNaN(num1) || isNaN(num2)) {
		res.status(400).json({
			error: 'Both n1 and n2 must be numbers.'
		});
		return;
	}
	const result = num1 - num2;
	res.json({ result });
});

// Multiplies two numbers and returns the result
app.get('/multiply', (req, res) => {
	const { n1, n2 } = req.query;
	const num1 = Number(n1);
	const num2 = Number(n2);
	if (isNaN(num1) || isNaN(num2)) {
		res.status(400).json({
			error: 'Both n1 and n2 must be numbers.'
		});
		return;
	}
	const result = num1 * num2;
	res.json({ result });
});

// Divides two numbers and returns the result
app.get('/divide', (req, res) => {
	const { n1, n2 } = req.query;
	const num1 = Number(n1);
	const num2 = Number(n2);
	if (isNaN(num1) || isNaN(num2)) {
		res.status(400).json({
			error: 'Both n1 and n2 must be numbers.'
		});
		return;
	}
	if (num2 === 0) {
		res.status(400).json({
			error: 'Cannot divide by zero.'
		});
		return;
	}
	const result = num1 / num2;
	res.json({ result });
});

// Returns n1 to the power of n2
app.get('/power', (req, res) => {
	const { n1, n2 } = req.query;
	const num1 = Number(n1);
	const num2 = Number(n2);
	if (isNaN(num1) || isNaN(num2)) {
		res.status(400).json({
			error: 'Both n1 and n2 must be numbers.'
		});
		return;
	}
	const result = Math.pow(num1, num2);
	res.json({ result });
});

// Returns root of n1
app.get('/root', (req, res) => {
	const { n1 } = req.query;
	const num1 = Number(n1);
	if (isNaN(num1)) {
		res.status(400).json({
			error: 'n1 must be a number.'
		});
		return;
	}
	if (num1 < 0) {
		res.status(400).json({
			error: 'n1 must be a positive number.'
		});
		return;
	}
	const result = Math.sqrt(num1);
	res.json({ result });
});

// Returns square of n1
app.get('/square', (req, res) => {
	const { n1 } = req.query;
	const num1 = Number(n1);
	if (isNaN(num1)) {
		res.status(400).json({
			error: 'n1 must be a number.'
		});
		return;
	}
	const result = Math.pow(num1, 2);
	res.json({ result });
});


const PORT = process.env.PORT || 3000;
if (process.env.NODE_ENV !== 'production') {
  app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
  });
}

module.exports = app;
