function calculateNumber(a, b) {
    let round_a = Math.round(a);
    let round_b = Math.round(b);
    return round_a + round_b
}

module.exports = calculateNumber;