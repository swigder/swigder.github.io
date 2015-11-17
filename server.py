from bottle import route, run, template, static_file
from word_segmentation.bigram_word_segmenter import BigramWordSegmenter
from word_segmentation.brown_cmu_unigram_provider import BrownCmuUnigramProvider
from word_segmentation.brown_bigram_provider import BrownBigramProvider


unigram_provider = BrownCmuUnigramProvider()
bigram_provider = BrownBigramProvider()
segmenter = BigramWordSegmenter(unigram_provider, bigram_provider)


@route('/')
def index():
    return static_file('index.html', root='.')


@route('/js/<filename>')
def callback(filename):
    return static_file(filename, root='./js')


@route('/segment/<sentence>')
def segment(sentence='thisisasamplesentence'):
    return template('{{sentence}}....', sentence=" ".join(segmenter.segment_words(sentence)))


run(host='localhost', port=8080, debug=True)