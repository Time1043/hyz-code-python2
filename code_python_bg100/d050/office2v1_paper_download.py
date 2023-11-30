# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/11/30 16:43
# @File    ：office2v1_paper_download.py
# @Function:

import requests
from urllib.parse import urlparse, urljoin
import os


def download_pdfs(url_list, destination_folder):
    """
    Download PDFs from a list of URLs and save them to a specified destination folder.

    :param url_list: List of URLs pointing to the PDFs.
    :param destination_folder: Folder path where PDFs will be saved.
    :return: A list of file paths for the downloaded PDFs.
    """
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created directory: {destination_folder}")

    downloaded_files = []

    for url in url_list:
        # Extracting the PDF file name from the URL
        parsed_url = urlparse(url)
        file_name = parsed_url.path.split('/')[-1] + ".pdf"

        # Joining the destination folder with the file name
        file_path = os.path.join(destination_folder, file_name)

        # Modifying the URL to get the direct PDF link
        pdf_url = url.replace("/abs/", "/pdf/") + ".pdf"  # Change to direct PDF link

        print(f"Downloading {pdf_url}...")

        # Downloading the PDF
        try:
            response = requests.get(pdf_url)
            if response.status_code == 200:
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                downloaded_files.append(file_path)
                print(f"Downloaded and saved to {file_path}")
            else:
                print(f"Failed to download PDF from {url}. Status Code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred while downloading {url}: {e}")

    return downloaded_files


if __name__ == '__main__':
    # Example usage
    url_list = [
        "https://arxiv.org/abs/2307.08621",
        "https://arxiv.org/abs/1803.08494",
        # ... more URLs ...
    ]

    destination_folder = r"C:\Users\huangyingzhu\Desktop\paper"

    # Calling the function
    downloaded_files = download_pdfs(url_list, destination_folder)
    print(downloaded_files)
