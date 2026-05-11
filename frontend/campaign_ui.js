function renderCampaign(data) {
    document.getElementById("root").innerHTML = `
        <section class="campaign-card">
            <h1>${data.title}</h1>
            <p>${data.description}</p>
            <button onclick="trackClick()">Join</button>
        </section>
    `;
}

function showCampaignStats(data) {
    document.getElementById("stats").innerHTML = `
        <p>Total Clicks: ${data.clicks}</p>
    `;
}