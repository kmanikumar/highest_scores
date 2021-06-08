# Highest Scores

### Pre-Requisites
* python3
* nothing else!

###  How to run with sample data files
```
python3 <script_filename> <data_filename> <# top results>
python3 ./batch_highest.py score_recs.data 3
python3 ./stream_highest.py score_recs.data 4
```
###  Batch vs Stream
* batch_highest.py uses a quickselect based algorithm, suitable for finding k highest scores and IDs for batches
* stream_highest.py uses a min-heap based algorithm, suitable for finding k highest scores and IDs at any point in a stream of data 
