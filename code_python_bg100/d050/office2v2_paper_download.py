# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/11/30 16:43
# @File    ：office2v2_paper_download.py
# @Function:

import requests
from urllib.parse import urlparse, urljoin
import os
import time


def read_urls_from_file(file_path):
    """
    Read URLs from a given text file.

    :param file_path: Path to the text file containing URLs.
    :return: List of URLs.
    """
    with open(file_path, 'r') as file:
        urls = file.readlines()
    return [url.strip() for url in urls]


def download_pdfs(url_list, destination_folder, delay=5):
    """
    Download PDFs from a list of URLs and save them to a specified destination folder.

    :param url_list: List of URLs pointing to the PDFs.
    :param destination_folder: Folder path where PDFs will be saved.
    :param delay: Delay between downloads in seconds.
    :return: A list of file paths for the downloaded PDFs.
    """
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created directory: {destination_folder}")

    downloaded_files = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    for url in url_list:
        parsed_url = urlparse(url)
        file_name = parsed_url.path.split('/')[-1] + ".pdf"
        file_path = os.path.join(destination_folder, file_name)
        pdf_url = url.replace("/abs/", "/pdf/") + ".pdf"

        print(f"Downloading {pdf_url}...")

        try:
            response = requests.get(pdf_url, headers=headers)
            if response.status_code == 200:
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                downloaded_files.append(file_path)
                print(f"Downloaded and saved to {file_path}")
            else:
                print(f"Failed to download PDF from {url}. Status Code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred while downloading {url}: {e}")

        time.sleep(delay)  # Delay to prevent overwhelming the server

    return downloaded_files


if __name__ == '__main__':
    # Example usage
    file_path = r"D:\code\hyz-code-python2\code_python_bg100\d050\paprt_url231130.txt"
    url_list = read_urls_from_file(file_path)

    destination_folder = r"C:\Users\huangyingzhu\Desktop\paper"

    # Calling the function
    downloaded_files = download_pdfs(url_list, destination_folder)
    print("Downloaded files:", downloaded_files)
