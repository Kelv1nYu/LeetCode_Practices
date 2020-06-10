SELECT ad_id,

ROUND(IFNULL(SUM(IF(action = 'Clicked',1,0)) * 100 / ((SUM(IF(action = 'Clicked',1,0)) + 
        SUM(IF(action = 'Viewed',1,0)))), 0), 2) AS 'ctr'

FROM Ads
Group BY ad_id
ORDER BY ctr DESC, ad_id;