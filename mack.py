from asyncio.log import logger
from http.client import HTTPException
from typing import Any
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from fastapi import FastAPI


def create_app() -> FastAPI:
    """
    实例化FastAPI
    :return: fastapi 实例
    :rtype: FastAPI
    """
    # 实例化
    return FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]
app = create_app()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {
        "result": {
            "total": 100,
            "stockList": [
                {"part_number": "12345", "description": "Component 1"},
                {"part_number": "67890", "description": "Component 2"}
            ]
        }
    }


@app.post("/edapluginsapi/v1/stock/search")
async def search_stock(data: dict):
    try:
        # 打印请求数据
        print("Received POST request data:", data)

        # 从请求数据中获取关键信息
        keyword = data.get("keyword")
        limit = data.get("limit")
        page = data.get("page")
        supplier = data.get("supplier")
        supplierSort = data.get("supplierSort")

        # 构建与上文代码相匹配的响应数据结构
        response = {
            "result": {
                "total": 100,  # 根据实际情况修改
                "stockList": [
                    {
                        "categoryId": 1380,
                        "categoryName": "32-bit MCU Microcontrollers",
                        "docUrl": "//file.elecfans.com/web1/M00/D7/F3/pIYBAF_py8qAIrvAAAz73UCSj1A254.pdf",
                        "encap": "LQFP48_7X7MM",
                        "goodsDesc": "32-bit MCU Microcontrollers  2.6V~3.6V LQFP48_7X7MM CPU core: ARM Cortex-M3 Maximum CPU frequency: 108MHz Program storage capacity: 128KB Program memory type: FLASH RAM Total capacity: 20KB Number of GPIO ports: 37",
                        "goodsImage": [
                            "//file.elecfans.com/web2/M00/54/84/poYBAGLXzWuAc62lAARJCagNT2s317.png!300!264?_t=1661802159"
                        ],
                        "goodsName": "GD32F103CBT6",
                        "goodsNo": "UN0004805",
                        "increment": 1,
                        "minBuynum": 1,
                        "priceStair": [
                            {
                                "cnPrice": 5.15000,
                                "hkPrice": 0.70303,
                                "purchase": 1
                            }
                        ],
                        "providerName": "Gigadevice",
                        "stockId": "2500335685",
                        "stockNumber": "74",
                        "supplierName": "NextPCB",
                        "usExchangeRate": 7.325400
                    },
                    {
                        "goodsName": "GD32F103CBT6",
                        "providerName": "Gigadevice",
                        "goodsDesc": "32-bit MCU Microcontrollers  2.6V~3.6V LQFP48_7X7MM CPU core: ARM Cortex-M3 Maximum CPU frequency: 108MHz Program storage capacity: 128KB Program memory type: FLASH RAM Total capacity: 20KB Number of GPIO ports: 37",
                        "encap": "LQFP48_7X7MM",
                        "stockNumber": "2500335685",
                        "priceStair": [
                            {
                                "cnPrice": 5.15000,
                                "hkPrice": 0.70303,
                                "purchase": 1
                            }
                        ],
                        "supplierName": "Supplier A",
                        "stockId": 2500335685
                    },
                    {
                        "goodsName": "CPart3",
                        "providerName": "Manufacturer2",
                        "goodsDesc": "Description2",
                        "encap": "Package2",
                        "stockNumber": "2500335685",
                        "priceStair": [{"hkPrice": 30.0}],
                        "supplierName": "Supplier C",
                        "stockId": 2500335685
                    },

                ]
            }
        }

        return response
    except Exception as e:
        # 捕获异常并记录日志
        logger.error(f"An errred: {str(e)}")
        # 返回适当的错误响应
        # raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == '__main__':
    uvicorn.run('mack:app',
                host='127.0.0.2',
                port=8080
                )
