function renderCampaign(data) {
    document.getElementById("root").innerHTML = `
        <section class="campaign-card">
            <h1>${data.title}</h1>
            <p>${data.description}</p>
        </section>
    `;
}