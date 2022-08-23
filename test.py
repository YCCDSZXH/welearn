import requests
import urllib.parse
# from urllib import unquote
session = requests.session()
response = session.get("https://welearn.sflep.com/user/prelogin.aspx?loginret=http://welearn.sflep.com/user/loginredirect.aspx")
rturl = urllib.parse.unquote(response.url).split("returnUrl=")[1]
print()

data = {
    'rturl': rturl,
    'account': '11111111111',
    'pwd': 'Aa112211',
}
# session.headers = headers

response = session.post('https://sso.sflep.com/idsvr/account/login',data=data)
print(response.text)
# # print(session.cookies)
resp = session.get("https://sso.sflep.com/idsvr"+rturl)
print(resp.text)
session.headers={"Referer": "https://welearn.sflep.com/student/index.aspx"}
# print("https://sso.sflep.com/idsvr"+rturl)
# print(resp.status_code)
# https://sso.sflep.com/idsvr/connect/authorize/callback?client_id=welearn_web&redirect_uri=https://welearn.sflep.com/signin-sflep&response_type=code&scope=openid profile email phone address&code_challenge=PEG2Xt_2d5EbaoPkuKd3lrZRxkkOAgmmajkUECmT514&code_challenge_method=S256&state=OpenIdConnect.AuthenticationProperties=4lpIMKnUGLC-rwSMjgCiVlgESoYKrpZR3d-U5X9bzek9eKUzS9YjHsS1MmQ4_MquaQ_PVtsYYC_v23Xw1HtObXWHy1l8mz_VizOz9hbSKZZhnMyvQqEUqNgx8j7ekTMUgStBe3bvfPBYhxowkjx2oh7Ssmn7Spawyj8DSFm0H0_XYm0Vky41c1MehIa3g4nWyIAVv8guArnFkSckm59s2_c0FeA_FE_zOBjfvwUhtw1OryXVvh9VqhZdcot6tHmMxuO-esHujoWrMCG_mSeASkYdgod55Qf--4ua3oMBcr-pIx5sEs8nFPs5b3mNffnW7sq80MyYTTgbcWtWyxSI9A&x-client-SKU=ID_NET472&x-client-ver=6.16.0.0
# https://sso.sflep.com/idsvr/connect/authorize/callback%3Fclient_id%3Dwelearn_web%26redirect_uri%3Dhttps%253A%252F%252Fwelearn.sflep.com%252Fsignin-sflep%26response_type%3Dcode%26scope%3Dopenid%2520profile%2520email%2520phone%2520address%26code_challenge%3DPt9uLHaHsDBFJvtog06QuGHAeuRIqokGji4jd7U-FfY%26code_challenge_method%3DS256%26state%3DOpenIdConnect.AuthenticationProperties%253DjKENTqKBmLf1c6wVF_e7OkUReCZLJkgIaZnObb9RjvkGsXlcKevymP7frgMQXY1Ck6B4iFX2IfZeGRFF_7MdCEiTOAlQN16tCLxD5Wj9lR6i8-IpNA_b134ZGLGVqIm-oynJJtBWpXxZEyY5JF5kBO9l7thrXVc_-hQXZ3eM586Vltxkxe-ZIzroNmZ6Mwr-pJZUNjiLcQYPQO3Bb0CwXolxPbdm7uTAWruZQlYugHBIjp_L300p2X8wMT9fxRzNuOP_9b3GGP6oVvRvbCfwD6Jbm4KM3YxLVjBUK3V8zx7oLHDX11DWztEf5krxVkO24tMO_zj6QhhXAGNGeZJF1w%26x-client-SKU%3DID_NET472%26x-client-ver%3D6.16.0.0
response = session.get("https://welearn.sflep.com/ajax/authCourse.aspx?action=gmc")
print(response.text)
