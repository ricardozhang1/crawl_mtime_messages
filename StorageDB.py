#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

class DataOutPut(object):
    def __init__(self):
        self.cx = sqlite3.connect("MTime.db")
        self.create_table("MTime")
        self.datas = []


    def create_table(self,table_name):
        value = '''
            id integer primary key,
            MovieId integer,
            MovieTitle varcha(40) NOT NULL,
            RatingFinal REAL NOT NULL DEFAULT 0.0,
            ROtherFinal REAL NOT NULL DEFAULT 0.0,
            RPictureFinal REAL NOT NULL DEFAULT 0.0,
            RDirectorFinal REAL NOT NULL DEFAULT 0.0,
            RStoryFinal REAL NOT NULL DEFAULT 0.0,
            Usercount integer NOT NULL DEFAULT 0,
            AttitudeCount integer NOT NULL DEFAULT 0,
            TotalBoxOffic varchar(20) NOT NULL,
            TodayBoxOffice varchar(20) NOT NULL,
            Rank integer NOT NULL DEFAULT 0,
            ShowDays integer NOT NULL DEFAULT 0,
            isRelease integer NOT NULL
        '''
        self.cx.execute('CREATE TABLE IF NOT EXISTS %s (%s)'%(table_name,value))

    def store_data(self,data):
        if data is None:
            return
        self.datas.append(data)
        if len(self.datas)>10:
            self.output_db('MTime')

    def output_db(self,table_name):
        for data in self.datas:
           self.cx.execute('''INSERT INTO %s (MovieId,MovieTitle,RatingFinal,ROtherFinal,RPictureFinal,RDirectorFinal,RStoryFinal,Usercount,AttitudeCount,TotalBoxOffic,TodayBoxOffice,Rank,ShowDays,isRelease) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''%table_name,data)
           self.datas.remove(data)
        self.cx.commit()


    def output_end(self):
        if len(self.datas)>0:
            self.output_db('MTime')
        self.cx.close()


if __name__ == '__main__':
    b = (1,'125','水电费红素','3','0','0','0','0','1','1','jusdc','fgsd','0','60')
    a = DataOutPut()
    a.store_data(b)