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
> action_offer_help

##  SourceData with tags 1
> greet
*  sourceData{"tags":"environment"}
    -   slot{"tags":"environment"}
    -   action_source_data
    -   action_reoffer_help
* affirm
    -  action_reset_slots
    - action_offer_help
> action_offer_help
 
##  SourceData with tags, limit 1
> greet
*  sourceData{"tags":"environment", "limit" : "10"}
    -   slot{"tags":"environment"}
    -   slot{"limit":"10"}   
    -   action_source_data
    -   action_reoffer_help
* affirm
    -  action_reset_slots
    - action_offer_help
> action_offer_help

##  SourceData with tags 2
> greet
*  sourceData{"tags":"environment"}
    -   slot{"tags":"environment"}
    -   action_source_data
    -   action_reoffer_help
* deny
    -   action_farewell
    -   action_restart
 
##  SourceData with tags, limit 2
> greet
*  sourceData{"tags":"environment", "limit" : "10"}
    -   slot{"tags":"environment"}
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
* sourceDataProvideTags{"tags":"environment"}
    -   slot{"tags":"environment"}
    -   action_source_data
    -   action_reoffer_help   
* affirm
    -   action_reset_slots
    -   action_offer_help
> action_offer_help

##  SourceData without tags 2
> greet
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"environment", "limit":"10"}
    -   slot{"tags":"environment"}
    -   slot{"limit":"10"}  
    -   action_source_data
    -   action_reoffer_help
* affirm
    -   action_reset_slots
    -   action_offer_help
> action_offer_help

##  SourceData without tags 4
> greet
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"environment"}
    -   slot{"tags":"environment"}
    -   action_source_data
    -   action_reoffer_help   
* deny
    -   action_farewell
    -   action_restart

##  SourceData without tags 5
> greet
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"environment", "limit":"10"}
    -   slot{"tags":"environment"}
    -   slot{"limit":"10"}  
    -   action_source_data
    -   action_reoffer_help
* deny
    -   action_farewell
    -   action_restart


##  SourceData with tags 3
> greet
*  sourceData{"tags":"healthcare", "tags":"2001"}
    -   slot{"tags":"healthcare"}
    -   slot{"tags":"2001"}
    -   action_source_data
    -   action_reoffer_help
* affirm
    -   action_reset_slots
    -   action_offer_help
> action_offer_help
 
##  SourceData with tags, limit 3
> greet
*  sourceData{"tags":"healthcare", "tags":"2001", "limit" : "10"}
    -   slot{"tags":"healthcare"}
    -   slot{"tags":"2001"}
    -   slot{"limit":"10"}   
    -   action_source_data
    -   action_reoffer_help
* affirm
    -   action_reset_slots
    -   action_offer_help
> action_offer_help

##  SourceData with tags 4
> greet
*  sourceData{"tags":"healthcare", "tags":"2001"}
    -   slot{"tags":"healthcare"}
    -   slot{"tags":"2001"}
    -   action_source_data
    -   action_reoffer_help
* deny
    -   action_farewell
    -   action_restart
 
##  SourceData with tags, limit 4
> greet
*  sourceData{"tags":"healthcare", "limit" : "10", "tags":"2001"}
    -   slot{"tags":"healthcare"}
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
* sourceDataProvideTags{"tags":"healthcare","tags":"2001"}
    -   slot{"tags":"healthcare"}
    -   slot{"tags":"2001"}
    -   action_source_data
    -   action_reoffer_help   
* affirm
    -   action_reset_slots
    -   action_offer_help
> action_offer_help

##  SourceData without tags 7
> greet
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"healthcare", "limit":"10","tags":"2001"}
    -   slot{"tags":"healthcare"}
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
* sourceDataProvideTags{"tags":"environment","tags":"2001"}
    -   slot{"tags":"healthcare"}
    -   slot{"tags":"2001"}
    -   action_source_data
    -   action_reoffer_help   
