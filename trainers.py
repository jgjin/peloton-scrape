"""Parse Peloton trainers data."""

import requests


def main(
):
    """Parse Peloton trainers data."""
    trainers = requests.get(
        "https://api.onepeloton.com/api/instructor?limit=36",
    ).json()
    for trainer in trainers["data"]:
        name = trainer["name"]
        print(name)

        # url_types = [
        #     "life_style_image_url",
        #     "jumbotron_url",
        #     "jumbotron_url_dark",
        # ]
        # urls = dict(filter(
        #     lambda key_val: key_val is not None,
        #     map(
        #         lambda url_type: (url_type, trainer[url_type]) if trainer[url_type] else None,
        #         url_types,
        #     ),
        # ))

        # for url_type, img_url in urls.items():
        #     img_req = requests.get(img_url, stream=True)
        #     with open(f"assets/{name} {url_type}.jpg", "wb") as img_output:
        #         for chunk in img_req:
        #             img_output.write(chunk)


if __name__ == "__main__":
    main()
