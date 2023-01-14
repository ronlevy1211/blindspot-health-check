import requests


class NPMPackage:
    def __init__(self, package_name):
        self.repository_url = None
        self.maintainers = None
        self.date = None
        self.package_name = package_name
        self.url = f"https://registry.npmjs.org/{package_name}/latest"

    def get_package_info(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            latest_package_info = response.json()
            latest_version = latest_package_info["version"]
            response = requests.get(self.url.replace("/latest", ""))
            package_info = response.json()
            self.date = package_info["time"][latest_version]
            self.maintainers = package_info["maintainers"]
            self.repository_url = package_info["repository"]["url"]
        else:
            raise ValueError(f'Unable to fetch information for {self.package_name},status code: {response.status_code}')

    def __str__(self):
        return f'Package: {self.package_name}\nLatest version: {self.latest_version}\nDate of latest version: {self.date}\nMaintainers: {self.maintainers}\nRepository URL: {self.repository_url}'