* affirm
    -   action_reset_slots
    -   action_offer_help
> action_offer_help

##  SourceData without tags 9
> greet
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"healthcare", "limit":"10","tags":"2001"}
    -   slot{"tags":"healthcare"}
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
* sourceDataProvideTags{"tags":"healthcare", "limit":"10","tags":"2001"}
    -   slot{"tags":"healthcare"}
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
* sourceDataProvideTags{"tags":"census", "limit":"10","tags":"2001"}
    -   slot{"tags":"census"}
    -   slot{"tags":"2001"}
    -   slot{"limit":"10"}  
    -   action_source_data
    -   action_reoffer_help
* affirm
    -   action_reset_slots
    -   action_offer_help
> action_offer_help


 ## SourceData without tags 10 full story 3
 * greet
- action_greet
- action_offer_help
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"census"}
    -   slot{"tags":"census"}
    -   action_source_data
    -   action_reoffer_help
* affirm
    -   action_reset_slots
    -   action_offer_help
> action_offer_help

 ## SourceData without tags 10 full story 4
 * greet
- action_greet
- action_offer_help
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"census", "limit":"5"}
    -   slot{"tags":"census"}
   -   slot{"limit":"5"}  
    -   action_source_data
    -   action_reoffer_help
* affirm
    -   action_reset_slots
    -   action_offer_help
> action_offer_help

## SourceData without tags 10 full story 5
* greet
- action_greet
- action_offer_help
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"census"}
    -   slot{"tags":"census"}
    -   action_source_data
    -   action_reoffer_help
* deny
    -   action_farewell
    -   action_restart


## Request Help - block 2
> action_offer_help
* requestHelp
    - action_help
    - action_offer_help
> action_offer_help2

##  SourceData with tags 1- block 2
> action_offer_help
*  sourceData{"tags":"census"}
    -   slot{"tags":"census"}
    -   action_source_data
    -   action_reoffer_help
* affirm
    -  action_reset_slots
    - action_offer_help
> action_offer_help2
 
##  SourceData with tags, limit 1- block 2
> action_offer_help
*  sourceData{"tags":"census", "limit" : "10"}
    -   slot{"tags":"census"}
    -   slot{"limit":"10"}   
    -   action_source_data
    -   action_reoffer_help
* affirm
    -  action_reset_slots
    - action_offer_help
> action_offer_help2

##  SourceData with tags 2- block 2
> action_offer_help
*  sourceData{"tags":"census"}
    -   slot{"tags":"census"}
    -   action_source_data
    -   action_reoffer_help
* deny
    -   action_farewell
    -   action_restart
 
##  SourceData with tags, limit 2- block 2
> action_offer_help
*  sourceData{"tags":"census", "limit" : "10"}
    -   slot{"tags":"census"}
    -   slot{"limit":"10"}  
    -   action_source_data
    -   action_reoffer_help
* deny
    -   action_farewell
    -   action_restart

##  SourceData without tags 1- block 2
> action_offer_help
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"demographics"}
    -   slot{"tags":"demographics"}
    -   action_source_data
    -   action_reoffer_help   
* affirm
    -   action_reset_slots
    -   action_offer_help
> action_offer_help2

##  SourceData without tags 2- block 2
> action_offer_help
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"demographics", "limit":"10"}
    -   slot{"tags":"demographics"}
    -   slot{"limit":"10"}  
    -   action_source_data
    -   action_reoffer_help
* affirm
    -   action_reset_slots
    -   action_offer_help
> action_offer_help2

##  SourceData without tags 4- block 2
> action_offer_help
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"demographics"}
    -   slot{"tags":"demographics"}
    -   action_source_data
    -   action_reoffer_help   
* deny
    -   action_farewell
    -   action_restart

##  SourceData without tags 5- block 2
> action_offer_help
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"demographics", "limit":"10"}
    -   slot{"tags":"demographics"}
    -   slot{"limit":"10"}  
    -   action_source_data
    -   action_reoffer_help
