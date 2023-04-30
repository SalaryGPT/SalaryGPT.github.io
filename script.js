async function calculateTakeHomeSalary() {
    const offerLetter = document.getElementById('offerLetter').value;
    const response = await fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ offerLetter })
    });
    const result = await response.json();
    document.getElementById('result').innerHTML = `Your take home monthly amount: ₹${result.takeHomeMonthlyAmount}`;
}
