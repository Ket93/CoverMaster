//js for options page
var buttonDiv = document.getElementById('buttondiv');
var email = document.getElementById('email');
var nname = document.getElementById('name');
var phone = document.getElementById('phone');
var newOptions = null
chrome.storage.local.get(['options'], function (result) {
    console.log('old options: ', result.options);
    newOptions = result.options;
    if (newOptions === undefined) {
        newOptions = {
            email: '',
            name: '',
            phone: ''
        };
    };
    document.getElementById('email').value = newOptions['email'];
    document.getElementById('name').value = newOptions['name'];
    document.getElementById('phone').value = newOptions['phone'];
});

function constructButtons(div) {
    let button = document.createElement('button');
    button.innerText = "save";
    button.addEventListener('click', function () {
        newOptions['email'] = email.value;
        newOptions['name'] = nname.value;
        newOptions['phone'] = phone.value;
        chrome.storage.local.set({
            options: { ...newOptions }
        }, () => console.log(newOptions));
    });
    buttonDiv.appendChild(button);
}




constructButtons(buttonDiv);
