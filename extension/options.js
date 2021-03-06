//js for options page
var email = document.getElementById('email');
var nname = document.getElementById('name');
var phone = document.getElementById('phone');
var zip = document.getElementById('zip');
var address = document.getElementById('address');
var template = document.getElementById('file');
var button = document.getElementById('save');
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
            zip: '',
            template: ''
        };
    };
    document.getElementById('email').value = newOptions['email'];
    document.getElementById('name').value = newOptions['name'];
    document.getElementById('phone').value = newOptions['phone'];
    document.getElementById('zip').value = newOptions['zip'];
    document.getElementById('address').value = newOptions['address'];
});

const zero = 0n
const shift = 8n

function asciiToBinary(str) {
    const len = str.length
    let n = zero
    for (let i = 0; i < len; i++) {
        n = (n << shift) + BigInt(str.charCodeAt(i))
    }
    return n.toString(2).padStart(len * 8, 0)
}

button.addEventListener('click', async function () {
    newOptions['email'] = email.value;
    newOptions['name'] = nname.value;
    newOptions['phone'] = phone.value;
    newOptions['address'] = address.value;
    newOptions['zip'] = zip.value;

    // try {
    //     let terriblecodinghabitvariable = await template.files[0]
    //     console.log(terriblecodinghabitvariable)
    //     fetch("http://localhost:25565/savetemplate", {
    //         method: "POST",
    //         mode: 'no-cors',
    //         body: await template.files[0]
    //     }).then(out => {
    //         console.log(out)
    //         console.log('sent template')
    //     });
    // } catch (TypeError) {
    //     console.log('no template')
    // }

    // console.log(newOptions['template'])
    chrome.storage.local.set({
        options: { ...newOptions }
    }, () => console.log(newOptions));
});
