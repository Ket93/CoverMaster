
var posting = document.querySelector("body > main > div.orbisModuleHeader > div > div > div:nth-child(1) > table > tbody > tr:nth-child(1) > td:nth-child(2) > span").innerText
//const url = "http://localhost:25565/submit"
console.log("Running cover letter script")
if (posting === 'Approved') {
    const url = "https://34.130.223.251:25565/submit"
    var companyName = document.getElementsByClassName("table table-bordered")[3].rows[0].cells[1];
    var companyDivision = document.getElementsByClassName("table table-bordered")[3].rows[1].cells[1];
    var jobAddress = document.getElementsByClassName("np-view-question--18")[0];
    // var jobCity = document.getElementsByClassName("np-view-question--20")[0];
    var jobProvince = document.getElementsByClassName("np-view-question--21")[0];
    var jobCountry = document.getElementsByClassName("np-view-question--23")[0];
    var jobPostal = document.getElementsByClassName("np-view-question--22")[0];
    var scrapedData = {
        companyName: companyName.innerText || companyName.textContent,
        companyDivision: companyDivision.innerText || companyDivision.textContent,
        jobAddress: jobAddress.innerText || jobAddress.textContent,
        // jobCity: jobCity.innerText || jobCity.textContent,
        jobProvince: jobProvince.innerText || jobProvince.textContent,
        jobCountry: jobCountry.innerText || jobCountry.textContent,
        jobPostal: jobPostal.innerText || jobPostal.textContent
    };
    chrome.runtime.sendMessage({
        message: 'test_url',
        data: scrapedData
    }, response => updateBackground(response.html))
    
};
