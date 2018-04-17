## Source Data with 1 Entity
* greet
    - action_greet
    - action_offer_help
* sourceData{"tags": "healthcare"}
    - slot{"tags": "healthcare"}
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart

## Source Data with 2 Entities
* greet
    - action_greet
    - action_offer_help
* sourceData{"tags": "healthcare", "tags": "child"}
    - slot{"tags": "healthcare"}
    - slot{"tags": "child"}    
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart

## Source Data with 3 Entities
* greet
    - action_greet
    - action_offer_help
* sourceData{"tags": "healthcare", "tags": "child", "tags":"education"}
    - slot{"tags": "healthcare"}
    - slot{"tags": "child"}    
    - slot{"tags": "education"}            
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart

## Source Data with 4 Entities
* greet
    - action_greet
    - action_offer_help
* sourceData{"tags": "healthcare", "tags": "child", "tags":"education", "tags":"population"}
    - slot{"tags": "healthcare"}
    - slot{"tags": "child"}    
    - slot{"tags": "education"}  
    - slot{"tags": "population"}    
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart

## Source Data with 5 Entities 
* greet
    - action_greet
    - action_offer_help
* sourceData{"tags": "healthcare", "tags": "child", "tags":"education", "tags":"population","tags":"growth"}
    - slot{"tags": "healthcare"}
    - slot{"tags": "child"}    
    - slot{"tags": "education"}  
    - slot{"tags": "population"}  
    - slot{"tags": "growth"}
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart
    
## Source Data with 6 Entities
* greet
    - action_greet
    - action_offer_help
* sourceData{"tags": "healthcare", "tags": "child", "tags":"education", "tags":"population","tags":"growth", "tags": "rate"}
    - slot{"tags": "healthcare"}
    - slot{"tags": "child"}    
    - slot{"tags": "education"}  
    - slot{"tags": "population"}  
    - slot{"tags": "growth"}
    - slot{"tags": "rate"}    
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart

## Source Data with 1 Entity and Limit
* greet
    - action_greet
    - action_offer_help
* sourceData{"tags": "healthcare", "limit": "10"}
    - slot{"tags": "healthcare"}
    - slot{"limit": "10"}
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart

## Source Data with 2 Entities and Limit
* greet
    - action_greet
    - action_offer_help
* sourceData{"tags": "healthcare", "tags": "child", "limit": "10"}
    - slot{"tags": "healthcare"}
    - slot{"tags": "child"}    
    - slot{"limit": "10"}    
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart

## Source Data with 3 Entities and Limit
* greet
    - action_greet
    - action_offer_help
* sourceData{"tags": "healthcare", "tags": "child", "tags":"education", "limit": "10"}
    - slot{"tags": "healthcare"}
    - slot{"tags": "child"}    
    - slot{"tags": "education"}            
    - slot{"limit": "10"}
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart

## Source Data with 4 Entities and Limit
* greet
    - action_greet
    - action_offer_help
* sourceData{"tags": "healthcare", "tags": "child", "tags":"education", "tags":"population", "limit": "10"}
    - slot{"tags": "healthcare"}
    - slot{"tags": "child"}    
    - slot{"tags": "education"}  
    - slot{"tags": "population"}    
    - slot{"limit": "10"}
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart

## Source Data with 5 Entities and Limit 
* greet
    - action_greet
    - action_offer_help
* sourceData{"tags": "healthcare", "tags": "child", "tags":"education", "tags":"population","tags":"growth", "limit": "10"}
    - slot{"tags": "healthcare"}
    - slot{"tags": "child"}    
    - slot{"tags": "education"}  
    - slot{"tags": "population"}  
    - slot{"tags": "growth"}
    - slot{"limit": "10"}
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart
  
## Source Data with 6 Entities and Limit
* greet
    - action_greet
    - action_offer_help
* sourceData{"tags": "healthcare", "tags": "child", "tags":"education", "tags":"population","tags":"growth", "tags": "rate", "limit": "10"}
    - slot{"tags": "healthcare"}
    - slot{"tags": "child"}    
    - slot{"tags": "education"}  
    - slot{"tags": "population"}  
    - slot{"tags": "growth"}
    - slot{"tags": "rate"}    
    - slot{"limit": "10"}
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart

## Source Data Provide Tags with 1 Entity
* greet
    - action_greet
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags": "healthcare"}
    - slot{"tags": "healthcare"}
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart

