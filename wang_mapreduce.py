import couchdb
server = couchdb.Server('http://admin:admin@115.146.86.154:5984/')
db=server['truetweet']
try:
    db2=server.create('result')
except:
    db2=server['result']
viewData_Melbourne={
     "getdata_number":{
        "map":"function(doc){if(doc.place.full_name=='Melbourne, Victoria')emit(doc._id,1)}",
         "reduce":"function (key, values) {   return sum(values); }"},
    "getdata_beer": {
        "map": "function(doc){if(doc.place.full_name=='Melbourne, Victoria'&& doc.beer==false)emit(doc._id,1)}",
        "reduce": "function (key, values) {   return sum(values); }"},
    "getdata_profanity":{
        "map": "function(doc){if(doc.place.full_name=='Melbourne, Victoria'&& doc.profanity==false)emit(doc._id,1)}",
        "reduce": "function (key, values) {   return sum(values); }"},
    "getdata_crime":{
        "map": "function(doc){if(doc.place.full_name=='Melbourne, Victoria'&& doc.crime==false)emit(doc._id,1)}",
        "reduce": "function (key, values) {   return sum(values); }"},
    "getdata_sentiment_positive":{
        "map": "function(doc){if(doc.place.full_name=='Melbourne, Victoria'&& doc.sentiment.compound>0)emit(doc._id,1)}",
        "reduce": "function (key, values) {   return sum(values); }"},
    "getdata_sentiment_neutral":{
        "map": "function(doc){if(doc.place.full_name=='Melbourne, Victoria'&& doc.sentiment.compound==0)emit(doc._id,1)}",
        "reduce": "function (key, values) {   return sum(values); }"},
    "getdata_sentiment_negtive":{
        "map": "function(doc){if(doc.place.full_name=='Melbourne, Victoria'&& doc.sentiment.compound<0)emit(doc._id,1)}",
        "reduce": "function (key, values) {   return sum(values); }"}
    }
viewData_Sydney={
    "getdata_number":{
        "map":"function(doc){if(doc.place.full_name=='Sydney, New South Wales')emit(doc._id,1)}",
         "reduce":"function (key, values) {   return sum(values); }"},
    "getdata_beer": {
        "map": "function(doc){if(doc.place.full_name=='Sydney, New South Wales'&& doc.beer==false)emit(doc._id,1)}",
        "reduce": "function (key, values) {   return sum(values); }"},
    "getdata_profanity":{
        "map": "function(doc){if(doc.place.full_name=='Sydney, New South Wales'&& doc.profanity==false)emit(doc._id,1)}",
        "reduce": "function (key, values) {   return sum(values); }"},
    "getdata_crime":{
        "map": "function(doc){if(doc.place.full_name=='Sydney, New South Wales'&& doc.crime==false)emit(doc._id,1)}",
        "reduce": "function (key, values) {   return sum(values); }"},
    "getdata_sentiment_positive":{
        "map": "function(doc){if(doc.place.full_name=='Sydney, New South Wales'&& doc.sentiment.compound>0)emit(doc._id,1)}",
        "reduce": "function (key, values) {   return sum(values); }"},
    "getdata_sentiment_neutral":{
        "map": "function(doc){if(doc.place.full_name=='Sydney, New South Wales'&& doc.sentiment.compound==0)emit(doc._id,1)}",
        "reduce": "function (key, values) {   return sum(values); }"},
    "getdata_sentiment_negtive":{
        "map": "function(doc){if(doc.place.full_name=='Sydney, New South Wales'&& doc.sentiment.compound<0)emit(doc._id,1)}",
        "reduce": "function (key, values) {   return sum(values); }"}
}
viewData_Perth={
    "getdata_number":{
        "map":"function(doc){if(doc.place.full_name=='Perth, Western Australia')emit(doc._id,1)}",
         "reduce":"function (key, values) {   return sum(values); }"},
    "getdata_beer": {
        "map": "function(doc){if(doc.place.full_name=='Perth, Western Australia'&& doc.beer==false)emit(doc._id,1)}",
        "reduce": "function (key, values) {   return sum(values); }"},
    "getdata_profanity":{
        "map": "function(doc){if(doc.place.full_name=='Perth, Western Australia'&& doc.profanity==false)emit(doc._id,1)}",
        "reduce": "function (key, values) {   return sum(values); }"},
    "getdata_crime":{
        "map": "function(doc){if(doc.place.full_name=='Perth, Western Australia'&& doc.crime==false)emit(doc._id,1)}",
        "reduce": "function (key, values) {   return sum(values); }"},
    "getdata_sentiment_positive":{
        "map": "function(doc){if(doc.place.full_name=='Perth, Western Australia'&& doc.sentiment.compound>0)emit(doc._id,1)}",
        "reduce": "function (key, values) {   return sum(values); }"},
    "getdata_sentiment_neutral":{
        "map": "function(doc){if(doc.place.full_name=='Perth, Western Australia'&& doc.sentiment.compound==0)emit(doc._id,1)}",
        "reduce": "function (key, values) {   return sum(values); }"},
    "getdata_sentiment_negtive":{
        "map": "function(doc){if(doc.place.full_name=='Perth, Western Australia'&& doc.sentiment.compound<0)emit(doc._id,1)}",
        "reduce": "function (key, values) {   return sum(values); }"}
}

