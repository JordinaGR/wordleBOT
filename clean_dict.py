import pandas as pd
import numpy as np

df = pd.read_csv('diccionarimod.csv')

# df = df[~df.paraules.str.contains("aaa")]
# df = df[~df.paraules.str.contains("bbb")]
# df = df[~df.paraules.str.contains("ccc")]
# df = df[~df.paraules.str.contains("ddd")]
# df = df[~df.paraules.str.contains("eee")]
# df = df[~df.paraules.str.contains("ff")]
# df = df[~df.paraules.str.contains("gg")]
# df = df[~df.paraules.str.contains("hh")]
# df = df[~df.paraules.str.contains("iii")]
# df = df[~df.paraules.str.contains("jj")]
# df = df[~df.paraules.str.contains("kk")]
# df = df[~df.paraules.str.contains("lll")]
# df = df[~df.paraules.str.contains("mmm")]
# df = df[~df.paraules.str.contains("nnn")]
# df = df[~df.paraules.str.contains("ooo")]
# df = df[~df.paraules.str.contains("pp")]
# df = df[~df.paraules.str.contains("qq")]
# df = df[~df.paraules.str.contains("rrr")]
# df = df[~df.paraules.str.contains("sss")]
# df = df[~df.paraules.str.contains("tt")]
# df = df[~df.paraules.str.contains("uuu")]
# df = df[~df.paraules.str.contains("vv")]
# df = df[~df.paraules.str.contains("ww")]
# df = df[~df.paraules.str.contains("xx")]
# df = df[~df.paraules.str.contains("yy")]
# df = df[~df.paraules.str.contains("zz")]
# df = df[~df.paraules.str.contains("11")]

# df = df[df.paraules.str.contains('a|e|i|o|u')==True]

# df = df[~df.paraules.str.contains("1i")]
# df = df[~df.paraules.str.contains("1e")]

# df = df[~df.paraules.str.startswith('rr')]
# df = df[~df.paraules.str.startswith('ss')]
# df = df[~df.paraules.str.startswith('aa')]
# df = df[~df.paraules.str.startswith('ee')]
# df = df[~df.paraules.str.startswith('ii')]
# df = df[~df.paraules.str.startswith('1')]
# df = df[~df.paraules.str.startswith('y')]

# df = df[~df.paraules.str.endswith('z')]
# df = df[~df.paraules.str.endswith('h')]
# df = df[~df.paraules.str.endswith('w')]
# df = df[~df.paraules.str.endswith('q')]
# df = df[~df.paraules.str.endswith('j')]

# df = df[~df.paraules.str.contains("cz")]
# df = df[~df.paraules.str.contains("z1")]
# df = df[~df.paraules.str.contains("vb")]
# df = df[~df.paraules.str.contains("nm")]
# df = df[~df.paraules.str.contains("gh")]
# df = df[~df.paraules.str.contains("qw")]
# df = df[~df.paraules.str.contains("ty")]

# df = df[~df.paraules.str.contains("df")]
# df = df[~df.paraules.str.contains("cm")]
# df = df[~df.paraules.str.contains("cn")]
# df = df[~df.paraules.str.contains("t1")]
# df = df[~df.paraules.str.contains("1t")]
# df = df[~df.paraules.str.contains("1w")]
# df = df[~df.paraules.str.contains("1q")]

# df = df[~df.paraules.str.contains("zy")]
# df = df[~df.paraules.str.contains("zg")]
# df = df[~df.paraules.str.contains("zk")]

# df = df[~df.paraules.str.endswith('k')]

# df = df[~df.paraules.str.startswith('up')]

# df1 = df[df.paraules.str.contains("1a|1o|1u")]
# df2 = df[df.paraules.str.endswith("1")]
# df = df[~df.paraules.str.contains("1")]
# df = pd.concat([df1, df2, df])

# df = df[~df.paraules.str.contains("zx")]
# df = df[~df.paraules.str.contains("zf")]
# df = df[~df.paraules.str.contains("vd")]
# df = df[~df.paraules.str.contains("vl")]

# df1 = df[df.paraules.str.contains("qu")]
# df = df[~df.paraules.str.contains("q")]
# df = pd.concat([df, df1])
# df = df[~df.paraules.str.endswith('qu')]

# df1 = df[df.paraules.str.contains("ny")]
# df = df[~df.paraules.str.contains("y")]
# df = pd.concat([df, df1])

# df = df[~df.paraules.str.contains("kb")]
# df = df[~df.paraules.str.contains("bk")]
# df = df[~df.paraules.str.contains("bw")]
# df = df[~df.paraules.str.contains("wb")]
# df = df[~df.paraules.str.contains("wk")]
# df = df[~df.paraules.str.contains("kw")]
# df = df[~df.paraules.str.contains("k")]

# df1 = df[df.paraules.str.contains("za|ze|zi|zo|zu")]
# df = df[~df.paraules.str.contains("z")]
# df = pd.concat([df, df1])

# df1 = df[df.paraules.str.contains("ja|je|ji|jo|ju")]
# df = df[~df.paraules.str.contains("j")]
# df = pd.concat([df, df1])

df = df[~df.paraules.str.contains("sl")]

print(df)

df.to_csv('diccionarimod.csv', index=False)
# df.to_csv('test.csv', index=False)