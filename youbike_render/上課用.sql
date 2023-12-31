/*
沖突更新資料
*/
INSERT INTO 台北市youbike (站點名稱, 行政區, 更新時間, 地址, 總車輛數, 可借, 可還) 
VALUES ('YouBike2.0_一壽橋','文山區','2023-11-08 10:43:16','樟新街64號前方',100,10,20)
ON CONFLICT (站點名稱,更新時間) DO UPDATE 
  SET 總車輛數 = 100, 
      可借 = 10,
	    可還 = 20;


/*
沖突不做事
*/
INSERT INTO 台北市youbike (站點名稱, 行政區, 更新時間, 地址, 總車輛數, 可借, 可還) 
VALUES ('YouBike2.0_一壽橋','文山區','2023-11-08 10:43:16','樟新街64號前方',100,10,20)
ON CONFLICT (站點名稱,更新時間) DO NOTHING 

	  
	  
SELECT * 
FROM 台北市youbike
WHERE 站點名稱='YouBike2.0_一壽橋'

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

概念是將目前 table 同時命名為「a」,「b」後，用 join 語法來達成自己與自己比對資料的結果，再用 select distinct 的功能刪除重複資料