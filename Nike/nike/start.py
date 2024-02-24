import requests
import time
from datetime import datetime

logo = "https://s7.ezgif.com/tmp/ezgif-7-75b3768ab3.png"

headers = {
    "authority": "api.nike.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": '"Chromium";v="112", "Brave";v="112", "Not:A-Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "sec-gpc": "1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
}


def webhook(payload):
    print("[BACKEND] Sending webhook...")
    webhook_url = "https://discord.com/api/webhooks/1210945515970232391/K7_AMKP5bx37xJDIL7lXkHxmC12CrHC-QsMC6ARBRWAU4QFmENh79k6lVudts51Us2Dr"
    response = requests.post(webhook_url, json=payload)
    try:
        response.raise_for_status()
        print("[BACKEND] Webhook sent!")
    except requests.exceptions.HTTPError as err:
        print(err)
    except:
        print("[BACKEND] Webhook failed!")


def start():
    print("[BACKEND] Starting thread...")
    first_run = True
    ids = []

    url = "https://api.nike.com/product_feed/rollup_threads/v2?filter=marketplace(IL)&filter=language(en)&filter=employeePrice(true)&filter=attributeIds(16633190-45e5-4830-a068-232ac7aea82c,193af413-39b0-4d7e-ae34-558821381d3f,53e430ba-a5de-4881-8015-68eb1cff459f)&anchor=0&consumerChannelId=d9a5bc42-4b9c-4976-858a-f159cf99c647&count=60&sort=effectiveStartViewDateDesc"

    while True:
        try:
            print("[BACKEND] Getting data...")
            response = requests.get(url, headers=headers)
            data = response.json()
            print("[BACKEND] Successful got data.")

            if first_run:
                id = data["objects"][0]["id"]
                ids.append(id)
                print("[BACKEND] Adding ID (first run): {}".format(id))
                first_run = False
            else:
                print("[BACKEND] Checking for new IDs...")

                id = data["objects"][0]["id"]
                if id not in ids:
                    ids.append(id)
                    print("[BACKEND] Adding ID: {}".format(id))
                    # get product info

                    product_info = data["objects"][0]["productInfo"][0]["merchProduct"]
                    status = product_info["status"]
                    style_color = product_info["styleColor"]
                    channels = product_info["channels"]
                    exclusive_access = product_info["exclusiveAccess"]
                    try:
                        publish_type = product_info["publishType"]
                    except:
                        publish_type = None

                    image_urls = data["objects"][0]["productInfo"][0]["imageUrls"]["productImageUrl"]
                    full_price = data["objects"][0]["productInfo"][0]["merchPrice"]["fullPrice"]
                    available = data["objects"][0]["productInfo"][0]["availability"]["available"]
                    title = data["objects"][0]["productInfo"][0]["productContent"]["title"]
                    slug = data["objects"][0]["productInfo"][0]["productContent"]["slug"]

                    # get launch info
                    try:
                        method = data["objects"][0]["productInfo"][0]["launchView"]["method"]
                        start_entry_date = data["objects"][0]["productInfo"][0]["launchView"]["startEntryDate"]
                    except:
                        method = None
                        start_entry_date = None

                    payload = {
                        "status": status,
                        "styleColor": style_color,
                        "channels": channels,
                        "exclusiveAccess": exclusive_access,
                        "imageUrls": image_urls,
                        "fullPrice": full_price,
                        "available": available,
                        "title": title,
                        "slug": slug,
                        "method": method,
                        "startEntryDate": start_entry_date,
                        "publishType": publish_type,
                    }

                    webhook(payload)

                print("[BACKEND] Sleeping for 300 seconds...")
                time.sleep(300)

        except Exception as e:
            print("[BACKEND] Error: {}".format(e))
            continue


start()