* deny
    -   action_farewell
    -   action_restart


##  SourceData with tags 3- block 2
> action_offer_help
*  sourceData{"tags":"demographics", "tags":"2001"}
    -   slot{"tags":"demographics"}
    -   slot{"tags":"2001"}
    -   action_source_data
    -   action_reoffer_help
* affirm
    -   action_reset_slots
    -   action_offer_help
> action_offer_help2
 
##  SourceData with tags, limit 3- block 2
> action_offer_help
*  sourceData{"tags":"demographics", "tags":"2001", "limit" : "10"}
    -   slot{"tags":"demographics"}
    -   slot{"tags":"2001"}
    -   slot{"limit":"10"}   
    -   action_source_data
    -   action_reoffer_help
* affirm
    -   action_reset_slots
    -   action_offer_help
> action_offer_help2

##  SourceData with tags 4- block 2
> action_offer_help
*  sourceData{"tags":"demographics", "tags":"2001"}
    -   slot{"tags":"demographics"}
    -   slot{"tags":"2001"}
    -   action_source_data
    -   action_reoffer_help
* deny
    -   action_farewell
    -   action_restart
 
##  SourceData with tags, limit 4- block 2
> action_offer_help
*  sourceData{"tags":"demographics", "limit" : "10", "tags":"2001"}
    -   slot{"tags":"demographics"}
    -   slot{"tags":"2001"}
    -   slot{"limit":"10"}  
    -   action_source_data
    -   action_reoffer_help
* deny
    -   action_farewell
    -   action_restart

##  SourceData without tags 6- block 2
> action_offer_help
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"demographics","tags":"2001"}
    -   slot{"tags":"demographics"}
    -   slot{"tags":"2001"}
    -   action_source_data
    -   action_reoffer_help   
* affirm
    -   action_reset_slots
    -   action_offer_help
> action_offer_help2

##  SourceData without tags 7- block 2
> action_offer_help
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"demographics", "limit":"10","tags":"2001"}
    -   slot{"tags":"demographics"}
    -   slot{"tags":"2001"}
    -   slot{"limit":"10"}  
    -   action_source_data
    -   action_reoffer_help
* deny
    -   action_farewell
    -   action_restart

##  SourceData without tags 8- block 2
> action_offer_help
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"demographics","tags":"2001"}
    -   slot{"tags":"demographics"}
    -   slot{"tags":"2001"}
    -   action_source_data
    -   action_reoffer_help   
* affirm
    -   action_reset_slots
    -   action_offer_help
> action_offer_help2

##  SourceData without tags 9- block 2
> action_offer_help
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"demographics", "limit":"10","tags":"2001"}
    -   slot{"tags":"demographics"}
    -   slot{"tags":"2001"}
    -   slot{"limit":"10"}  
    -   action_source_data
    -   action_reoffer_help
* deny
    -   action_farewell
    -   action_restart


## Request Help - block 3
> action_offer_help2
* requestHelp
    - action_help
    - action_offer_help
> action_offer_help3

##  SourceData with tags 1- block 3
> action_offer_help2
*  sourceData{"tags":"demographics"}
    -   slot{"tags":"demographics"}
    -   action_source_data
    -   action_reoffer_help
* affirm
    -  action_reset_slots
    - action_offer_help
> action_offer_help3
 
##  SourceData with tags, limit 1- block 3
> action_offer_help2
*  sourceData{"tags":"demographics", "limit" : "10"}
    -   slot{"tags":"demographics"}
    -   slot{"limit":"10"}   
    -   action_source_data
    -   action_reoffer_help
* affirm
    -  action_reset_slots
    - action_offer_help
> action_offer_help3

##  SourceData with tags 2- block 3
> action_offer_help2
*  sourceData{"tags":"demographics"}
    -   slot{"tags":"demographics"}
    -   action_source_data
    -   action_reoffer_help
* deny
    -   action_farewell
    -   action_restart
 
