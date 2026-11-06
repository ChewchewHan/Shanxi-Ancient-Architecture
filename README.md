# 山西古建檔案庫（Shanxi Ancient Architecture）

> 面向實地訪古、建築史學習與自駕規劃的持續更新資料庫。重點記錄山西現存古建築的地點、歷史年代、建築本體、彩塑壁畫、開放狀態、導航座標和可追溯來源。

## 項目原則

1. **先記錄實物，再討論年代。** 寺院始建年代、現存殿堂建造年代、塑像/壁畫年代、歷代維修年代分開記錄。
2. **來源可追溯。** 重要歷史判斷鏈接官方文物單位、政府部門、專業院校、正式調查報告或學術出版物。
3. **不把地圖標記當作開放證明。** 村內、學校、機關、寺院看護區域及維修中的地點，必須另行確認進入方式。
4. **不確定就標待覈實。** 未查到可信證據的年代、地址、門票和開放信息，不猜測、不補造。
5. **地圖座標保留來源信息。** 原始 KML 對各地點標記 `CGCS2000`。導入 Google Earth / Google My Maps 後應抽樣覈對座標偏移。

## 當前數據（v0.1 初始化）

- 點位按原始城市文件夾分組；名稱、座標和來源鏈接保留。
- 449條是地圖線索，不代表449處均爲國家級文保單位、全部開放或已經完成斷代。
- 首批建立 **20處重點考察 KML 標記** 與 **20份重點古建專題檔案**。
- 重點檔案的斷代等級分A/B；其他點位初始統一標作待覈實。後續按證據逐條升級。

## 快速入口

| 需要什麼 | 文件 |
|---|---|
| 完整地名、座標、來源 | [data/sites.csv](data/sites.csv) |
| GitHub網頁可直接瀏覽的449處清單 | [data/all-sites.md](data/all-sites.md) |
| 程序讀取數據 | [data/sites.json](data/sites.json) |
| 449處全部地圖標記 | [maps/all-sites.kml](maps/all-sites.kml) |
| 20處重點考察點 | [maps/core-sites.kml](maps/core-sites.kml) |
| 各市獨立地圖圖層 | [maps/by-city/](maps/by-city/) |
| Google My Maps 導入說明 | [maps/google-mymaps.md](maps/google-mymaps.md) |
| 城市數量目錄 | [data/city-index.md](data/city-index.md) |
| 重點建築專題檔案 | [places/README.md](places/README.md) |
| 斷代與來源目錄 | [sources/README.md](sources/README.md) |
| 30天自駕路線 | [itineraries/30-day-self-drive.md](itineraries/30-day-self-drive.md) |
| 重點路線地圖點位 | [itineraries/30-day-route-points.md](itineraries/30-day-route-points.md) |
| 如何用本倉庫規劃旅行 | [itineraries/how-to-use-this-repository-with-chatgpt.md](itineraries/how-to-use-this-repository-with-chatgpt.md) |

## 城市分佈

| 城市 | 地點數 |
|---|---:|
| 大同 | 19 |
| 朔州 | 5 |
| 忻州 | 32 |
| 太原 | 27 |
| 陽泉 | 11 |
| 呂梁 | 33 |
| 晉中 | 59 |
| 長治 | 70 |
| 晉城 | 71 |
| 臨汾 | 44 |
| 運城 | 78 |
| **合計** | **449** |

## 字段與斷代

字段解釋見 [data/data-dictionary.md](data/data-dictionary.md)。

- `construction_period`：具體現存建築或構件年代。
- `founding_period`：寺院/廟宇創建年代。
- `dating_status`：待覈實、部分覈實或已覈實。
- `source_confidence`：A/B/C資料證據等級，不是文物保護級別。
- `access_checked_at`：開放狀態最後覈查日；空白代表未覈查，不代表開放或關閉。

## Google 地圖

打開 [Google My Maps](https://www.google.com/mymaps)，新建地圖，選擇導入並上傳 `maps/all-sites.kml`。建議再單獨導入 `maps/core-sites.kml`。詳情見 [導入說明](maps/google-mymaps.md)。

座標注意：原始文件標註CGCS2000，未在倉庫內擅自做GCJ-02/BD-09轉換。Google地圖或國內地圖導入後，如有偏移先覈驗座標系，不要直接拖動標記來掩蓋偏移。道路入口須另行覈對。

## 開放與票務

本倉庫是長期歷史資料庫，不是實時票務接口。開放時間、維修閉館、預約渠道、票價、庫存和道路狀況均會變化。每次出行應另查景區/文物管理單位的最新公告並記錄覈查日期。

## 許可和貢獻

資料補充、考據修正和開放狀態更新的規則見 [CONTRIBUTING.md](CONTRIBUTING.md)。

本倉庫以獨立整理的地點名稱、座標、考據摘要和外部來源鏈接爲主。原始地圖數據權利歸原提供者/權利人所有；轉載圖片、測繪圖、書籍掃描和整篇文章前應確認授權。歡迎提供出處明確、能指出具體建築構件或碑刻證據的修訂建議。

建議保護 `main` 分支；通過 Pull Request 審覈新增年代和開放信息，避免未經覈實的修改進入正式目錄。
