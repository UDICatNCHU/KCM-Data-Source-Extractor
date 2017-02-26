from dcard import Dcard
import json, sys
topic = sys.argv[1]
num = int(sys.argv[2])

dcard = Dcard()
ariticle_metas = dcard.forums(topic).get_metas(num=num, sort='new')
articles = dcard.posts(ariticle_metas).get()
with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(articles.result(), f, ensure_ascii=False)
with open('output.kcm', 'w', encoding='utf-8') as f:
	for i in articles.results:
		f.write(i['title'] + '\n' + i['content'] + '\n'.join(map(lambda x: x.get('content', ''), i['comments'])) + '\n')
