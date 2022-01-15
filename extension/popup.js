//js for the popup
let resultDiv = document.getElementById('result');
let background = document.getElementById('body');

function startUp() {
    resultDiv.innerHTML = 'Analyzing page...'
    chrome.runtime.sendMessage({
        message: 'test_url'
    }, response => updateBackground(response.html))
};

function updateBackground(info) {
    resultDiv.innerHTML = info
    if (info == 'Reliable') {
        background.classList.add('success')
    } else {
        background.classList.add('bad')
    };

    // chrome.storage.local.set({
    //     teststorage: info
    // });
    //sends message to the 'onMessage' listener in background.js
    // chrome.runtime.sendMessage({
    //     message: 'storage updated'
    // }, html => updateBackground(html));
}

startUp();
