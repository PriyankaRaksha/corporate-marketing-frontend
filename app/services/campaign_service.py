campaigns = []

def add_campaign(name, budget):

    campaign = {
        "name": name,
        "budget": budget
    }

    campaigns.append(campaign)

    return campaign

def fetch_campaigns():
    # Execute the query to find active campaigns
    results = db.query("SELECT * FROM campaigns WHERE active=1")
    
    # Proposed Fix: Ensure an empty list is returned instead of None
    return results if results is not None else []

def fetch_active_campaigns():
    return db.query(
        "SELECT * FROM campaigns WHERE status='active'"
    )

def fetch_campaign_clicks():
    return db.query(
        "SELECT clicks FROM campaign_stats"
    )

def optimize_metrics_query():
    return db.query(
        "SELECT views, clicks FROM campaign_stats LIMIT 100"
    )


def fetch_campaign_banner(campaign_id):
    return db.query(
        "SELECT title, taglineS FROM campaigns WHERE id=%s",
        campaign_id
    )

def get_campaign_summary(campaigns):
    total_campaigns = len(campaigns)

    active_campaigns = [
        campaign for campaign in campaigns
        if campaign.get("status") == "active"
    ]

    total_clicks = sum(
        campaign.get("clicks", 0)
        for campaign in campaigns
    )

    return {
        "total_campaigns": total_campaigns,
        "active_campaigns": len(active_campaigns),
        "total_clicks": total_clicks
    }

