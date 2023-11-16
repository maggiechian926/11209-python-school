取得最新時間
SELECT *
FROM 台北市youbike
WHERE (更新時間,站點名稱) IN (
	SELECT MAX(更新時間),站點名稱
	FROM 台北市youbike
	GROUP BY 站點名稱
) 

搜尋站點
SELECT *
FROM 台北市youbike
WHERE (更新時間,站點名稱) IN (
	SELECT MAX(更新時間),站點名稱
	FROM 台北市youbike
	GROUP BY 站點名稱
) AND 站點名稱 like '%台北%'