# KCM Data Source Extractor  
此專案會產出KCM所能建立模型的資料  
分別來自Wiki、PTT、Dcard  
若使用者想要自行蒐集其他來源的語料  
然後建立KCM模型  
則請參照下列提供的資料格式  
即可將其語料當成輸入檔開始建立模型
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [KCM Data Source Extractor](#kcm-data-source-extractor)
  - [Getting Started](#getting-started)
    - [Prerequisities](#prerequisities)
    - [Installing](#installing)
  - [Running & Testing](#running--testing)
    - [Run](#run)
    - [Break down into end to end tests](#break-down-into-end-to-end-tests)
    - [And coding style tests](#and-coding-style-tests)
    - [Results](#results)
  - [Built With](#built-with)
  - [Contributors](#contributors)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisities

1. OS：Ubuntu / OSX would be nice
2. environment：need python3 `sudo apt-get update; sudo apt-get install; python3 python3-dev`

### Installing

1. `git clone https://github.com/UDICatNCHU/KCM-Data-Source-Extractor.git`
2. 使用虛擬環境：
  1. `virtualenv venv`
  2. 啟動方法
    1. for Linux：`. venv/bin/activate`
    2. for Windows：`venv\Scripts\activate`
3. `pip install -r requirements.txt`

## Running & Testing

### Run

1. 選擇你要的語料，進入下列資料夾執行`python main.py`進行下載：
  * [WikiPedia](WikiPedia/README.md)
  * Dcard
  * PTT

### Break down into end to end tests

目前還沒寫測試...

### And coding style tests

目前沒有coding style tests...

### Results
輸入資料沒有格式限制，將整段文字寫入檔案即可  
PTT輸入資料：

```
: 引述《LYCC (阿貓)》之銘言： : : 大家好，針對交通資位制，爬了國考版與公務員版許多文，但遍尋不著   
: : 心中的一些問題，懇請善心人士指教，謝謝。 : : 1. 交通資位制相關檔案(如制度薪資福利等條例)有官方網站可以參閱嗎？ : :   
還是受訓時老師們會特別講解？ : 交通資位制有很多種如果是公路總局的話公總的網站(公路園地)目前未對外開放 :   
受訓時我覺得也不會特別講解因為很多長官也搞不懂都以為交通資位制福利很好 : 因為單位不同薪資也不同.. 公路總局會辦新進人員講習課程   
會說明薪資福利相關內容 （沒有婚喪補助 子女教育津貼） : : 2. 今年簡章有特別提到本考試及格人員於取得考試及格之日起，於服務一年內不得 : :   
轉調原分發任用之主管機關及其所屬機關學校以外之機關學校任職 : : 此條款是說含受訓4個月，共1年4個月內不能申請調動到其他機關單位嗎？ : :   
yahoo某篇知識有人說受訓4個月完就可以申請調職，然後到新機關再進行實習受訓 : : 這方法行的通嗎？ : :   
另外，如果假如分發到交通部公路總局高雄區監理所屏東市， : : 在基礎訓期間，假如高雄區監理所底下之旗山台東有缺可以進去的話， : :   
可以不受1年4個月的限制嗎？ : : 又或者新竹區監理所有缺可以進去的話，可以不受1年4個月的限制嗎？ : 這就不清楚了請知道的人解答吧   
4個月受訓完成之後就可以請調交通部底下的所有單位 前提是長官要同意商調才可 通常有所謂的內規 先去探聽看看有沒有人請調成功過 一般來說還挺難的 : :   
3. 交通資位制於偏遠地區(如偏遠山區離島)，會有偏遠地區加給嗎？ : 偏遠地區及離島有加給.... 想薪水高的話就選外島或山區的單位  


```

## Built With


## Contributors

* **張泰瑋** [david](https://github.com/david30907d)

## License

## Acknowledgments
