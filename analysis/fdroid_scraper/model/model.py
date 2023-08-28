from dataclasses import dataclass, asdict
from enum import Enum
class ExternalDataSourceVendor(Enum):
    GITHUB = "github.com"
    GITLAB = "gitlab.com"
    OTHER = "other"

    def __repr__(self) -> str:
        return super().__repr__()

class ExternalDataSource:
    address: str
    vendor: ExternalDataSourceVendor

@dataclass
class ApplicationInfo:
    package_name: str
    name: str
    category: str
    version: str
    issue_tracker: ExternalDataSourceVendor
    source_code: ExternalDataSourceVendor
    changelog: ExternalDataSourceVendor
    build_metadata: ExternalDataSourceVendor

@dataclass
class PackageSummary:
    name: str
    package: str
    summary: str
    category: str
    link: str

    def to_dict(self):
        return asdict(self)
