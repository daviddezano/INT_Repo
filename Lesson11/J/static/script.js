const Text = document.getElementById('txt_a');
const Btn = document.getElementById('btn-submit');
const Results = document.getElementById('result-p');
const ResDiv = document.getElementById('result-div');

async function countWords(words){
    console.log("Counting words");
    const response = await fetch(`/count_words?words=${words}`);
    const data = await response.json();
    console.log(`found ${data.status} words`);
    Results.style.display = 'block';
    ResDiv.style.display = 'block';
    Results.textContent = `Counted: ${data.status} words!`;
}

Btn.addEventListener("click", function(event){
    console.log("Text was submitted");
    event.preventDefault();
    const words = Text.value;
    console.log(`text given: ${words}`)
    countWords(words);
});