# -*- coding: utf-8 -*-
import os,glob

print '必ず手動でバックアップを取ってください: 危険な行為です'
ans = raw_input('このディレクトリ以下のファイルをrenameしますか? (yes/no): ')

if ans == 'yes':
    for dire in glob.glob('./*'):
        if dire != './rename.py':
            for i,files in enumerate(glob.glob(dire+'/*.JPG')): #一旦全て適当にrenameする
                print files
                os.rename(files,dire+'/dammy{0:02d}'.format(i+100)+'.JPG')
            for i,files in enumerate(glob.glob(dire+'/*.JPG')): #番号でrenameする
                print files
                os.rename(files,dire+'/{0:02d}'.format(i+1)+'.JPG')
                print dire+'/{0:02d}'.format(i+1)+'.JPG'
else:
    print 'renameは行いませんでした.'