## Source Data Provide Tags with 2 Entities
* greet
    - action_greet
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags": "healthcare", "tags":"child"}
    - slot{"tags": "healthcare"}
    - slot{"tags": "child"}
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart

## Source Data Provide Tags with 3 Entities
* greet
    - action_greet
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags": "healthcare", "tags":"child", "tags": "education"}
    - slot{"tags": "healthcare"}
    - slot{"tags": "child"}
    - slot{"tags": "education"}
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart

## Source Data Provide Tags with 4 Entities
* greet
    - action_greet
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags": "healthcare", "tags":"child", "tags": "education", "tags":"population"}
    - slot{"tags": "healthcare"}
    - slot{"tags": "child"}
    - slot{"tags": "education"}
    - slot{"tags": "population"}
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart

## Source Data Provide Tags with 5 Entities
* greet
    - action_greet
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags": "healthcare", "tags":"child", "tags": "education", "tags":"population", "tags": "growth"}
    - slot{"tags": "healthcare"}
    - slot{"tags": "child"}    
    - slot{"tags": "education"}  
    - slot{"tags": "population"}  
    - slot{"tags": "growth"}
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart

## Source Data Provide Tags with 6 Entities
* greet
    - action_greet
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags": "healthcare", "tags":"child", "tags": "education", "tags":"population", "tags": "growth", "tags":"rate"}
    - slot{"tags": "healthcare"}
    - slot{"tags": "child"}    
    - slot{"tags": "education"}  
    - slot{"tags": "population"}  
    - slot{"tags": "growth"}
    - slot{"tags": "rate"}  
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart


## Source Data Provide Tags with 1 Entity and Limit
* greet
    - action_greet
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags": "healthcare", "limit": "10"}
    - slot{"tags": "healthcare"}
    - slot{"limit": "10"}    
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart

## Source Data Provide Tags with 2 Entities and Limit
* greet
    - action_greet
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags": "healthcare", "tags":"child", "limit": "10"}
    - slot{"tags": "healthcare"}
    - slot{"tags": "child"}
    - slot{"limit": "10"}
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart

## Source Data Provide Tags with 3 Entities and Limit
* greet
    - action_greet
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags": "healthcare", "tags":"child", "tags": "education", "limit": "10"}
    - slot{"tags": "healthcare"}
    - slot{"tags": "child"}
    - slot{"tags": "education"}
    - slot{"limit": "10"}    
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart

## Source Data Provide Tags with 4 Entities and Limit
* greet
    - action_greet
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags": "healthcare", "tags":"child", "tags": "education", "tags":"population", "limit": "10"}
    - slot{"tags": "healthcare"}
    - slot{"tags": "child"}
    - slot{"tags": "education"}
    - slot{"tags": "population"}
    - slot{"limit": "10"}    
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart

## Source Data Provide Tags with 5 Entities and Limit 
* greet
    - action_greet
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags": "healthcare", "tags":"child", "tags": "education", "tags":"population", "tags": "growth", "limit":"10"}
    - slot{"tags": "healthcare"}
    - slot{"tags": "child"}    
    - slot{"tags": "education"}  
    - slot{"tags": "population"}  
    - slot{"tags": "growth"}
    - slot{"tags": "10"}
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart

## Source Data Provide Tags with 6 Entities and Limit
* greet
    - action_greet
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags": "healthcare", "tags":"child", "tags": "education", "tags":"population", "tags": "growth", "tags":"rate", "limit": "10"}
    - slot{"tags": "healthcare"}
    - slot{"tags": "child"}    
    - slot{"tags": "education"}  
    - slot{"tags": "population"}  
    - slot{"tags": "growth"}
    - slot{"tags": "rate"}  
    - slot{"limit": "10"}      
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart

## Request Help 
* greet
    - action_greet
    - action_offer_help
* requestHelp
    - action_help
    - action_offer_help
* deny
    - action_farewell
    - action_restart

## Farewell after action_offer_help
* greet
    - action_greet
    - action_offer_help
* farewell
    - action_farewell
    - action_restart
## Farewell afer action_source_data_prompt_tags
* greet
    - action_greet
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* farewell
    - action_farewell
    - action_restart

## Farewell after acter_reoffer_help
* greet
    - action_greet
    - action_offer_help
* sourceData{"tags": "healthcare"}
    - slot{"tags": "healthcare"}
    - action_source_data
    - action_reoffer_help
* farewell
    - action_farewell
    - action_restart
