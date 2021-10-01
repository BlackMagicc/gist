import datetime
import time

"""
Task #1: Get all campaign shopping data with a calculated CPA (cost per
aquisition) greater than 1

The purpose is to get the environment up and running and perform a data
mutation.

1. Data is passed into the function as the first parameter
2. Add a new calculated value to each data object keyed as `cpa`
   a. CPA is Cost (cost) per Aquisition (conversions)
3. Filter the returned data as an array of object to only include the values 
that have a `cpa` greater than 1.
"""
dataForTask1 = [
    {
        "campaignName": "getSingleCampaign:1",
        "cost": 6,
        "impressions": 2,
        "clicks": 3,
        "revenue": 4,
        "conversions": 5
    },
    {
        "campaignName": "getSingleCampaign:2",
        "cost": 6,
        "impressions": 7,
        "clicks": 8,
        "revenue": 9,
        "conversions": 10
    },
    {
        "campaignName": "getSingleCampaign:3",
        "cost": 5,
        "impressions": 4,
        "clicks": 3,
        "revenue": 2,
        "conversions": 1
    }
]

def task1(data=dataForTask1):
    res = []
    for item in data:
        for option in item:
            if option == 'cost':
                cost = item[option]
            elif option == 'conversions':
                acquisition = item[option]
                if acquisition == 0:
                    return []
        cpa = cost / acquisition
        if cpa > 1:
            item['cpa'] = cpa
            res.append(item)
    return res

"""
Task #2: Get the average ROAS (return on ad spend) for each site between a
date range and submit it to the Data Science API

1. Data is passed into the function as the first parameter as an array of
arrays that contain site objects. Start and end date are the second and third
parameter respectively
2. Filter out any campaign data that is outside of the date range
3. Add a new calculated value to each data object keyed as `roas`
   a. ROAS is Return (revenue) on Ad Spend (Cost)
4. Average the ROAS for all campaigns in a site
5. Return a new array of objects that contains each site's id and its average 
ROAS. If there is no data matching or no average ROAS, then don't return any 
information about that site. 
   a. The payload should be shaped as below
     {
       site_id: <SITE_ID>
       average_roas: <AVERAGE_ROAS>
     }
"""
dataForTask2 = [
    [
        {
            "campaignName": "getSingleCampaign:0",
            "cost": 6,
            "siteId": 1,
            "date": "12/31/2019",
            "impressions": 7,
            "clicks": 8,
            "revenue": 9,
            "conversions": 10,
        },
        {
            "campaignName": "getSingleCampaign:1",
            "cost": 6,
            "siteId": 1,
            "date": "01/01/2020",
            "impressions": 7,
            "clicks": 8,
            "revenue": 9,
            "conversions": 10,
        },
        {
            "campaignName": "getSingleCampaign:2",
            "cost": 5,
            "siteId": 1,
            "date": "01/02/2020",
            "impressions": 4,
            "clicks": 3,
            "revenue": 2,
            "conversions": 1,
        },
        {
            "campaignName": "getSingleCampaign:3",
            "cost": 5,
            "siteId": 1,
            "date": "01/03/2020",
            "impressions": 4,
            "clicks": 3,
            "revenue": 0,
            "conversions": 1,
        },
        {
            "campaignName": "getSingleCampaign:4",
            "cost": 10,
            "siteId": 1,
            "date": "01/04/2020",
            "impressions": 11,
            "clicks": 12,
            "revenue": 13,
            "conversions": 14,
        },
    ],
    [
        {
            "campaignName": "getSingleCampaign:0",
            "cost": 6,
            "siteId": 2,
            "date": "01/02/2020",
            "impressions": 7,
            "clicks": 8,
            "revenue": 9,
            "conversions": 10,
        },
        {
            "campaignName": "getSingleCampaign:1",
            "cost": 6,
            "siteId": 2,
            "date": "01/03/2020",
            "impressions": 7,
            "clicks": 8,
            "revenue": 9,
            "conversions": 10,
        },
        {
            "campaignName": "getSingleCampaign:2",
            "cost": 5,
            "siteId": 2,
            "date": "01/04/2020",
            "impressions": 4,
            "clicks": 3,
            "revenue": 2,
            "conversions": 1,
        },
        {
            "campaignName": "getSingleCampaign:3",
            "cost": 5,
            "siteId": 2,
            "date": "01/05/2020",
            "impressions": 4,
            "clicks": 3,
            "revenue": 0,
            "conversions": 1,
        },
        {
            "campaignName": "getSingleCampaign:4",
            "cost": 10,
            "siteId": 2,
            "date": "01/06/2020",
            "impressions": 11,
            "clicks": 12,
            "revenue": 13,
            "conversions": 14,
        },
    ]
]


def task2(siteData=dataForTask2, startDate="01/01/2020", endDate="01/08/2020"):
    our_return = 0
    ad_spend = 0
    fake_siteData = []
    # This for loop will filter any dates outside of the range for us
    for item in siteData:
        for campaign in item:
            for option in campaign:
                if option == 'date':
                    date = campaign[option]
                    new_date = time.strptime(date, "%m/%d/%Y")
                    new_start_date = time.strptime(startDate, "%m/%d/%Y")
                    new_end_date = time.strptime(endDate, "%m/%d/%Y")
                    if new_start_date <= new_date <= new_end_date:
                        fake_siteData.append(campaign)

    site1_count = 0
    site2_count = 0

    # This for loop will grab the total amount of valid id's for only site 1
    # And calculate the avg roa for only site 1
    total_roa = 0
    for campaign in fake_siteData:
        x = True  # Use this variable as a flag to know when to calculate roa
        for option in campaign:
            if option == 'cost':
                ad_spend = campaign[option]
                if ad_spend == 0:
                    return []
            elif option == 'revenue':
                our_return = campaign[option]
            elif option == 'siteId':
                if campaign[option] != 1:
                    x = False
                    break
                else:
                    site1_count += 1
        if x:
            try:
                roa = our_return / ad_spend
                total_roa += roa
            except ZeroDivisionError:
                roa = our_return
    try:
        site1_avg_roa = total_roa / site1_count
        site1_avg_roa = round(site1_avg_roa, 2)
    except ZeroDivisionError:
        site1_avg_roa = 0

    # This for loop will grab the total amount of valid id's for only site 2
    # And calculate the avg roa for only site 2
    total_roa = 0
    for campaign in fake_siteData:
        x = True  # Use this variable as a flag to know when to calculate roa
        for option in campaign:
            if option == 'cost':
                ad_spend = campaign[option]
            elif option == 'revenue':
                our_return = campaign[option]
            elif option == 'siteId':
                if campaign[option] != 2:
                    x = False
                    break
                else:
                    site2_count += 1
        if x:
            roa = our_return / ad_spend
            total_roa += roa

    try:
        site2_avg_roa = total_roa / site2_count
        site2_avg_roa = round(site2_avg_roa, 2)
    except ZeroDivisionError:
        site2_avg_roa = 0

    for item in fake_siteData.copy():
        for option in item.copy():
            if option == 'siteId':
                camp = item[option]
                if camp == 1:
                    item['site_id'] = 1
                    item['average_roas'] = site1_avg_roa
                elif camp == 2:
                    item['site_id'] = 2
                    item['average_roas'] = site2_avg_roa
    res = []
    for item in fake_siteData:
        my_dict = {}
        for key, value in item.items():
            if key == 'site_id':
                my_dict[key] = value
            elif key == 'average_roas':
                my_dict[key] = value
        if my_dict not in res:
            res.append(my_dict)
    return res


print(task2(dataForTask2))
if __name__ == '__main__':
    print('Trial')
