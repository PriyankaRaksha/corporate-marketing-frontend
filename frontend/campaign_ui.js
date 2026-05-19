function renderCampaign(data) {
    if (!data || data.length === 0) {
        document.getElementById("root").innerHTML =
            "<p>No campaigns available</p>";
        return;
    }

    document.getElementById("root").innerHTML = `
        <h1>${data.title}</h1>
    `;
}

function showCampaignStats(data) {
    document.getElementById("stats").innerHTML = `
        <p>Total Clicks: ${data.clicks}</p>
    `;
}

function enableCampaignTracking() {
    console.log("Tracking enabled");
}

function loadCampaignBanner(title) {
    document.getElementById("banner").innerHTML =
        `<h2>${title}</h2>`;
}