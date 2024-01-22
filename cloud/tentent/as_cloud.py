import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.lighthouse.v20200324 import lighthouse_client, models

# todo 弹性伸缩暂不考虑
class TencentAsManager:
    def __init__(self, kid, key):
        self.cred = credential.Credential(kid, key)
        self.region = []
        httpProfile = HttpProfile()
        httpProfile.endpoint = "lighthouse.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        self.clientProfile = clientProfile