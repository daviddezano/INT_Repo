

const ClickButton = document.getElementById('btn_clk');

// Change button text to local time
ClickButton.addEventListener('click', function () {
    ClickButton.innerHTML = new Date().toLocaleTimeString();
});

