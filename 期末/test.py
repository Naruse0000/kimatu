import MeCab
import unidic

tagger = MeCab.Tagger()  # 「tagger = MeCab.Tagger('-d ' + unidic.DICDIR)」
sample_txt = 'くるまでまつ'
result = tagger.parse(sample_txt)
print(result)