##  SourceData with tags, limit 2- block 3
> action_offer_help2
*  sourceData{"tags":"demographics", "limit" : "10"}
    -   slot{"tags":"demographics"}
    -   slot{"limit":"10"}  
    -   action_source_data
    -   action_reoffer_help
* deny
    -   action_farewell
    -   action_restart

##  SourceData without tags 1- block 3
> action_offer_help2
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"population"}
    -   slot{"tags":"population"}
    -   action_source_data
    -   action_reoffer_help   
* affirm
    -   action_reset_slots
    -   action_offer_help
> action_offer_help3

##  SourceData without tags 2- block 3
> action_offer_help2
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"population", "limit":"10"}
    -   slot{"tags":"population"}
    -   slot{"limit":"10"}  
    -   action_source_data
    -   action_reoffer_help
* affirm
    -   action_reset_slots
    -   action_offer_help
> action_offer_help3

##  SourceData without tags 4- block 3
> action_offer_help2
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"population"}
    -   slot{"tags":"population"}
    -   action_source_data
    -   action_reoffer_help   
* deny
    -   action_farewell
    -   action_restart

##  SourceData without tags 5- block 3
> action_offer_help2
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"population", "limit":"10"}
    -   slot{"tags":"population"}
    -   slot{"limit":"10"}  
    -   action_source_data
    -   action_reoffer_help
* deny
    -   action_farewell
    -   action_restart


##  SourceData with tags 3- block 3
> action_offer_help2
*  sourceData{"tags":"population", "tags":"2001"}
    -   slot{"tags":"population"}
    -   slot{"tags":"2001"}
    -   action_source_data
    -   action_reoffer_help
* affirm
    -   action_reset_slots
    -   action_offer_help
> action_offer_help3
 
##  SourceData with tags, limit 3- block 3
> action_offer_help2
*  sourceData{"tags":"population", "tags":"2001", "limit" : "10"}
    -   slot{"tags":"population"}
    -   slot{"tags":"2001"}
    -   slot{"limit":"10"}   
    -   action_source_data
    -   action_reoffer_help
* affirm
    -   action_reset_slots
    -   action_offer_help
> action_offer_help3

##  SourceData with tags 4- block 3
> action_offer_help2
*  sourceData{"tags":"population", "tags":"2001"}
    -   slot{"tags":"population"}
    -   slot{"tags":"2001"}
    -   action_source_data
    -   action_reoffer_help
* deny
    -   action_farewell
    -   action_restart
 
##  SourceData with tags, limit 4- block 3
> action_offer_help2
*  sourceData{"tags":"population", "limit" : "10", "tags":"2001"}
    -   slot{"tags":"population"}
    -   slot{"tags":"2001"}
    -   slot{"limit":"10"}  
    -   action_source_data
    -   action_reoffer_help
* deny
    -   action_farewell
    -   action_restart

##  SourceData without tags 6- block 3
> action_offer_help2
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"population","tags":"2001"}
    -   slot{"tags":"population"}
    -   slot{"tags":"2001"}
    -   action_source_data
    -   action_reoffer_help   
* affirm
    -   action_reset_slots
    -   action_offer_help
> action_offer_help3

##  SourceData without tags 7- block 3
> action_offer_help2
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"population", "limit":"10","tags":"2001"}
    -   slot{"tags":"population"}
    -   slot{"tags":"2001"}
    -   slot{"limit":"10"}  
    -   action_source_data
    -   action_reoffer_help
* deny
    -   action_farewell
    -   action_restart

##  SourceData without tags 8- block 3
> action_offer_help2
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"population","tags":"2001"}
    -   slot{"tags":"population"}
    -   slot{"tags":"2001"}
    -   action_source_data
    -   action_reoffer_help   
* affirm
    -   action_reset_slots
    -   action_offer_help
> action_offer_help3

