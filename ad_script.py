import datetime
import random
import json
from facebookads.api import FacebookAdsApi
from facebookads.adobjects.campaign import Campaign
#from facebookads import adobjects
from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.targeting import Targeting
from facebookads.adobjects.targetingsearch import TargetingSearch
from facebookads.adobjects.adimage import AdImage
from facebookads.adobjects.adcreative import AdCreative
from facebookads.adobjects.adcreativelinkdata import AdCreativeLinkData
from facebookads.adobjects.adcreativeobjectstoryspec \
import AdCreativeObjectStorySpec
from facebookads.adobjects.ad import Ad
from facebookads.adobjects.customaudience import CustomAudience

my_app_id = ''
my_app_secret = ''
my_access_token = ''
my_campaign_id = ''
my_ad_account_id = ''
my_page_id = ''

image_hash_1 = ''

def get_campaign():
    """
    Fetch your campaign
    """
    campaign = Campaign(my_campaign_id)
    return campaign

def activate_campaign():
    campaign = Campaign(my_campaign_id)
    campaign[Campaign.Field.status] = 'ACTIVE'
    campaign.remote_update()
    pass

def get_ad_set(campaign):
    adsets = campaign.get_ad_sets()
    adset = AdSet(fbid=adsets[0][AdSet.Field.id])
    print (adset)
    return adset

def create_new_ad_set():
    """
    Create a new adset
    """
    adset = AdSet(parent_id=my_ad_account_id)
    adset[AdSet.Field.name] = 'Mutegolf SDK Ad Set'
    adset[AdSet.Field.campaign_id] = my_campaign_id
    
    adset[AdSet.Field.optimization_goal] = AdSet.OptimizationGoal.page_likes
    adset[AdSet.Field.promoted_object] = {
            'page_id': my_page_id
        }
    
    adset[AdSet.Field.billing_event] = AdSet.BillingEvent.impressions
    #adset[AdSet.Field.end_time] = 1520517600 # UNIX 
    adset[AdSet.Field.daily_budget] = 200 # 200 cents
    adset[AdSet.Field.is_autobid] = True
    adset[AdSet.Field.targeting] = {
        Targeting.Field.geo_locations: {
            'countries': ['IN']
        }
    }

    ''',
    "flexible_spec": [
            {
                "interests": [
                  {
                    "id": "6003107902433", 
                    "name": "Association football (Soccer)"
                  }, 
                  {
                    "id": "6003139266461", 
                    "name": "Movies"
                  }
                ]
            }
        ]
        Targeting.Field.genders: {
            'genders': [2]
        }'''
    
    adset[AdSet.Field.status] = AdSet.Status.active

    adset.remote_create()
    #adset[AdSet.Field.bid_amount] = 
    #remote_adset

    return adset

def create_new_ad(adset, image_hash):

    link_data = AdCreativeLinkData()
    link_data[AdCreativeLinkData.Field.message] = '“Like” to find ways to help man’s best friend.'
    link_data[AdCreativeLinkData.Field.link] = 'https://www.facebook.com/caltech.clickmaniac'
    link_data[AdCreativeLinkData.Field.image_hash] = image_hash

    object_story_spec = AdCreativeObjectStorySpec()
    object_story_spec[AdCreativeObjectStorySpec.Field.page_id] = my_page_id
    object_story_spec[AdCreativeObjectStorySpec.Field.link_data] = link_data


    creative = AdCreative(parent_id=my_ad_account_id)
    creative[AdCreative.Field.name] = 'SDK Creative 1'
    creative[AdCreative.Field.object_story_spec] = object_story_spec

    # Finally, create your ad along with ad creative.
    # Please note that the ad creative is not created independently, rather its
    # data structure is appended to the ad group
    ad = Ad(parent_id=my_ad_account_id)
    ad[Ad.Field.name] = 'SDK Dog Ad 1'
    ad[Ad.Field.adset_id] = adset[AdSet.Field.id]
    ad[Ad.Field.creative] = creative
    ad[Ad.Field.status] = Ad.Status.active
    ad.remote_create()
    pass

def create_new_ad_image(filepath):
    image = AdImage(parent_id=my_ad_account_id)
    image[AdImage.Field.filename] = filepath
    image.remote_create()

    return image[AdImage.Field.hash]

def create_filter_array(dict):
    pass

def remote_update(adset):
    """ Update your adset. """
    adset.remote_update(params = {
        AdSet.Field.bid_amount: 1,
        AdSet.Field.targeting: {
            Targeting.Field.geo_locations: {
                'countries': ['IN', 'ID']
            }
        }
    })
    '''adset.remote_update(params = {
        AdSet.Field.targeting: {
            Targeting.Field.geo_locations: {
                'countries': ['IN']
            },
            Targeting.Field.interests: [
                {
                    'id': 6003332344237,
                    'name': 'Dogs',
                },
                {
                    "id": 6004041604463,
                    "name": "Dogs and Puppies!"
                },
                {
                    "id": 6004037726009,
                    "name": "Pets"
                },
                {
                    "id": 6003341040796,
                    "name": "Puppy"
                }
            ],
        }
        })
    '''
    print (adset)
    
def get_clicks(adset):
    """ Get impressions...this could be used for anything. """
    params = {
        "fields": [
            AdsInsights.Field.unique_clicks
        ],
        "level": "ad", # maybe change this?
        "time_range": {
            "since": "2016-11-11",
            "until": "2016-11-13"
            }
    }
    # Returns an array of insights for each ad.
    clicks = set.get_insights(params = params)

def get_interest_ids():
    params = {
        'q': 'puppy',
        'type': 'adinterest'
    }

    resp = TargetingSearch.search(params=params)
    print(resp)

def get_country_ids():
    params = {
        'q': 'indonesia',
        'type': 'adgeolocation',
        'location_types': ['country'],
    }
    resp = TargetingSearch.search(params=params)
    print(resp)


if __name__ == "__main__":

    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

    campaign = get_campaign()

    #activate_campaign()

    #get_interest_ids()
    #create_new_ad(adset, image_hash)

    '''
    image_paths = ['ad_pictures/dog_ads/3.jpg']
    #for path in image_paths:
    image_hash = create_new_ad_image('ad_pictures/dog_ads/3.jpg')

    print ('Image Hash: ', image_hash)
    '''
    
    
    #adset = create_new_ad_set()

    #print ('Ad Set Created!')
    #get_country_ids()
    
    adset = get_ad_set(campaign)

    remote_update(adset)

    #print (adset)

    #create_new_ad(adset, image_hash_1)

    '''
    if len(adset.get_ads()) > 0:
        print ("# Ads:", len(adset.get_ads()))
    '''
    '''else:
        create_new_ad(adset)
    '''
    