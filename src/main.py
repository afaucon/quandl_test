import quandl

quandl.ApiConfig.api_key = 'xzWdz9s66uqKCAFQjiFw'
quandl.ApiConfig.api_version = '2015-04-09'

data = quandl.get('NSE/OIL')
print (data.head())