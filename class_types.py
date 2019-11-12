"""Parse Peloton class types."""

import requests


def main(
):
    """Parse Peloton class types."""
    metadata = requests.get(
        "https://api.onepeloton.com/api/ride/metadata_mappings",
    ).json()
    for class_type in metadata["class_types"]:
        if class_type["is_active"]:
            print(class_type["display_name"])


if __name__ == "__main__":
    main()
