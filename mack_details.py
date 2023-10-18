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


@app.post("/edapluginsapi/v1/stock/detail")
async def search_stock(data: dict):
    try:

        # 构建与上文代码相匹配的响应数据结构
        response = {
            "result": {
                "stock":{
                    "stockId": 2500335685,
                    #  "stock": {
                    #     "MPN": "Part123",
                    #     "Manufacturer": "ManufacturerX",
                    #     "Description": "This is a sample part",
                    #     "Package / Footprint": "SMD-0805",
                    #     "Category": "Electronics",
                    #     "Stock": 1000,
                    #     "Minimum Order Quantity(MOQ)": 10,
                    #     "priceStair": [
                    #         {"purchase": 10, "hkPrice": 5.00},
                    #         {"purchase": 50, "hkPrice": 4.50},
                    #         {"purchase": 100, "hkPrice": 4.00}
                    #     ],
                    #     "docUrl": "https://example.com/datasheet.pdf",
                    #     "goodsImage": ["https://example.com/part_image.jpg"]
                    # },

                    "categoryId": 1380,
                    "categoryName":"32-bit MCU Microcontrollers",
                    "docUrl":"//file.elecfans.com/web1/M00/D7/F3/pIYBAF_py8gAIrVAAA273UCSj1A254.pdf",
                    "encap":"LOFP48 7X7MM",
                    "goodsDesc": "32-bit MCU Micocontrollers 2.6V-3.6V LOFP48 7X7MM CPU core: ARM Cortex-M3 MaximurCPUfrequency: 108MHzRAM Total capacity: 20KB Number of GPIO ports: 37",
                    "goodsImage":[
                        "//fileelecfans.com/web2/M00/54/84/poYBAGLX2WuAC621AARJCagNT2s317,png!300!264?-t=1661802159"
                    ],
                    "goodsName":"GD32F103CBT6",
                    "goodsNo":"UNO004805",
                    "increment": 1,
                    "minBuynum": 1,
                    "pricestair": [
                        {
                        "cnPrice": 5.15000,
                        "hkPrice": 0.69945,
                        "purchase": 1,
                        }
                    ],
                    "providerName":"Gigadevice"
                }
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
                port=8081
                )
