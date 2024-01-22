from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdb.v20170320 import cdb_client, models
from cloud.tentent.Bean import Bean


class TencentMysqlManager:
    def __init__(self, kid, key):
        self.cred = credential.Credential(kid, key)
        self.region = Bean().get_region()
        httpProfile = HttpProfile()
        httpProfile.endpoint = "cdb.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        self.clientProfile = clientProfile

    def get_cdb_instances(self):
        req = models.DescribeDBInstancesRequest()
        regions = self.region
        for region in regions:
            try:
                client = cdb_client.CdbClient(self.cred, region, self.clientProfile)
                req = models.DescribeDBInstancesRequest()
                resp = client.DescribeDBInstances(req)
                print(resp.to_json_string())
            except TencentCloudSDKException as err:
                print("Error in region {}: {}".format(region, err))

