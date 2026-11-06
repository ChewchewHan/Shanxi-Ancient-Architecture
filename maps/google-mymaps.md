# Google Maps / Google My Maps 匯入指南

## 最穩妥方式

1. 開啟 [Google My Maps](https://www.google.com/mymaps)，新建一張地圖。
2. 在圖層中選擇「匯入」，上傳 `all-sites.kml`；若想分割槽管理，可改為分別匯入 `by-city/` 中各城市 KML。
3. 單圖層不建議無限堆疊。可按城市拆圖層；精華點位另匯入 `core-sites.kml`。
4. 點選標記可檢視原始地點名稱、城市、年代摘要及 Google Maps 檢索連結。

## 座標警告

原始檔 `Bilibili 影片提供的地點資訊（整理後轉為 KML）` 內含 `<OvCoordType>CGCS2000</OvCoordType>` 標記。本專案保留源座標，未擅自做 GCJ-02 / BD-09 轉換。Google 地圖底圖常用 WGS84/全球地理定位體系，若匯入後位置出現偏移，應先確認座標轉換方案，不能直接拖動標記掩蓋系統差異。對精確導航請以現場道路和地圖應用重新檢索為準。

## 資料限制

KML 點位只代表來源地圖上的標註，不代表可入內、開放、售票、道路可達或斷代完成。學校、村委會、機關、住戶範圍內的地點，應先取得許可。
