#!/usr/bin/env python

import boto3
import pprint

BUCKET = 'smartthings-amielke-test'

def enumerate_keys():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(BUCKET)
    return [obj.get() for obj in bucket.objects.all() if '.key' in obj.key]

def main():
    keys = enumerate_keys()
    for key in keys:
        pprint.pprint(key['Body'].read())
    # load_keys(keys)

if __name__ == '__main__':
    main()
