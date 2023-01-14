import datetime
import requests
import re
import logging
from datetime import timedelta
from models.AuthGen.AuthGen import AuthGen
from models.NPMPackage.NPMPackage import NPMPackage


class HealthCheck:
    def __init__(self, package_name):
        self.package_name = package_name
        self.response = {'package_name': package_name, 'version_date_validation': True, 'maintainers_validation': True,
                         'repository_commit_validation': True}
        self.package = NPMPackage(package_name)

    def check_version_date(self):
        date_30_days_ago = datetime.datetime.now() - timedelta(days=30)
        version_date = datetime.datetime.strptime(self.package.date, "%Y-%m-%dT%H:%M:%S.%fZ")
        if version_date < date_30_days_ago:
            return False
        return True

    def check_maintainers(self):
        if len(self.package.maintainers) < 2:
            return False
        return True

    def check_repository_commit(self):
        repository_url = self.package.repository_url
        match = re.search(r"(.+)://github\.com/(.+)/(.+)\.git", repository_url)
        owner = match.group(2)
        repo = match.group(3)
        auth = AuthGen("config.ini")
        token = auth.get_token("GitHub", "token")
        headers = {'Authorization': f'token {token}'}
        response = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits", headers=headers)
        data = response.json()
        latest_commit_date = data[0]["commit"]["committer"]["date"]
        last_commit_date = datetime.datetime.strptime(latest_commit_date, "%Y-%m-%dT%H:%M:%SZ")
        date_14_days_ago = datetime.datetime.now() - timedelta(days=14)
        if last_commit_date < date_14_days_ago:
            return False
        return True

    def security_check(self):
        self.package.get_package_info()
        if not self.check_version_date():
            logging.warning(f"{self.package_name} is not secure: Last version is more than 30 days old.")
            self.response['version_date_validation'] = False
        if not self.check_maintainers():
            logging.warning(f"{self.package_name} is not secure: Less than 2 maintainers.")
            self.response['maintainers_validation'] = False
        if not self.check_repository_commit():
            logging.warning(f"{self.package_name} is not secure: Last commit in repository is more than 14 days old.")
            self.response['repository_commit_validation'] = False
        return str(self.response)
