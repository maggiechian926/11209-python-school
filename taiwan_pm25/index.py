import requests
import psycopg2 #連接PostgreSQL 資料庫
from datetime import datetime
from password import apikey


__all__ = ['ambient_air_postgresql_data']

'''下載資料'''
def download_air_data() -> dict:
    air_url = f"https://data.moenv.gov.tw/api/v2/aqx_p_02?api_key={apikey}"
    response = requests.get(air_url, params={'limit': 100})
    response.raise_for_status()
    print('下載成功，你好棒喔！')
    return response.json()

'''連接資料庫'''
def connect_to_database() ->list[tuple]:
    conn = psycopg2.connect(
        host='localhost',
        database='air_quality',
        user='postgres',
        password='your_password',
    )
    return conn

'''建立資料表'''
def create_table(conn:psycopg2.Connection) -> None:
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "細懸浮微粒資料PM2.5"(
        "ID" SERIAL,
        "測站名稱" TEXT NOT NULL,
        "縣市名稱" TEXT NOT NULL,
        "細懸浮微粒濃度" FLOAT NOT NULL,
        "資料建置日期" TEXT NOT NULL,
        "測項單位" TEXT NOT NULL,
        "更新時間" TEXT NOT NULL,
        PRIMARY KEY("ID")
        )
        ''')
    conn.commit()

'''新增資料'''
def insert_data(conn:psycopg2.Connection,values:list[any]) -> None:
    cursor = conn.cursor()
    for value in values:
        cursor.execute(
            '''
            INSERT INTO 細懸浮微粒資料PM2.5(測站名稱,縣市名稱,細懸浮微粒濃度,資料建置日期,測項單位,更新時間)
            VALUES(%s, %s, %s, %s, %s, %s)
            ''',
            value,
        )
    conn.commit()

'''下載,並更新資料庫'''
def update_postgresql_data()->None:
    data = download_air_data()
    conn = connect_to_database()
    create_table(conn)
    values = []
    for item in data['records']:
        values.append([item['site'], item['county'], item['pm25'], item['datacreationdate'], item['itemunit']])
    insert_data(conn,values)
    conn.close()

def main():
    start_time = datetime.now()
    while (datetime.now() - start_time) < datetime.timedelta(hours=24):
        update_postgresql_data()
        time.sleep(3600)
    print('資料更新完畢，程式結束')

if __name__ == '__main__':
    main()