##  SourceData without tags 9- block 3
> action_offer_help2
* sourceData
    -   action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"population", "limit":"10","tags":"2001"}
    -   slot{"tags":"population"}
    -   slot{"tags":"2001"}
    -   slot{"limit":"10"}  
    -   action_source_data
    -   action_reoffer_help
* deny
    -   action_farewell
    -   action_restart
    
## Farewell 1 
> greet
* farewell
    - action_farewell
    - action_restart

## Farewell 2
> action_offer_help
* farewell
    - action_farewell
    - action_restart

## Farewell 3
> action_offer_help2
* farewell
    - action_farewell
    - action_restart

## Farewell 4
> action_offer_help3
* farewell
    - action_farewell
    - action_restart

## Long Story 1
* greet
    - action_greet
    - action_offer_help
* requestHelp
    - action_help
    - action_offer_help
* farewell
    - action_farewell
    - action_restart
* greet
    - action_greet
    - action_offer_help
* requestHelp
    - action_help
    - action_offer_help
* farewell
    - action_farewell
    - action_restart
* greet
    - action_greet
    - action_offer_help
* requestHelp
    - action_help
    - action_offer_help
* farewell
    - action_farewell
    - action_restart
* greet
    - action_greet
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - action_source_data
    - action_reoffer_help
* affirm
    - action_reset_slots
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - action_source_data
    - action_reoffer_help
* affirm
    - action_reset_slots
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - action_source_data
    - action_reoffer_help
* farewell
    - action_farewell
    - action_restart
* greet
    - action_greet
    - action_offer_help
