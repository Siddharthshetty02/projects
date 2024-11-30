import requests
from bs4 import BeautifulSoup
import os

def download_instagram_reel(url, output_folder="reels"):
    """
    Downloads an Instagram reel from the provided URL.

    Args:
        url (str): The URL of the Instagram reel.
        output_folder (str): Folder to save the downloaded reel.
    """
    try:
        # Get the page source
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the video URL in the page's metadata
        video_tag = soup.find("meta", property="og:video")
        if not video_tag:
            print("Could not find a video at the given URL. Please check the link.")
            return

        video_url = video_tag["content"]

        # Get the video content
        video_response = requests.get(video_url, stream=True)
        video_response.raise_for_status()

        # Ensure output folder exists
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Save the video file
        file_name = os.path.join(output_folder, "reel.mp4")
        with open(file_name, "wb") as video_file:
            for chunk in video_response.iter_content(chunk_size=1024):
                video_file.write(chunk)

        print(f"Reel downloaded successfully and saved as: {file_name}")

    except requests.exceptions.RequestException as e:
        print(f"Error during the download: {e}")

def main():
    print("Instagram Reel Downloader")
    reel_url = input("Enter the URL of the Instagram reel: ").strip()
    if not reel_url:
        print("URL cannot be empty. Please try again.")
        return

    download_instagram_reel(reel_url)

if __name__ == "__main__":
    main()
