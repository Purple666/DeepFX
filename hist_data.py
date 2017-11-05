
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


class HistData:
    def __init__(self, csv_path=None, begin_date=None, end_date=None, range_limited=True):
        self.csv_path = csv_path
        with open(self.csv_path) as f:
            try:
                int(f.readline()[0])
                print('no header')
                header = None
                names = ('Date', 'Open', 'High', 'Low', 'Close', 'Volume')
            except:
                print('header is included')
                header = 0
                names = None
        self.csv_data = pd.read_csv(self.csv_path,
                                    names=names, header=header,
                                    index_col='Date', parse_dates=['Date'],
                                    dtype={'Date': 'str', 'Open': 'float', 'High': 'float', 'Low': 'float', 'Close': 'float', 'Volume': 'int'},
                                    sep=';')
        self.begin_date = begin_date
        self.end_date = end_date
        if range_limited:
            self.csv_data = self.data()
            if(len(self.csv_data) is 0):
                raise ValueError('Given csv in the range was empty.')
        
    def data(self):
        if self.begin_date is None and self.end_date is None:
            return self.csv_data
        else:
            is_in_date_array = (self.csv_data.index >= self.begin_date) &                                 (self.csv_data.index <= self.end_date)
            return self.csv_data.ix[is_in_date_array]
    
    def steps(self):
        return len(self.csv_data) - 1;

    def max_value(self):
        return self.csv_data.max()['Close']

    def min_value(self):
        return self.csv_data.min()['Close']

    def date_at(self, index):
        return self.csv_data.iloc[index].name
    
    def close_at(self, index):
        return self.csv_data.ix[[index], ['Close']].Close[0]
    
    def values_at(self, index):
        return self.csv_data.ix[[index], :]
    #def dates(self):
    #    return self.data().index.values

    #''' 引数の日時がデータフレームに含まれるか '''
    #def has_datetime(self, datetime64_value):
    #    try:
    #        h.data().loc[datetime64_value]
    #        return True
    #    except KeyError:
    #        return False
#
    #def _get_nearist_index(self, before_or_after, datetime):
    #    if before_or_after == 'before':
    #        offset = -1
    #    else:
    #        offset = 0
    #    index = max(h.data().index.searchsorted(datetime) + offset, 0)
    #    return self.data().ix[self.data().index[index]]
#
    #''' 引数の日時を含まない直前に存在する値を取得する '''        
    #def get_last_exist_datetime(self, datetime64_value):
    #    return self._get_nearist_index('before', datetime64_value)
    #    
    #''' 引数の日時を含む直後に存在する値を取得する '''
    #def get_next_exist_datetime(self, datetime64_value):
    #    return self._get_nearist_index('after', datetime64_value)
    #
    #''' fromとtoの日時の差が閾値内にあるか否か '''
    #def is_datetime_diff_in_threshould(self, from_datetime, to_datetime, threshold_timedelta):
    #    last_datetime = h.get_last_exist_datetime(from_datetime)
    #    next_exist_datetime = h.get_next_exist_datetime(to_datetime)
    #    delta = next_exist_datetime.name - last_datetime.name
    #    return delta <= threshold_timedelta


# In[ ]:


if __name__ == '__main__':
    import numpy as np
    begin = '2017-10-01T00:00:00'
    end = '2017-10-07T23:59:59'
    
    hd = HistData(csv_path = 'historical_data/DAT_ASCII_USDJPY_M1_201710_m5.csv',
                     begin_date=begin,
                     end_date=end)
    #print(hd.data())
    print(hd.max_value())
    print(hd.min_value())
    print(hd.date_at(1))
    print(hd.close_at(1))
    print(hd.values_at(1))


# In[ ]:




