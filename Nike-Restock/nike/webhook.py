from datetime import datetime
import requests


def webhook_titan(data: dict):
    print("[BACKEND] Sending webhook...")

    url = f"https://www.nike.com/il/t/{data['slug']}/{data['styleColor']}"

    webhook = "https://discord.com/api/webhooks/1210945515970232391/K7_AMKP5bx37xJDIL7lXkHxmC12CrHC-QsMC6ARBRWAU4QFmENh79k6lVudts51Us2Dr"
    logo_titan = "https://s7.ezgif.com/tmp/ezgif-7-75b3768ab3.png"

    embee = []

    array_channels = ""
    for channel in data["channels"]:
        array_channels += f"{channel}\n"

    embee.append({"name": "Status", "value": data["status"], "inline": True})
    embee.append({"name": "SKU", "value": data["styleColor"], "inline": True})
    embee.append({"name": "Region", "value": ":flag_il:", "inline": False})
    embee.append(
        {
            "name": "Available at",
            "value": "```\n" + array_channels + "```",
            "inline": False,
        }
    )
    embee.append({"name": "Available", "value": str(data["available"]), "inline": True})
    embee.append(
        {"name": "Price", "value": str(data["fullPrice"]) + "₪", "inline": False}
    )

    # based of the size of the line data["size"]

    line = len(data["size"].splitlines())
    number_of_element = line / 5
    number_of_element = int(number_of_element)

    for i in range(number_of_element):
        # create a list of 5 elements
        list_of_5 = data["size"].splitlines()[i * 5 : (i + 1) * 5]
        # join the list of 5 elements
        list_of_5 = "\n".join(list_of_5)

        embee.append({"name": "Size", "value": list_of_5, "inline": True})

    current_time = datetime.now().strftime("%I:%M %p")

    data = {
        "username": "Portal",
        "avatar_url": logo_titan,
        "embeds": [
            {
                "title": data["title"],
                "url": url,
                "color": 12298642,
                "thumbnail": {"url": data["imageUrls"]},
                "fields": embee,
                "footer": {
                    "text": "Portal Monitors" + " • Today at " + current_time,
                    "icon_url": logo_titan,
                },
            }
        ],
    }

    response = requests.post(webhook, json=data)
    try:
        response.raise_for_status()
        print("[BACKEND] Webhook sent!")

    except requests.exceptions.HTTPError as err:
        print(err)
    except:
        print("[BACKEND] Webhook failed!")


def webhook_uzumaki(data: dict):
    print("[BACKEND] Sending webhook...")

    url = f"https://www.nike.com/il/t/{data['slug']}/{data['styleColor']}"

    webhook = "https://discord.com/api/webhooks/1210945515970232391/K7_AMKP5bx37xJDIL7lXkHxmC12CrHC-QsMC6ARBRWAU4QFmENh79k6lVudts51Us2Dr"
    logo_uzumaki = "https://s7.ezgif.com/tmp/ezgif-7-75b3768ab3.png"

    embee = []

    array_channels = ""
    for channel in data["channels"]:
        array_channels += f"{channel}\n"

    embee.append({"name": "Status", "value": data["status"], "inline": True})
    embee.append({"name": "SKU", "value": data["styleColor"], "inline": True})
    embee.append({"name": "Region", "value": ":flag_il:", "inline": False})
    embee.append(
        {
            "name": "Available at",
            "value": "```\n" + array_channels + "```",
            "inline": False,
        }
    )
    embee.append({"name": "Available", "value": str(data["available"]), "inline": True})
    embee.append(
        {"name": "Price", "value": str(data["fullPrice"]) + "₪", "inline": False}
    )

    # based of the size of the line data["size"]

    line = len(data["size"].splitlines())
    number_of_element = line / 5
    number_of_element = int(number_of_element)

    for i in range(number_of_element):
        # create a list of 5 elements
        list_of_5 = data["size"].splitlines()[i * 5 : (i + 1) * 5]
        # join the list of 5 elements
        list_of_5 = "\n".join(list_of_5)

        embee.append({"name": "Size", "value": list_of_5, "inline": True})

    current_time = datetime.now().strftime("%I:%M %p")

    data = {
        "username": "Portal",
        "avatar_url": logo_uzumaki,
        "embeds": [
            {
                "title": data["title"],
                "url": url,
                "color": 12298642,
                "thumbnail": {"url": data["imageUrls"]},
                "fields": embee,
                "footer": {
                    "text": "Portal Monitors" + " • Today at " + current_time,
                    "icon_url": logo_uzumaki,
                },
            }
        ],
    }

    response = requests.post(webhook, json=data)
    try:
        response.raise_for_status()
        print("[BACKEND] Webhook sent!")

    except requests.exceptions.HTTPError as err:
        print(err)
    except:
        print("[BACKEND] Webhook failed!")