* sourceData{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare", "tags":"female", "tags":"male", "tags":"mobility", "tags":"london"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - slot{"tags":"female"}
    - slot{"tags":"male"}
    - slot{"tags":"mobility"}
    - slot{"tags":"london"}
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart
* greet
    - action_greet
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - action_source_data
    - action_reoffer_help
* affirm
    - action_reset_slots
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - action_source_data
    - action_reoffer_help
* affirm
    - action_reset_slots
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - action_source_data
    - action_reoffer_help
* farewell
    - action_farewell
    - action_restart
* greet
    - action_greet
    - action_offer_help
* sourceData{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare", "tags":"female", "tags":"male", "tags":"mobility", "tags":"london"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - slot{"tags":"female"}
    - slot{"tags":"male"}
    - slot{"tags":"mobility"}
    - slot{"tags":"london"}
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart
* greet
    - action_greet
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - action_source_data
    - action_reoffer_help
* affirm
    - action_reset_slots
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - action_source_data
    - action_reoffer_help
* affirm
    - action_reset_slots
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - action_source_data
    - action_reoffer_help
* farewell
    - action_farewell
    - action_restart
* greet
    - action_greet
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - action_source_data
    - action_reoffer_help
* affirm
    - action_reset_slots
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* farewell
    - action_farewell
    - action_restart
* greet
    - action_greet
    - action_offer_help
* farewell
    - action_farewell
    - action_restart
* greet
    - action_greet
    - action_offer_help
* requestHelp
    - action_help
    - action_offer_help
* requestHelp
    - action_help
    - action_offer_help
* requestHelp
    - action_help
    - action_offer_help
* requestHelp
    - action_help
    - action_offer_help
* sourceData{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare", "tags":"female", "tags":"male", "tags":"mobility", "tags":"london", "tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare", "tags":"female", "tags":"male", "tags":"mobility", "tags":"london"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - slot{"tags":"female"}
    - slot{"tags":"male"}
    - slot{"tags":"mobility"}
    - slot{"tags":"london"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - slot{"tags":"female"}
    - slot{"tags":"male"}
    - slot{"tags":"mobility"}
    - slot{"tags":"london"}
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart
* greet
    - action_greet
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - action_source_data
    - action_reoffer_help
* affirm
    - action_reset_slots
    - action_offer_help
* farewell
    - action_farewell
    - action_restart
* greet
    - action_greet
    - action_offer_help
* requestHelp
    - action_help
    - action_offer_help
* farewell
    - action_farewell
    - action_restart
* greet
    - action_greet
    - action_offer_help
* requestHelp
    - action_help
    - action_offer_help
* farewell
    - action_farewell
    - action_restart
* greet
    - action_greet
    - action_offer_help
* requestHelp
    - action_help
    - action_offer_help
* farewell
    - action_farewell
    - action_restart
* greet
    - action_greet
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - action_source_data
    - action_reoffer_help
* affirm
    - action_reset_slots
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - action_source_data
    - action_reoffer_help
* affirm
    - action_reset_slots
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - action_source_data
    - action_reoffer_help
* farewell
    - action_farewell
    - action_restart
* greet
    - action_greet
    - action_offer_help
* sourceData{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare", "tags":"female", "tags":"male", "tags":"mobility", "tags":"london"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - slot{"tags":"female"}
    - slot{"tags":"male"}
    - slot{"tags":"mobility"}
    - slot{"tags":"london"}
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart
* greet
    - action_greet
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - action_source_data
    - action_reoffer_help
* affirm
    - action_reset_slots
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - action_source_data
    - action_reoffer_help
* affirm
    - action_reset_slots
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - action_source_data
    - action_reoffer_help
* farewell
    - action_farewell
    - action_restart
* greet
    - action_greet
    - action_offer_help
* sourceData{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare", "tags":"female", "tags":"male", "tags":"mobility", "tags":"london"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - slot{"tags":"female"}
    - slot{"tags":"male"}
    - slot{"tags":"mobility"}
    - slot{"tags":"london"}
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart
* greet
    - action_greet
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - action_source_data
    - action_reoffer_help
* affirm
    - action_reset_slots
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - action_source_data
    - action_reoffer_help
* affirm
    - action_reset_slots
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - action_source_data
    - action_reoffer_help
* farewell
    - action_farewell
    - action_restart
* greet
    - action_greet
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - action_source_data
    - action_reoffer_help
* affirm
    - action_reset_slots
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* farewell
    - action_farewell
    - action_restart
* greet
    - action_greet
    - action_offer_help
* farewell
    - action_farewell
    - action_restart
* greet
    - action_greet
    - action_offer_help
* requestHelp
    - action_help
    - action_offer_help
* requestHelp
    - action_help
    - action_offer_help
* requestHelp
    - action_help
    - action_offer_help
* requestHelp
    - action_help
    - action_offer_help
* sourceData{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare", "tags":"female", "tags":"male", "tags":"mobility", "tags":"london", "tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare", "tags":"female", "tags":"male", "tags":"mobility", "tags":"london"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - slot{"tags":"female"}
    - slot{"tags":"male"}
    - slot{"tags":"mobility"}
    - slot{"tags":"london"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - slot{"tags":"female"}
    - slot{"tags":"male"}
    - slot{"tags":"mobility"}
    - slot{"tags":"london"}
    - action_source_data
    - action_reoffer_help
* deny
    - action_farewell
    - action_restart
* greet
    - action_greet
    - action_offer_help
* sourceData
    - action_source_data_prompt_tags
* sourceDataProvideTags{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - action_source_data
    - action_reoffer_help
* affirm
    - action_reset_slots
    - action_offer_help
* farewell
    - action_farewell
    - action_restart
* greet
    - action_greet
    - action_offer_help
* requestHelp
    - action_help
    - action_offer_help
* farewell
    - action_farewell
    - action_restart
* greet
    - action_greet
    - action_offer_help
* requestHelp
    - action_help
    - action_offer_help
* farewell
    - action_farewell
    - action_restart
* greet
    - action_greet
    - action_offer_help

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

## Farewell Spam
* farewell
    - action_farewell
    - action_restart
* farewell
    - action_farewell
    - action_restart
* farewell
    - action_farewell
    - action_restart
* farewell
    - action_farewell
    - action_restart
* farewell
    - action_farewell
    - action_restart
* farewell
    - action_farewell
    - action_restart
* farewell
    - action_farewell
    - action_restart
* farewell
    - action_farewell
    - action_restart
* farewell
    - action_farewell
    - action_restart
* farewell
    - action_farewell
    - action_restart
* farewell
    - action_farewell
    - action_restart
* farewell
    - action_farewell
    - action_restart
* farewell
    - action_farewell
    - action_restart
* farewell
    - action_farewell
    - action_restart
* farewell
    - action_farewell
    - action_restart
* farewell
    - action_farewell
    - action_restart

## Greet Spam
* greet
    - action_greet
    - action_offer_help
* greet
    - action_greet
    - action_offer_help
* greet
    - action_greet
    - action_offer_help
* greet
    - action_greet
    - action_offer_help
* greet
    - action_greet
    - action_offer_help
* greet
    - action_greet
    - action_offer_help
* greet
    - action_greet
    - action_offer_help
* greet
    - action_greet
    - action_offer_help
* greet
    - action_greet
    - action_offer_help
* greet
    - action_greet
    - action_offer_help
* greet
    - action_greet
    - action_offer_help
* greet
    - action_greet
    - action_offer_help
* greet
    - action_greet
    - action_offer_help
* greet
    - action_greet
    - action_offer_help
* greet
    - action_greet
    - action_offer_help
* greet
    - action_greet
    - action_offer_help

## Source Data Spam 
*sourceData{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceData{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceData{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceData{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceData{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceData{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceData{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceData{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceData{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceData{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceData{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceData{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceData{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceData{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceData{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceData{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help

## Source Data Provide Tags Spam 
*sourceDataProvideTags{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceDataProvideTags{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceDataProvideTags{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceDataProvideTags{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceDataProvideTags{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceDataProvideTags{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceDataProvideTags{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceDataProvideTags{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceDataProvideTags{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceDataProvideTags{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceDataProvideTags{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceDataProvideTags{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceDataProvideTags{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceDataProvideTags{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceDataProvideTags{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help
*sourceDataProvideTags{"tags": "child", "tags": "health"}
    - slot{"tags":"child"}
    - slot{"tags":"health"}
    - action_source_data
    - action_reoffer_help

## Request Help Spam 
*requestHelp
    - action_help
    - action_offer_help
*requestHelp
    - action_help
    - action_offer_help
*requestHelp
    - action_help
    - action_offer_help
*requestHelp
    - action_help
    - action_offer_help
*requestHelp
    - action_help
    - action_offer_help
*requestHelp
    - action_help
    - action_offer_help
*requestHelp
    - action_help
    - action_offer_help
*requestHelp
    - action_help
    - action_offer_help
*requestHelp
    - action_help
    - action_offer_help
*requestHelp
    - action_help
    - action_offer_help
*requestHelp
    - action_help
    - action_offer_help
*requestHelp
    - action_help
    - action_offer_help
*requestHelp
    - action_help
    - action_offer_help
*requestHelp
    - action_help
    - action_offer_help
*requestHelp
    - action_help
    - action_offer_help
*requestHelp
    - action_help
    - action_offer_help

## Many entities
* greet
    - action_greet
    - action_offer_help
* sourceData{"tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare", "tags":"female", "tags":"male", "tags":"mobility", "tags":"london", "tags":"child", "tags":"population", "tags":"pollution", "tags": "healthcare", "tags":"female", "tags":"male", "tags":"mobility", "tags":"london"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - slot{"tags":"female"}
    - slot{"tags":"male"}
    - slot{"tags":"mobility"}
    - slot{"tags":"london"}
    - slot{"tags":"child"}
    - slot{"tags":"population"}
    - slot{"tags":"pollution"}
    - slot{"tags":"healthcare"}
    - slot{"tags":"female"}
    - slot{"tags":"male"}
    - slot{"tags":"mobility"}
    - slot{"tags":"london"}
    - action_source_data
    - action_reoffer_help