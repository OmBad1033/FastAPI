from pymongo import MongoClient

MONGO_URI='mongodb+srv://ombad:messi1033om@cluster0.aqbw0sc.mongodb.net'
#MONGO_URI='mongodb+srv://ombad:messi1033om@cluster0.aqbw0sc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

#MONGO_URI='mongodb+srv://FatBoy123:ThinBoy@cluster0.aqbw0sc.mongodb.net'

conn=MongoClient(MONGO_URI)