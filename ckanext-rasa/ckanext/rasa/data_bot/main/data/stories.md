## Greet 1
* greet
- action_greet
- action_offer_help
> greet

## Request Help 
> greet
* requestHelp
    - action_help
    - action_offer_help
> greet

##  SourceData with tags 1
> greet
*  sourceData{"tags":"abc"}
    -   slot{"tags":"abc"}
    -   action_source_data
    -   action_reoffer_help
* affirm
    -  action_reset_slots
    - action_offer_help
> greet
 
##  SourceData with tags, limit 1
> greet
*  sourceData{"tags":"abc", "limit" : "10"}
    -   slot{"tags":"abc"}
    -   slot{"limit":"10"}   
    -   action_source_data
    -   action_reoffer_help
* affirm
    -  action_reset_slots
    - action_offer_help
> greet

##  SourceData with tags 2
> greet
*  sourceData{"tags":"abc"}
    -   slot{"tags":"abc"}
    -   action_source_data
    -   action_reoffer_help
* deny
    -   action_farewell
    -   action_restart
 
##  SourceData with tags, limit 2
> greet
*  sourceData{"tags":"abc", "limit" : "10"}
    -   slot{"tags":"abc"}
    -   slot{"limit":"10"}  
    -   action_source_data
    -   action_reoffer_help
* deny
    -   action_farewell
    -   action_restart

##  SourceData without tags 1
> greet
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"abc"}
    -   slot{"tags":"abc"}
    -   action_source_data
    -   action_reoffer_help   
* affirm
    -   action_reset_slots
    -   action_offer_help
> greet

##  SourceData without tags 2
> greet
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"abc", "limit":"10"}
    -   slot{"tags":"abc"}
    -   slot{"limit":"10"}  
    -   action_source_data
    -   action_reoffer_help
* affirm
    -   action_reset_slots
    -   action_offer_help
> greet

##  SourceData without tags 4
> greet
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"abc"}
    -   slot{"tags":"abc"}
    -   action_source_data
    -   action_reoffer_help   
* deny
    -   action_farewell
    -   action_restart

##  SourceData without tags 5
> greet
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"abc", "limit":"10"}
    -   slot{"tags":"abc"}
    -   slot{"limit":"10"}  
    -   action_source_data
    -   action_reoffer_help
* deny
    -   action_farewell
    -   action_restart


##  SourceData with tags 3
> greet
*  sourceData{"tags":"abc", "tags":"2001"}
    -   slot{"tags":"abc"}
    -   slot{"tags":"2001"}
    -   action_source_data
    -   action_reoffer_help
* affirm
    -   action_reset_slots
    -   action_offer_help
> greet
 
##  SourceData with tags, limit 3
> greet
*  sourceData{"tags":"abc", "tags":"2001", "limit" : "10"}
    -   slot{"tags":"abc"}
    -   slot{"tags":"2001"}
    -   slot{"limit":"10"}   
    -   action_source_data
    -   action_reoffer_help
* affirm
    -   action_reset_slots
    -   action_offer_help
> greet

##  SourceData with tags 4
> greet
*  sourceData{"tags":"abc", "tags":"2001"}
    -   slot{"tags":"abc"}
    -   slot{"tags":"2001"}
    -   action_source_data
    -   action_reoffer_help
* deny
    -   action_farewell
    -   action_restart
 
##  SourceData with tags, limit 4
> greet
*  sourceData{"tags":"abc", "limit" : "10", "tags":"2001"}
    -   slot{"tags":"abc"}
    -   slot{"tags":"2001"}
    -   slot{"limit":"10"}  
    -   action_source_data
    -   action_reoffer_help
* deny
    -   action_farewell
    -   action_restart

##  SourceData without tags 6
> greet
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"abc","tags":"2001"}
    -   slot{"tags":"abc"}
    -   slot{"tags":"2001"}
    -   action_source_data
    -   action_reoffer_help   
* affirm
    -   action_reset_slots
    -   action_offer_help
> greet

##  SourceData without tags 7
> greet
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"abc", "limit":"10","tags":"2001"}
    -   slot{"tags":"abc"}
    -   slot{"tags":"2001"}
    -   slot{"limit":"10"}  
    -   action_source_data
    -   action_reoffer_help
* deny
    -   action_farewell
    -   action_restart

##  SourceData without tags 8
> greet
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"abc","tags":"2001"}
    -   slot{"tags":"abc"}
    -   slot{"tags":"2001"}
    -   action_source_data
    -   action_reoffer_help   
* affirm
    -   action_reset_slots
    -   action_offer_help
> greet

##  SourceData without tags 9
> greet
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"abc", "limit":"10","tags":"2001"}
    -   slot{"tags":"abc"}
    -   slot{"tags":"2001"}
    -   slot{"limit":"10"}  
    -   action_source_data
    -   action_reoffer_help
* deny
    -   action_farewell
    -   action_restart
    
## SourceData without tags 10 full story 1
* greet
- action_greet
- action_offer_help
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"abc", "limit":"10","tags":"2001"}
    -   slot{"tags":"abc"}
    -   slot{"tags":"2001"}
    -   slot{"limit":"10"}  
    -   action_source_data
    -   action_reoffer_help
* deny
    -   action_farewell
    -   action_restart
 
 ## SourceData without tags 10 full story 2
 * greet
- action_greet
- action_offer_help
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"abc", "limit":"10","tags":"2001"}
    -   slot{"tags":"abc"}
    -   slot{"tags":"2001"}
    -   slot{"limit":"10"}  
    -   action_source_data
    -   action_reoffer_help
* affirm
    -   action_reset_slots
    -   action_offer_help
> greet

 ## SourceData without tags 10 full story 3
 * greet
- action_greet
- action_offer_help
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"abc"}
    -   slot{"tags":"abc"}
    -   action_source_data
    -   action_reoffer_help
* affirm
    -   action_reset_slots
    -   action_offer_help
> greet

 ## SourceData without tags 10 full story 4
 * greet
- action_greet
- action_offer_help
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"abc", "limit":"5"}
    -   slot{"tags":"abc"}
   -   slot{"limit":"5"}  
    -   action_source_data
    -   action_reoffer_help
* affirm
    -   action_reset_slots
    -   action_offer_help
> greet

## SourceData without tags 10 full story 5
* greet
- action_greet
- action_offer_help
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"abc"}
    -   slot{"tags":"abc"}
    -   action_source_data
    -   action_reoffer_help
* deny
    -   action_farewell
    -   action_restart