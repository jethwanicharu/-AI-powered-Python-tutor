document.getElementById('ask_button').onclick = function() {
    const userInput = document.getElementById('user_input').value;
    fetch('/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'user_input': userInput
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerText = data.response;
    });
};