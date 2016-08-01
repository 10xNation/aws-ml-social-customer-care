# The following parameters are used to create the Amazon Kinesis
# stream, AWS Lambda function that reads from the stream and the
# Amazon SNS topic Lambda will publish to whenever a tweet is
# classified as actionable.
AWS = {
  'awsAccountId' : 'xxxxxxxxxxxx',
  'kinesisStream' : 'tweetStream',
  'lambdaExecutionRole' : 'tweetStreamExecutionRole',
  'lambdaFunctionName' : 'classifyTweet',
  'mlModelId' : 'tweetStreamModel',
  'region' : 'us-east-1',
  'snsTopic' : 'actionableTweets'
}

# The parameters below are used by scanner.py to read tweets from the
# public stream twitter API[1] and push them to a kinesis
# stream. Configure this with twitter credentials for your own application[2]
#
# [1] https://dev.twitter.com/streaming/reference/post/statuses/filter
# [2] https://apps.twitter.com
# Twitter app OAuth settings
CONSUMER_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_TOKEN_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# Learn more about how this filter is used by Twitter's API
# https://dev.twitter.com/streaming/reference/post/statuses/filter
TWITTER_FILTER = 'aws'

# Learn more about Kinesis partitions
# http://docs.aws.amazon.com/kinesis/latest/dev/amazon-kinesis-producers.html
KINESIS_STREAM = AWS['kinesisStream']
KINESIS_PARTITION = 'demo'