viewData_Brisbane={
    "getdata_number":{
        "map":"function(doc){if(doc.place.full_name=='Brisbane, Queensland')emit(doc._id,1)}",
         "reduce":"function (key, values) {   return sum(values); }"},
    "getdata_beer": {
        "map": "function(doc){if(doc.place.full_name=='Brisbane, Queensland'&& doc.beer==false)emit(doc._id,1)}",
        "reduce": "function (key, values) {   return sum(values); }"},
    "getdata_profanity":{
        "map": "function(doc){if(doc.place.full_name=='Brisbane, Queensland'&& doc.profanity==false)emit(doc._id,1)}",
        "reduce": "function (key, values) {   return sum(values); }"},
    "getdata_crime":{
        "map": "function(doc){if(doc.place.full_name=='Brisbane, Queensland'&& doc.crime==false)emit(doc._id,1)}",
        "reduce": "function (key, values) {   return sum(values); }"},
    "getdata_sentiment_positive":{
        "map": "function(doc){if(doc.place.full_name=='Brisbane, Queensland'&& doc.sentiment.compound>0)emit(doc._id,1)}",
        "reduce": "function (key, values) {   return sum(values); }"},
    "getdata_sentiment_neutral":{
        "map": "function(doc){if(doc.place.full_name=='Brisbane, Queensland'&& doc.sentiment.compound==0)emit(doc._id,1)}",
        "reduce": "function (key, values) {   return sum(values); }"},
    "getdata_sentiment_negtive":{
        "map": "function(doc){if(doc.place.full_name=='Brisbane, Queensland'&& doc.sentiment.compound<0)emit(doc._id,1)}",
        "reduce": "function (key, values) {   return sum(values); }"}
}

def creat_design_doc(a, b):
    try:
        db[a] = dict(language='javascript', views=b)
    except:
        del db[a]
        db[a] = dict(language='javascript', views=b)


def get_result_first(a,b,c):
    for row in db.view(a):
        print(row)
        p={c:row.value}
        try:
            db2[b]=dict(p)

        except:
            del db2[b]
            db2[b] = dict(p)
def get_result_other(a,b,c):
    for row in db.view(a):
        print(row)
        data=db2[b]
        data[c]=row.value
        db2.save(data)



creat_design_doc('_design/Melbourne', viewData_Melbourne)
creat_design_doc('_design/Sydney', viewData_Sydney)
creat_design_doc('_design/Perth',viewData_Perth)
creat_design_doc('_design/Brisbane',viewData_Brisbane)



get_result_first('Sydney/getdata_number','result_data','Sydneycount')
get_result_other('Sydney/getdata_beer','result_data',"Sydneybeer")
get_result_other('Sydney/getdata_profanity','result_data',"Sydneyprofanity")
get_result_other('Sydney/getdata_crime','result_data',"Sydneycrime")
get_result_other('Sydney/getdata_sentiment_positive','result_data',"Sydneypositive")
get_result_other('Sydney/getdata_sentiment_neutral','result_data',"Sydneyneutral")
get_result_other('Sydney/getdata_sentiment_negtive','result_data',"Sydneynegtive")



get_result_other('Melbourne/getdata_number','result_data','Melbournecount')
get_result_other('Melbourne/getdata_beer','result_data',"Melbournebeer")
get_result_other('Melbourne/getdata_profanity','result_data',"Melbourneprofanity")
get_result_other('Melbourne/getdata_crime','result_data',"Melbournecrime")
get_result_other('Melbourne/getdata_sentiment_positive','result_data',"Melbournepositive")
get_result_other('Melbourne/getdata_sentiment_neutral','result_data',"Melbourneneutral")
get_result_other('Melbourne/getdata_sentiment_negtive','result_data',"Melbournenegtive")


get_result_other('Perth/getdata_number','result_data','Perthcount')
get_result_other('Perth/getdata_beer','result_data',"Perthbeer")
get_result_other('Perth/getdata_profanity','result_data',"Perthprofanity")
get_result_other('Perth/getdata_crime','result_data',"Perthcrime")
get_result_other('Perth/getdata_sentiment_positive','result_data',"Perthpositive")
get_result_other('Perth/getdata_sentiment_neutral','result_data',"Perthneutral")
get_result_other('Perth/getdata_sentiment_negtive','result_data',"Perthnegtive")

get_result_other('Brisbane/getdata_number','result_data','Brisbanecount')
get_result_other('Brisbane/getdata_beer','result_data',"Brisbanebeer")
get_result_other('Brisbane/getdata_profanity','result_data',"Brisbaneprofanity")
get_result_other('Brisbane/getdata_crime','result_data',"Brisbanecrime")
get_result_other('Brisbane/getdata_sentiment_positive','result_data',"Brisbanepositive")
get_result_other('Brisbane/getdata_sentiment_neutral','result_data',"Brisbaneneutral")
get_result_other('Brisbane/getdata_sentiment_negtive','result_data',"Brisbanenegtive")




