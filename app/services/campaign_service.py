campaigns = []

def add_campaign(name, budget):

    campaign = {
        "name": name,
        "budget": budget
    }

    campaigns.append(campaign)

    return campaign

def fetch_campaigns():
    return db.query("SELECT * FROM campaigns WHERE active=1")