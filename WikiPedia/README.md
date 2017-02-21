## WikiPedia 資料夾架構

* Directory：
  * langConfig：不同語言需要去抓不同的wiki資料然後分解、抓專有名詞來擴充字典，所以寫成不同的shell script (Each language writing in separated shellScript because having their own Wiki URL to get data.)
  * build：裏面事件立KCM model的程式。The programs of building KCM。
  * dictionary：dictionary used by jieba。
  * test：unit test python programs。
  * WikiRaw：
    * bz2：Raw Data downloaded from Wiki, having filename extension `bz2`. e.q. `zhwiki-20160501-pages-articles1.xml.bz2`
    * cht：directory extracted from bz2 Raw Data。e.q. `AA`、`AB` ...
    * preprocess_lib：
      * detectPN.py：Get more proper noun from title and text of Wiki, and append it into `jieba_expandDict` dict。
      * WikiExtractor.py：Extract articles from Raw Wiki Data
    * WikiPreProcessor.py：Start all the pre-processing program, including detectPN and WikiExtractor
