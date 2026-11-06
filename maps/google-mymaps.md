# Google Maps / Google My Maps 导入指南

## 最稳妥方式

1. 打开 [Google My Maps](https://www.google.com/mymaps)，新建一张地图。
2. 在图层中选择「导入」，上传 `all-sites.kml`；若想分区管理，可改为分别导入 `by-city/` 中各城市 KML。
3. 单图层不建议无限堆叠。可按城市拆图层；精华点位另导入 `core-sites.kml`。
4. 点击标记可查看原始地点名称、城市、年代摘要及 Google Maps 检索链接。

## 坐标警告

源文件 `VCG/山西各市.kml` 内含 `<OvCoordType>CGCS2000</OvCoordType>` 标记。本项目保留源坐标，未擅自做 GCJ-02 / BD-09 转换。Google 地图底图常用 WGS84/全球地理定位体系，若导入后位置出现偏移，应先确认坐标转换方案，不能直接拖动标记掩盖系统差异。对精确导航请以现场道路和地图应用重新检索为准。

## 数据限制

KML 点位只代表来源地图上的标注，不代表可入内、开放、售票、道路可达或断代完成。学校、村委会、机关、住户范围内的地点，应先取得许可。
