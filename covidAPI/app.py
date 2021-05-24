from flask import Flask, render_template, jsonify,request
from flask_restful import Api, Resource, reqparse
import requests
import json
from bs4 import BeautifulSoup
app = Flask(__name__)
api = Api(app)

class CovidAPI(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('country', type=str)
        args = parser.parse_args()
        s = args['country']
        
        #fetching data from wordometer websites
        url = "https://www.worldometers.info/coronavirus/"
        r = requests.get(url)
        soup = BeautifulSoup(r.text,"html.parser")

        table_data = soup.find_all('table', class_='table table-bordered table-hover main_table_countries')[0]

        #fetching table
        t=table_data.findAll(['tr'])

        #fetching the column name
        th = t[0].find_all('th')
        th_data = [col.text.strip('\n') for col in th]

        #print(th_data)
        data={}
        for cell in t:
            td = cell.find_all('td')
            row = [i.text.replace('\n','') for i in td]
            d={}
            if len(row)==0:
                continue
            for i in range(len(th_data)):
                d[th_data[i]] = row[i]
                
            data[row[1]]= d 
        if s:
            res= data[s]
            responseFormat={}
            responseFormat['Country Name']= res['Country,Other']
            responseFormat['Total Cases']= res['TotalCases']
            responseFormat['Active Cases']= res['ActiveCases']
            responseFormat['Total Death']= res['TotalDeaths']
            s1= "".join(res['TotalRecovered'].split(','))
            s2= "".join(res['Population'].split(','))
            s3= "".join(res['TotalRecovered'].split(','))
            s4= "".join(res['TotalCases'].split(','))
            responseFormat['Percentage of Population Infected ']= int(s1)/int(s2)*100
            responseFormat['Recovery Rate'] = int(s3)/int(s4)*100
            
            return jsonify(responseFormat)
        else:
            return jsonify(data)


api.add_resource(CovidAPI, '/api/getCovidCase')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)

    