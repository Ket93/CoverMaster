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

//when a message is sent from another script, it goes through this listener
// chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
//   if (request.message === 'test_url') {
//     chrome.tabs.query({ active: true, lastFocusedWindow: true }, tabs => {
//       const url = "http://http://34.130.223.251:25565/submit"
//       var companyName = document.getElementsByClassName("table table-bordered")[3].rows[0].cells[1];
//       var companyDivision = document.getElementsByClassName("table table-bordered")[3].rows[1].cells[1];
//       var jobAddress = document.getElementsByClassName("np-view-question--18")[0];
//       var jobCity = document.getElementsByClassName("np-view-question--20")[0];
//       var jobProvince = document.getElementsByClassName("np-view-question--21")[0];
//       var jobCountry = document.getElementsByClassName("np-view-question--23")[0];
//       var jobPostal = document.getElementsByClassName("np-view-question--22")[0];

//       //const url = "http://localhost:25565/submit"
//       fetch(url, {
//         method: "POST",
//         body: JSON.stringify({ url: tabs[0]['url'] })
//       }).then(response => response.text()).then(coverletterSITE => {
//         //open coverlettersite
//       });
//     });
//   };
//   return true;
// });


