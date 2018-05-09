import couchdb
server = couchdb.Server('http://admin:admin@115.146.86.154:5984/')
try:
    db2=server.create('result')
except:
    db2=server['result']
db=server['try']
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
# "Brisbane, Queensland"
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

get_result_first('Sydney/getdata_number','Sydney_New_South_Wales','count')
get_result_other('Sydney/getdata_beer','Sydney_New_South_Wales',"beer")
get_result_other('Sydney/getdata_profanity','Sydney_New_South_Wales',"profanity")
get_result_other('Sydney/getdata_crime','Sydney_New_South_Wales',"crime")
get_result_other('Sydney/getdata_sentiment_positive','Sydney_New_South_Wales',"positive")
get_result_other('Sydney/getdata_sentiment_neutral','Sydney_New_South_Wales',"neutral")
get_result_other('Sydney/getdata_sentiment_negtive','Sydney_New_South_Wales',"negtive")



get_result_first('Melbourne/getdata_number','Melbourne_Victoria','count')
get_result_other('Melbourne/getdata_beer','Melbourne_Victoria',"beer")
get_result_other('Melbourne/getdata_profanity','Melbourne_Victoria',"profanity")
get_result_other('Melbourne/getdata_crime','Melbourne_Victoria',"crime")
get_result_other('Melbourne/getdata_sentiment_positive','Melbourne_Victoria',"positive")
get_result_other('Melbourne/getdata_sentiment_neutral','Melbourne_Victoria',"neutral")
get_result_other('Melbourne/getdata_sentiment_negtive','Melbourne_Victoria',"negtive")


get_result_first('Perth/getdata_number','Perth_Western_Australia','count')
get_result_other('Perth/getdata_beer','Perth_Western_Australia',"beer")
get_result_other('Perth/getdata_profanity','Perth_Western_Australia',"profanity")
get_result_other('Perth/getdata_crime','Perth_Western_Australia',"crime")
get_result_other('Perth/getdata_sentiment_positive','Perth_Western_Australia',"positive")
get_result_other('Perth/getdata_sentiment_neutral','Perth_Western_Australia',"neutral")
get_result_other('Perth/getdata_sentiment_negtive','Perth_Western_Australia',"negtive")

get_result_first('Brisbane/getdata_number','Brisbane_Queensland','count')
get_result_other('Brisbane/getdata_beer','Brisbane_Queensland',"beer")
get_result_other('Brisbane/getdata_profanity','Brisbane_Queensland',"profanity")
get_result_other('Brisbane/getdata_crime','Brisbane_Queensland',"crime")
get_result_other('Brisbane/getdata_sentiment_positive','Brisbane_Queensland',"positive")
get_result_other('Brisbane/getdata_sentiment_neutral','Brisbane_Queensland',"neutral")
get_result_other('Brisbane/getdata_sentiment_negtive','Brisbane_Queensland',"negtive")


