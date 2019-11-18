import requests

from datetime import datetime

class Score:
	def __init__(self):
		self.url_of_matches="http://cricapi.com/api/matches"
		self.get_score="http://cricapi.com/api/cricketScore"
		self.apikey="Your Generated api Key"       #Put your generated api key here.
		self.unique_id=""

	def get_unique_id(self):

		uri_params={"apikey":self.apikey}
		resp=requests.get(self.url_of_matches,params=uri_params)
		resp_dict=resp.json()
		uid_found=0
		x1=raw_input("Enter Team1 Name:  ")
		x2=raw_input("Enter Team2 Name:  ")
		for i in resp_dict['matches']:
			if(i['team-1']==x1 or i['team-2']==x2 and i['matchStarted']):

				today_date=datetime.today().strftime('%Y-%m-%d')

				if today_date==i['date'].split("T")[0]:
					self.unique_id=i['unique_id']
					uid_found=1
					break


		if not uid_found:
			self.unique_id=-1

		send_data=self.get_current_score(self.unique_id)
		print(send_data)

	def get_current_score(self,unique_id):
		data=""

		if unique_id==-1:
			data="No matches today OR match not started yet"
		else:
			uri_params={"apikey":self.apikey,"unique_id":unique_id}
			resp=requests.get(self.get_score,params=uri_params)
			data_json=resp.json()

			try:
				data="Here is the score: \n"+data_json['stat']+"\n"+data_json['score']
			except KeyError as e:
				print (e)


		return data

if __name__=="__main__":

	obj_score=Score()
	obj_score.get_unique_id()
