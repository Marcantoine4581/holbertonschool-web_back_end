function calculateNumber(type, a, b) {
    if (type == 'SUM') {
        return Math.round(a) + Math.round(b)
    }
    if (type == 'SUBTRACT') {
        return Math.round(a) - Math.round(b)
    }
    if (type == 'DIVIDE') {
        if (b == 0) {
            return 'Error'
        }
        return Math.round(a) / Math.round(b)
    }
}

module.exports = calculateNumber;

// console.log(calculateNumber('ADD', 20.15, 10.20))
// console.log(calculateNumber('DIVIDE', 20, 0))
