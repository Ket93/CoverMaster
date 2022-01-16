//This script runs ONE time at the start of the function
//if you go into your 'extensions' page on chrome there should be a 'background page' that you can click on, the console will go to this
console.log("Running")

// // sets the local storage with address 'teststorage' to 'test' 
// chrome.storage.local.set({
//   teststorage: 'test'
// });

// //gets the local storage from 'teststorage' and prints it to the console
// chrome.storage.local.get(['teststorage'], function (result) {
//   console.log('Value is: ', result.teststorage)
// });

// when a message is sent from another script, it goes through this listener
// chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
//     if (request.message === 'test_url') {
//         const url = "https://34.130.223.251:25565/submit"
//         console.log('sent something')
//         fetch(url, {
//             method: "POST",
//             body: JSON.stringify(request.data)
//         }).then(response => response.text()).then(coverletterSITE => {
//             //open coverlettersite
//         });
//     };
//     return true;
// });


