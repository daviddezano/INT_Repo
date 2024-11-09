
const Form = document.getElementById('frm');
const Results = document.getElementById('result-p');

async function Calc(ops, num1, num2){
    console.log("fetching calculation");
    const response = await fetch(`/calculate?operation=${ops}&num1=${num1}&num2=${num2}`);
    const data = await response.json();
    console.log(data);
    console.log(data.status_code);
    Results.style.display = 'block';
    Results.textContent = `Result: ${data.result}`;
}

Form.addEventListener('submit', function (event) {
    console.log('Form is submitted!');
    event.preventDefault();
    const num1 = document.getElementById('num1').value;
    const num2 = document.getElementById('num2').value;
    const option = document.getElementById('operation').value;
    console.log(`Num1(${num1}), Num2(${num2}) Option(${option})`);
    Calc(option, num1, num2);
});