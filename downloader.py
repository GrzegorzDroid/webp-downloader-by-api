import requests
import pandas as pd
import os

# data loader function
def load_data(file_path):
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Use CSV or XLSX.")

# download function
def download_image(session, url, save_path):
    response = session.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
    else:
        print(f"Failed to download {url}, status code: {response.status_code}")

# main function
def main(file_path, download_folder, access_token, refresh_token):
    # load data from file
    data = load_data(file_path)
    
    # check if download folder exists
    os.makedirs(download_folder, exist_ok=True)
    
    # configuration of cookie session
    session = requests.Session()
    session.cookies.set('accessToken', access_token)
    session.cookies.set('refreshToken', refresh_token)
    
    # go through each line and download
    for index, row in data.iterrows():
        reference_code = row['reference code']
        api_path = row['api path']
        
        # set download url
        url = f"https://1-25-0.elements.4sellers.cloud{api_path}"
        
        # save path
        save_path = os.path.join(download_folder, f"{reference_code}.webp")
        
        # download image
        download_image(session, url, save_path)
        
        print(f"Downloaded {reference_code} to {save_path}")

if __name__ == "__main__":
    file_path = '.csv'  # path to csv or xlsx file
    download_folder = '' # where to download images
    # auth tokens
    access_token = ''
    refresh_token = ''
    
    main(file_path, download_folder, access_token, refresh_token)
