//js for options page
var email = document.getElementById('email');
var nname = document.getElementById('name');
var phone = document.getElementById('phone');
var zip = document.getElementById('zip');
var address = document.getElementById('address');
var newOptions = null
chrome.storage.local.get(['options'], function (result) {
    console.log('old options: ', result.options);
    newOptions = result.options;
    if (newOptions === undefined) {
        newOptions = {
            email: '',
            name: '',
            phone: '',
            address: '',
            zip: ''
        };
    };
    document.getElementById('email').value = newOptions['email'];
    document.getElementById('name').value = newOptions['name'];
    document.getElementById('phone').value = newOptions['phone'];
    document.getElementById('zip').value = newOptions['zip'];
    document.getElementById('address').value = newOptions['address'];
});

document.getElementById('save').addEventListener('click', function () {
    newOptions['email'] = email.value;
    newOptions['name'] = nname.value;
    newOptions['phone'] = phone.value;
    newOptions['address'] = address.value;
    newOptions['zip'] = zip.value;
    chrome.storage.local.set({
        options: { ...newOptions }
    }, () => console.log(newOptions));
});
