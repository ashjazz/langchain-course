from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os

load_dotenv()

OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_MODEL_NAME = os.environ.get("OPENAI_MODEL_NAME")

def main():
    print("Hello from langchain-course!\n")
    information = """
    埃隆·里夫·马斯克（英语：Elon Reeve Musk /ˈiːlɔːn/；1971年6月28日—），汉名马谊郎[注 3]，世界首富、商业大亨、英国皇家学会会士[注 4]、美国工程院院士[6]。他是SpaceX的创始人、董事长、首席执行官、首席工程师，特斯拉投资人、首席执行官、产品设计师、前董事长，无聊公司创始人，Neuralink、OpenAI联合创始人，同时也是X公司的首席技术官、董事长。2022年马斯克以2190亿美元财富成为世界首富，其后随着旗下公司的股价暴涨，其资产亦同时急剧增加，[7]随着SpaceX于2026年6月在美国纳斯达克上市，其拥有的个人财富突破1万亿美元，成为人类史上首位万亿富豪[8]。

马斯克在南非德兰士瓦省比勒陀利亚长大，曾短暂就读于比勒陀利亚大学，后于18岁移居加拿大就读女王大学。两年后，他转学到宾夕法尼亚大学，并获得经济学、物理学的学士学位。1995年，他搬到加利福尼亚州并就读于斯坦福大学，而后决定从商。他与弟弟金巴尔共同创办了网络软件公司Zip2。1999年，康柏公司以3.07亿美元收购了这家初创企业。同年，马斯克联合创办了在线银行X.com。2000年，该公司与Confinity合并为PayPal。2002年，EBay以15亿美元买下PayPal。

2002年，马斯克创办SpaceX，并担任董事长、首席执行官、首席技术官，该公司主要负责太空运输、航太制造。2004年，他加入电动车制造商特斯拉，并担任董事长与产品设计师，2008年兼任首席执行官。2006年，他协助创立太阳能服务公司SolarCity，该公司后成为特斯拉子公司特斯拉能源。2015年，他联合创办了非营利公司OpenAI，用于研究和推动友善人工智能。2016年，他联合创办了神经科技公司Neuralink，该公司专注于开发脑机接口。同年，他成立了无聊隧道施工公司，用于研发超回路列车。[注 5]2022年10月27日，马斯克以440亿美元收购社交平台Twitter，日后改组为X。2021年10月，美国商业杂志《福布斯》宣布马斯克财富达到2700亿美元，成为该杂志统计史上最富有的人[9]。2024年11月，美国总统当选人唐纳德·特朗普宣布委任马斯克为总统高级顾问，领导新创立的政府效率部[10]。

马斯克因被认为曾发表误导性或违背科学的言论以及传播关于COVID-19的错误信息而受到批评；在人工智能、加密货币、公共交通等方面的观点亦受到部分专家的批评。此外，马斯克旗下的特斯拉公司在各方面皆充满争议。
    """

    summary_template = """
    给到的信息 {information} 是关于一个人物的描述, 你需要给出以下内容：
    - 一个简短的总结
    - 关于这个人物的两个有趣的事实
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )

    llm = ChatOpenAI(
        base_url=OPENAI_BASE_URL,
        temperature=0,
        model=OPENAI_MODEL_NAME,
        api_key=OPENAI_API_KEY,
    )

    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})
    print(response)


if __name__ == "__main__":
    main()
