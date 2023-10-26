import requests

def download_youbike_data():
    '''
    下載youbike2.0資料
    https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json
    '''
    
    youbike_url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    response = requests.get(youbike_url)
    if requests.status_codes == 200:
       raise Exception("下載成功")
    else:
       raise Exception("下載失敗")
        
        
    