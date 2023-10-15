export default function divideFunction(numerator, denominator) {
	if (numerator === 0 || denominator === 0) {
		throw Error('cannot divide by 0');
	}
	return numerator / denominator;
}
