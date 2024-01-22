import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cvm.v20170312 import cvm_client, models


class TencentCvmManager:
    def __init__(self, kid, key):
        self.cred = credential.Credential(kid, key)
        self.region = []
        httpProfile = HttpProfile()
        httpProfile.endpoint = "cvm.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        self.clientProfile = clientProfile

    def get_cvm_instances(self):
        req = models.DescribeRegionsRequest()
        region_client = cvm_client.CvmClient(self.cred, "", self.clientProfile)
        regions_resp = json.loads(region_client.DescribeRegions(req).to_json_string())
        regions = [region['Region'] for region in regions_resp['RegionSet']]  # 提取地区标识符
        with open('tmp', 'w', encoding='utf-8') as file:
            file.write(str(regions))
        for reg in regions:
            try:
                regional_client = cvm_client.CvmClient(self.cred, reg, self.clientProfile)
                instances_req = models.DescribeInstancesRequest()  # 对每个地区创建新的请求对象
                resp = regional_client.DescribeInstances(instances_req)
                print(resp.to_json_string())
            except TencentCloudSDKException as err:
                print("Error in region {}: {}".format(reg, err))
