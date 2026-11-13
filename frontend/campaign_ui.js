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

function renderCampaignMetrics(data) {
    document.getElementById("metrics").innerHTML =
        `<p>${data.views}</p>`;
}

function cacheMetrics(data) {
    sessionStorage.setItem(
        "campaignMetrics",
        JSON.stringify(data)
    );
}

function renderCampaignBanner(data) {
    document.getElementById("banner").innerHTML = `
        <div class="campaign-banner">
            <h2>${data.title}</h2>
            <p>${data.tagline}</p>
        </div>
    `;
}

function renderCampaignAudience(data) {
    document.getElementById("audience").innerHTML = `
        <p>Target Audience: ${data.segment}</p>
    `;
}

function renderCampaignPerformance(data) {
    document.getElementById("performance").innerHTML = `
        <p>Views: ${data.views}</p>
        <p>Clicks: ${data.clicks}</p>
    `;
}

function renderCampaignSummary(metrics) {
    const container = document.getElementById("campaign-summary");
    if (!container) return;

    container.innerHTML = `
        <div class="summary-card">
            <h3>Total Campaigns</h3>
            <p>${metrics.total_campaigns}</p>
        </div>
        <div class="summary-card">
            <h3>Active Campaigns</h3>
            <p>${metrics.active_campaigns}</p>
        </div>
        <div class="summary-card">
            <h3>Total Clicks</h3>
            <p>${metrics.total_clicks}</p>
        </div>
    `;
}