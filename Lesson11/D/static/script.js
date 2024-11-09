const Celsius = document.getElementById('c-input');
const DisplayResult = document.getElementById('result-p')
const Form = document.getElementById('frm');


async function convertCelsiusToFahrenheit(celsius){
    const response = await fetch(`/convert_celsius_to_fahrenheit?celsius=${celsius}`);
    const data = await response.json();
    console.log(data);
    let degrees = '\u00B0';
    if (data.fahrenheit == 'ERROR'){
        alert(`Error, ${celsius} is not a number!`);
    } else {
        DisplayResult.textContent = `Temperature to Fahrenheit ${data.fahrenheit}${degrees}F`;
    }
}

Form.addEventListener('submit', function (event) {
    console.log('Celsius value is submitted!');
    event.preventDefault();
    const celsius = Celsius.value;
    console.log(`Convert '${celsius}' from celsius to fahrenheit`);
    answer = convertCelsiusToFahrenheit(celsius);
});