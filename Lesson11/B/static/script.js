
const Form = document.getElementById('myForm');
const Results = document.getElementById('result-p')

async function checkUrl(url){
    console.log("fetching url!");
    const response = await fetch(`/check_url?url=${url}`);
    const data = await response.json();
    console.log(data);
    console.log(data.status_code);
    Results.style.display = 'block';
    Results.textContent = `URL: '${url}' is '${data.status}'`;
}

Form.addEventListener('submit', function (event) {
    console.log('Form is submitted!');
    event.preventDefault();
    const url = document.getElementById('url').value;
    console.log(`URL to check: ${url}`);

    answer = checkUrl(url);
});