import sys
sys.path.append('/usr/local/server')
import command as c

symbols = ['flm','orbs','arpa','iota','band','bel','edu','loom','tlm','fxs','hook','people','unfi','agld','glmr','joe','iost','mav','xlm','astr','uma','cyber','bake','knc','gmt','mdt','rose','id','ksm','qnt','ssv','key','nkn','meme','zrx','chr','pyth','rdnt','rsr','lrc']
als=[i+'_bg3.py' for i in symbols]
print(als)
c.startAll(als, sleepTime=0.1)
