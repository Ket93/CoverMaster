
// var posting = document.querySelector("body > main > div.orbisModuleHeader > div > div > div:nth-child(1) > table > tbody > tr:nth-child(1) > td:nth-child(2) > span").innerText
console.log("Running cover letter script")
if (true) {
    // const url = "https://34.130.223.251:25565/submit"
    const url = "http://localhost:25565/submit"

    var companyName = document.getElementsByClassName("table table-bordered")[3].rows[0].cells[1];
    var companyDivision = document.getElementsByClassName("table table-bordered")[3].rows[1].cells[1];
    var jobAddress = document.getElementsByClassName("np-view-question--18")[0];
    var jobCity = document.getElementsByClassName("np-view-question--20")[0];
    var jobProvince = document.getElementsByClassName("np-view-question--21")[0];
    var jobCountry = document.getElementsByClassName("np-view-question--23")[0];
    var jobPostal = document.getElementsByClassName("np-view-question--22")[0];
    var jobSummary = document.getElementsByClassName("np-view-question--29")[0];
    var jobResp = document.getElementsByClassName("np-view-question--30")[0];
    var requiredSkills = document.getElementsByClassName("np-view-question--31")[0];
    var scrapedData = {
        companyName: '',
        companyDivision: '',
        jobAddress: '',
        jobCity: '',
        jobProvince: '',
        jobCountry: '',
        jobPostal: '',
        jobSummary: '',
        jobResp: '',
        requiredSkills: ''
    };
    try {
        scrapedData['companyName'] = companyName.innerText || companyName.textContent
        scrapedData['companyDivision'] = companyDivision.innerText || companyDivision.textContent
        scrapedData['jobAddress'] = jobAddress.innerText || jobAddress.textContent
        scrapedData['jobCity'] = jobCity.innerText || jobCity.textContent
        scrapedData['jobProvince'] = jobProvince.innerText || jobProvince.textContent
        scrapedData['jobCountry'] = jobCountry.innerText || jobCountry.textContent
        scrapedData['jobPostal'] = jobPostal.innerText || jobPostal.textContent
        scrapedData['jobSummary'] = jobSummary.innerText || jobSummary.textContent
        scrapedData['jobResp'] = jobResp.innerText || jobResp.textContent
        scrapedData['requiredSkills'] = requiredSkills.innerText || requiredSkills.textContent
    } catch (TypeError) {
        console.log(scrapedData);
    }

    console.log('saved something')
    chrome.storage.local.get(['options'], function (result) { // users' options from options page (email, name, etc.)
        console.log('Value is: ', result.options)
        fetch(url, {
            method: "POST",
            mode: 'no-cors',
            body: JSON.stringify({ ...scrapedData, ...result.options })
        }).then(out => {
            console.log(out)
            console.log('recieved something?')
        });
    });
};
