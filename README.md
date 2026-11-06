# 山西古建档案库（Shanxi Ancient Architecture）

> 面向实地访古、建筑史学习与自驾规划的持续更新资料库。重点记录山西现存古建筑的地点、历史年代、建筑本体、彩塑壁画、开放状态、导航坐标和可追溯来源。

## 项目原则

1. **先记录实物，再讨论年代。** 寺院始建年代、现存殿堂建造年代、塑像/壁画年代、历代维修年代分开记录。
2. **来源可追溯。** 重要历史判断链接官方文物单位、政府部门、专业院校、正式调查报告或学术出版物。
3. **不把地图标记当作开放证明。** 村内、学校、机关、寺院看护区域及维修中的地点，必须另行确认进入方式。
4. **不确定就标待核实。** 未查到可信证据的年代、地址、门票和开放信息，不猜测、不补造。
5. **地图坐标保留来源信息。** 原始 KML 对各地点标记 `CGCS2000`。导入 Google Earth / Google My Maps 后应抽样核对坐标偏移。

## 当前数据（v0.1 初始化）

- 从 [ChewchewHan/VCG](https://github.com/ChewchewHan/VCG) 的 `山西各市.kml` 中整理出 **449条古建地点记录**，覆盖11个地级市。
- 点位按原始城市文件夹分组；名称、坐标和来源链接保留。
- 449条是地图线索，不代表449处均为国家级文保单位、全部开放或已经完成断代。
- 首批建立 **20处重点考察 KML 标记** 与 **19份重点古建专题档案**。
- 重点档案的断代等级分A/B；其他点位初始统一标作待核实。后续按证据逐条升级。

## 快速入口

| 需要什么 | 文件 |
|---|---|
| 完整地名、坐标、来源 | [data/sites.csv](data/sites.csv) |\n| GitHub网页可直接浏览的449处清单 | [data/all-sites.md](data/all-sites.md) |
| 程序读取数据 | [data/sites.json](data/sites.json) |
| 449处全部地图标记 | [maps/all-sites.kml](maps/all-sites.kml) |
| 20处重点考察点 | [maps/core-sites.kml](maps/core-sites.kml) |
| 各市独立地图图层 | [maps/by-city/](maps/by-city/) |
| Google My Maps 导入说明 | [maps/google-mymaps.md](maps/google-mymaps.md) |
| 城市数量目录 | [data/city-index.md](data/city-index.md) |
| 重点建筑专题档案 | [places/README.md](places/README.md) |
| 断代与来源目录 | [sources/README.md](sources/README.md) |
| 30天自驾路线 | [itineraries/30-day-self-drive.md](itineraries/30-day-self-drive.md) |
| 重点路线地图点位 | [itineraries/30-day-route-points.md](itineraries/30-day-route-points.md) |
| 如何用本仓库规划旅行 | [itineraries/how-to-use-this-repository-with-chatgpt.md](itineraries/how-to-use-this-repository-with-chatgpt.md) |

## 城市分布

| 城市 | 地点数 |
|---|---:|
| 大同 | 19 |
| 朔州 | 5 |
| 忻州 | 32 |
| 太原 | 27 |
| 阳泉 | 11 |
| 吕梁 | 33 |
| 晋中 | 59 |
| 长治 | 70 |
| 晋城 | 71 |
| 临汾 | 44 |
| 运城 | 78 |
| **合计** | **449** |

## 字段与断代

字段解释见 [data/data-dictionary.md](data/data-dictionary.md)。

- `construction_period`：具体现存建筑或构件年代。
- `founding_period`：寺院/庙宇创建年代。
- `dating_status`：待核实、部分核实或已核实。
- `source_confidence`：A/B/C资料证据等级，不是文物保护级别。
- `access_checked_at`：开放状态最后核查日；空白代表未核查，不代表开放或关闭。

## Google 地图

打开 [Google My Maps](https://www.google.com/mymaps)，新建地图，选择导入并上传 `maps/all-sites.kml`。建议再单独导入 `maps/core-sites.kml`。详情见 [导入说明](maps/google-mymaps.md)。

坐标注意：原始文件标注CGCS2000，未在仓库内擅自做GCJ-02/BD-09转换。Google地图或国内地图导入后，如有偏移先核验坐标系，不要直接拖动标记来掩盖偏移。道路入口须另行核对。

## 开放与票务

本仓库是长期历史资料库，不是实时票务接口。开放时间、维修闭馆、预约渠道、票价、库存和道路状况均会变化。每次出行应另查景区/文物管理单位的最新公告并记录核查日期。

## 许可和贡献

资料补充、考据修正和开放状态更新的规则见 [CONTRIBUTING.md](CONTRIBUTING.md)。

本仓库以独立整理的地点名称、坐标、考据摘要和外部来源链接为主。原始地图数据权利归原提供者/权利人所有；转载图片、测绘图、书籍扫描和整篇文章前应确认授权。欢迎提供出处明确、能指出具体建筑构件或碑刻证据的修订建议。

建议保护 `main` 分支；通过 Pull Request 审核新增年代和开放信息，避免未经核实的修改进入正式目录。
