from openai import AzureOpenAI
 
# Subscription Keyを入力します。
api_key = "1adb78a6e8914f489719ef8b9e76f21d"
 
# 接続処理をしてくれるクライアントクラスを作成します
client = AzureOpenAI(
    api_version="2024-10-01-preview",
    azure_endpoint="https://ifx-apim-01.azure-api.net",
    api_key=api_key
)
 
# Chat Completionメソッドで問い合わせをします。
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "What Can you do {{file}}?",
        },
    ],
)
print(completion.model_dump_json(indent=2))