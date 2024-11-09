const Form = document.getElementById('frm');
const Results = document.getElementById('result-p');


async function logFeedBack(uname, email, comments){
    console.log("logging user feedback");
    const response = await fetch(`/log_feedback?user=${uname}&email=${email}&feedback=${comments}`);
    const data = response.json();
    console.log(data);
}

async function validateEmail(uname, email, comments) {
    console.log("validating email");
    const response = await fetch(`/validate_email?email=${email}`);
    const data = await response.json();
    console.log(data);

    if (String(data.status) == 'Email is NOT VALID'){
        alert(`Please enter a valid email address!`);
    } else {
        console.log(`logging user- ${uname},email- ${email}, feedback- ${comments}`);
        Results.textContent = `Thank you, your feedback is appreciated!`;
        logFeedBack(uname, email, comments);
    }
}

Form.addEventListener("submit", function(event){
    event.preventDefault();
    const uname = document.getElementById('uname').value;
    const email = document.getElementById('email').value;
    const comments = document.getElementById('comments').value;
    validateEmail(uname, email, comments);
});